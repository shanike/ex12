from typing import List, Tuple


def is_valid_path(board, path: List[Tuple[int, int]], words):
    """
        returns None if path is not a valid path, or if the word created through the path is not in the words list.
        otherwise returns the word

        :param board: {[[str]]} -- board game
        :param path: {[tuple]} -- [(0,0), (0,1)] -- a path on the board, where each location is a tuple: [0] is row [1] is col
        :param words: {[str]} -- list of words
    """
    word = ""
    for coord in path:
        row, col = coord
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            # print("invalid location -- not on board") # debugging purposes
            return None  # invalid location -- not on board
        word += board[row][col]

    print('is_valid_path found word: ', word); # debugging purposes
    return word if word in words else None


def find_length_n_paths(n, board, words):
    pass


def find_length_n_words(n, board, words):
    pass


def max_score_paths(board, words):
    pass


def get_words(words_file):
    with open(words_file, 'r') as file:
        return [word.rstrip() for word in file]
