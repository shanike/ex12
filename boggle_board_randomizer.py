import random

BOARD_SIZE = 4
LETTERS = [
    ['A', 'E', 'A', 'N', 'E', 'G'],
    ['A', 'H', 'S', 'P', 'C', 'O'],
    ['A', 'S', 'P', 'F', 'F', 'K'],
    ['O', 'B', 'J', 'O', 'A', 'B'],
    ['I', 'O', 'T', 'M', 'U', 'C'],
    ['R', 'Y', 'V', 'D', 'E', 'L'],
    ['L', 'R', 'E', 'I', 'X', 'D'],
    ['E', 'I', 'U', 'N', 'E', 'S'],
    ['W', 'N', 'G', 'E', 'E', 'H'],
    ['L', 'N', 'H', 'N', 'R', 'Z'],
    ['T', 'S', 'T', 'I', 'Y', 'D'],
    ['O', 'W', 'T', 'O', 'A', 'T'],
    ['E', 'R', 'T', 'T', 'Y', 'L'],
    ['T', 'O', 'E', 'S', 'S', 'I'],
    ['T', 'E', 'R', 'W', 'H', 'V'],
    ['N', 'U', 'I', 'H', 'M', 'QU']
]


def randomize_board(dice_list=LETTERS):
    dice_indices = list(range(len(dice_list)))
    random.shuffle(dice_indices)
    dice_indices_iter = iter(dice_indices)
    board = []
    for i in range(BOARD_SIZE):
        row = []
        for j in range(BOARD_SIZE):
            die = dice_list[next(dice_indices_iter)]
            letter = random.choice(die)
            row.append(letter)
        board.append(row)
    return board


if __name__ == "__main__":
    from pprint import pprint
    from ex12_utils import is_valid_path, get_words, find_length_n_paths, find_length_n_words, max_score_paths
    import time

    board = randomize_board()
    lots_of_words = get_words('./boggle_dict.txt')

    pprint(board)

    # start1 = time.time()
    # res = find_length_n_paths(5, board, lots_of_words)
    # end1 = time.time()
    # print("find_length_n_paths took:", end1 - start1)

    # start2 = time.time()
    # res2 = find_length_n_words(5, board, lots_of_words)
    # end2 = time.time()
    # print("find_length_n_words took:", end2 - start2)
    #
    # start3 = time.time()
    # res = max_score_paths(board, lots_of_words)
    # end3 = time.time()
    # print("res: ", res)
    # print("max_score_paths took:", end3 - start3)
