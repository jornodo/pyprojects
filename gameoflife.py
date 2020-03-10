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
    rand = random.randint(0, 9)
    if rand < 3:
        return True
    else:
        return False


def check_state(s_list):
    checked_list = []

    for i in range(len(s_list)):
        checked_list.append(s_list[i].copy())

    def find_neighbors(i, j):
        neighbors = 0
        neighbor_loc = [[i-1, j-1], [i, j-1], [j+1, j-1], [i, j-1], [i, j+1], [i+1, j-1], [i+1, j], [i+1, j+1]]
        for loc in neighbor_loc:
            try:
                if s_list[loc[0]][loc[1]]:
                    neighbors += 1
            except IndexError:
                pass

        return neighbors

    def alive(i, j, neighbors):
        # endrer verdi for index i liste
        if neighbors < 2:
            checked_list[i][j] = False
        elif neighbors == 2 or neighbors == 3:
            pass
        elif neighbors > 3:
            checked_list[i][j] = False

    def not_alive(i, j, neighbors):
        if neighbors == 3:
            checked_list[i][j] = True

    def iter_list():
        for i in range(len(s_list)):
            for j in range(len(s_list[i])):
                neighbors = find_neighbors(i, j)

                if s_list[i][j]:
                    alive(i, j, neighbors)
                else:
                    not_alive(i, j, neighbors)

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


main_func(5, 1000000)
