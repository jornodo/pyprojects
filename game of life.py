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


def check_state(s_list):
    checked_list = []

    # Checks
    for i in range(len(s_list)):
        checked_list.append(s_list[i].copy())

    def find_neighboors(i, j):
        neighboors = 0

        # Could possibly be done with one set of requisites for checks, and a try/except
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

            elif j < (len(s_list[i])-1):
                if s_list[i][j - 1]:
                    neighboors += 1
                if s_list[i][j + 1]:
                    neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
                if s_list[i + 1][j + 1]:
                    neighboors += 1
            else:
                if s_list[i][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
        elif i > 0 and i != (len(s_list[i])-1):
            if j == 0:
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i - 1][j + 1]:
                    neighboors += 1
                if s_list[i][j + 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
                if s_list[i + 1][j + 1]:
                    neighboors += 1

            elif j < (len(s_list[i])-1):
                if s_list[i - 1][j - 1]:
                    neighboors += 1
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i - 1][j + 1]:
                    neighboors += 1
                if s_list[i][j - 1]:
                    neighboors += 1
                if s_list[i][j + 1]:
                  neighboors += 1
                if s_list[i + 1][j - 1]:
                    neighboors += 1
                if s_list[i + 1][j]:
                    neighboors += 1
                if s_list[i + 1][j + 1]:
                   neighboors += 1

            elif j == (len(s_list[i])-1):
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

            if j == (len(s_list[i])-1):
                if s_list[i - 1][j - 1]:
                    neighboors += 1
                if s_list[i - 1][j]:
                    neighboors += 1
                if s_list[i][j - 1]:
                    neighboors += 1

        return neighboors


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

def make_boollist_int(bool_list):
    numeral_list = bool_list.copy()
    for i in range(len(bool_list)):
        for j in range(len(bool_list[i])):
            numeral_list[i][j] = int(bool_list[i][j])
    return numeral_list


def main_func(boardsize, rounds):
    # creates a n*n size list of booleans
    game = partial(to_list, get_bool, boardsize)
    original_state = to_list(game, boardsize).copy()

    def print_list(s_list):
        printed_list = make_boollist_int(s_list).copy()
        for i in range(len(printed_list)):
            print(printed_list[i])
        print('\n\n')

    def run_game():
        m_list = original_state.copy()
        print_list(original_state)
        time.sleep(1)
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
                m_list = check_state(m_list).copy()
                print_list(m_list)
            else:
                m_list = check_state(m_list).copy()
                print_list(m_list)

            time.sleep(1)

    run_game()


main_func(5, 100)

