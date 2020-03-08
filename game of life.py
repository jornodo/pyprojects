# Game of Life
import random
import time
from functools import partial
from functools import reduce


def to_list(func, n):
    result = []
    for i in range(n):
        result.append(func())
    return result


def get_bool():
    rand = random.randint(0, 1)
    if rand == 1:
        return True
    else:
        return False


def make_list(list_func, n):
    return to_list(list_func, n)


def check_state(s_list):
    checked_list = s_list

    def find_neighboors(i, j):
        neighboors = 0

        '''
        if i and j both is 0 --> check list[i][j+1], list[i+1][j], list[i+1][j+1] DONE

        if i is 0, and j > 0 --> check list[i][j-1] list[i][j+1] list[i+1][j-1 ---> j+1] DONE

        if i > 0 and J is 0 -> list[i-1][j -> j+1], list[i][j+1], list[i+1][j -> j+1] DONE 

        if i > 0 and j > 0 --> check list[i-1][j -> j+2], list[i][j-1 og j+1], og list[i+1][j-1 -> j+1] DONE    

        i == 0, j == len(list[i][j]) --> check list[i][j-1], list[i+1][j-1] list[i+1][j] DONE 

        i > 0, j ==  len(list[i][j]) --> check list[i-1 -> i+1][j-1], list[i-1, i+1][j] Done

        i == len(list[i]), j == 0 DONE 

        i == len(list[i]), j == len(list[i][j]) DONE


        all lines commented out gave indexOutOfRangeException


        '''
        if i == 0:
            if j == 0:
                if s_list[i][j + 1]:
                    neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
                if s_list[i + 1][j + 1]:
                    neighboors += 1

            elif j < len(s_list[i]):
                if s_list[i][j - 1]:
                    neighboors += 1
                # if s_list[i][j + 1]:
                #   neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
            #   if s_list[i + 1][j + 1]:
            #      neighboors += 1
            else:
                if s_list[i][j - 1]:
                    if s_list[i][j + 1]:
                        neighboors += 1
                    if s_list[i + 1][j - 1]:
                        neighboors += 1
                    if s_list[i + 1][j]:
                        neighboors += 1
        elif i > 0 and i != len(s_list[i]):
            if j == 0:
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i - 1][j + 1]:
                    neighboors += 1
                if s_list[i][j + 1]:
                    neighboors += 1
            #    if s_list[i + 1][j]:
            #        neighboors += 1
            #    if s_list[i + 1][j + 1]:
            #        neighboors += 1

            elif j < len(s_list[i]):
                if s_list[i - 1][j - 1]:
                    neighboors += 1
                if s_list[i - 1][j]:
                    neighboors += 1
                #   if s_list[i - 1][j + 1]:
                #      neighboors += 1
                if s_list[i][j - 1]:
                    neighboors += 1
            #   if s_list[i][j + 1]:
            #      neighboors += 1
            #    if s_list[i + 1][j - 1]:
            #        neighboors += 1
            #    if s_list[i + 1][j]:
            #        neighboors += 1
            #    if s_list[i + 1][j + 1]:
            #       neighboors += 1

            elif j == len(s_list[i]):
                if s_list[i - 1][j - 1]:
                    neighboors += 1
                if s_list[i][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
                if s_list[i - 1][j]:
                    neighboors += 1
        else:
            if j == 0:
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i - 1][j + 1]:
                    neighboors += 1
                if s_list[i][j + 1]:
                    neighboors += 1

            if j == len(s_list[i]):
                if s_list[i - 1][j - 1]:
                    neighboors += 1
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i][j - 1]:
                    neighboors += 1

        return neighboors

    # alive og not_alive er uferdige, og trenger parameter: i, j, iter_list skal ikke sette verdier av checked list,
    # det skal alive og not alive gjøre
    def alive(i, j, neighboors):
        # endrer verdi for index i liste
        if neighboors < 2:
            checked_list[i][j] = False
        elif neighboors == 2 or neighboors == 3:
            pass
        elif neighboors > 3:
            checked_list[i][j] = False

    def not_alive(i, j, neighboors):
        if neighboors == 3:
            checked_list[i][j] = True

    def iter_list():
        for i in range(len(s_list)):
            for j in range(len(s_list[i])):
                neighboors = find_neighboors(i, j)

                if s_list[i][j]:
                    alive(i, j, neighboors)
                else:
                    not_alive(i, j, neighboors)

    iter_list()
    return checked_list


def main_func(boardsize, rounds):
    # creates a n*n size list of booleans
    game = partial(to_list, get_bool, boardsize)
    original_state = to_list(game, boardsize)

    def print_list(s_list):
        for i in range(len(s_list)):
            print(s_list[i])
        print('\n\n')

    def run_game():
        m_list = original_state
        print_list(original_state)
        #time.sleep(1)
        for i in range(rounds):

            # Breaks if all cells are dead
            s_sum = 0
            for j in range(len(m_list)):
                s_sum += reduce(lambda x, y: x + y, m_list[j])
            if s_sum == 0:
                print('All cells died during round %i\n\nOriginal set of cells:\n' % (i + 1))
                print_list(original_state)
                break

            if i == 0:
                m_list = check_state(original_state)
                print_list(m_list)
            else:
                m_list = check_state(m_list)
                print_list(m_list)

            # time.sleep(1)

    run_game()


main_func(5, 100)

