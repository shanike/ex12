# import numpy
from constants import NEIGHBORS


def is_valid_path(board, path, words):
    """
        returns None if path is not a valid path, or if the word created through the path is not in the words list.
        otherwise returns the word

        :param board: {[[str]]} -- board game
        :param path: {[tuple]} -- [(0,0), (0,1)] -- a path on the board, where each location is a tuple: [0] is row [1] is col
        :param words: {[str]} -- list of words
    """

    word = ""
    if _does_have_duplicates(path):
        return None
    for i, coord in enumerate(path):
        row, col = coord
        if not _is_coord_on_board(coord, board):
            return None

        if i != len(path) - 1:  # not last -- there's another coord to check after me
            if not _is_my_neighbor(coord, path[i + 1], board):
                # not last coord in path + next coord is a neighbor of mine
                return None
        word += board[row][col]

    return word if word in words else None


def find_length_n_paths(n, board, words):
    """
       returns a list of all paths who are as long as <n>
       e.g: for n == 2, return value might be [[(0,0), (1,0)], [(0,0), (0,1)]]

        :param n: {int} -- length of paths to find
        :param board: {[[str]]} -- board game
        :param words: {[str]} -- list of words
    """
    if n > len(board) * len(board[0]):
        # not enough letters on board to create a <n>'s length path
        return []
    paths = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            curr_loc = (row, col)
            _find_length_n_paths_helper(n, board, words, curr_loc, paths, [curr_loc], _get_letter(board, curr_loc))
    return paths


def _find_length_n_paths_helper(n, board, words, start, paths, curr_path, curr_word):
    """
    recursive function that checks all paths of length <n> and appends to <paths> list only the paths which create a
    word which is in the <words> list
    * changes <paths> param

    :param start: tuple of row, col -- current location in path in board
    :param paths: list of paths -- the list to which good paths are added to
    :param curr_path: list of locations (tuples) -- path while it's being created
    :param curr_word: str -- word being created of the path being created
    """
    if len(curr_path) == n:
        print("curr_path: ", curr_path, curr_word)
        # finished this path, check word
        if curr_word in words:
            paths.append(curr_path)
        return False

    for neighbor in NEIGHBORS:
        new_loc = tuple(loc + nei for loc, nei in zip(start, neighbor))  # jump to next location
        if _is_coord_on_board(new_loc, board):  # check if new location is on the board...
            curr_letter = _get_letter(board, new_loc)
            _find_length_n_paths_helper(n, board, words, new_loc, paths, curr_path + [new_loc], curr_word + curr_letter)


def find_length_n_words(n, board, words):
    """
    returns a list of all paths which represents a word as long as <n>
    :param n: {int} -- length of words to find their paths
    :param board: {[[str]]} -- board game
    :param words: {[str]} -- list of words
    """
    words_n_length = {word for word in words if len(word) == n}
    if not len(words_n_length):
        return []
    paths = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            curr_loc = (row, col)
            _find_length_n_words_helper(n, board, words_n_length, curr_loc, paths, [curr_loc],
                                        _get_letter(board, curr_loc))

    return paths


def _find_length_n_words_helper(n, board, words, start, paths, curr_path, curr_word):
    """
    (recursive) helper for find_length_n_words of <words> in given <board>
    """
    if len(curr_word) >= n:
        if len(curr_word) == n and curr_word in words:
            paths.append(curr_path)
        return

    for neighbor in NEIGHBORS:
        new_loc = _get_neighbor_loc(start, neighbor)  # jump to next location
        if _is_coord_on_board(new_loc, board) and new_loc not in curr_path:
            curr_letter = _get_letter(board, new_loc)
            _find_length_n_words_helper(n, board, words, new_loc, paths, curr_path + [new_loc], curr_word + curr_letter)


def max_score_paths(board, words):
    # todo
    pass


def get_words(words_file):
    """
    returns a list of lines from given file name (:param word_file:)

    :param words_file: {str} -- file name

    Returns:
        list -- a list in which each item is a stripped line from file
    """
    with open(words_file, 'r') as file:
        return [word.rstrip() for word in file]


def _is_coord_on_board(coordinate, board):
    row, col = coordinate
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    return True


def _get_neighbor_loc(loc, neighbor_tuple):
    """
    calculates neighbor's location
    :param loc: (row, col)
    :param neighbor_tuple: one of NEIGHBOR const items
    :return: location of neighbor
    """
    return tuple(loc + nei for loc, nei in zip(loc, neighbor_tuple))


def _is_my_neighbor(coord, next_coord):
    """
    checks if given <coord> and <next_coord> are neighbors
    :type coord: (row, col)
    :type next_coord: (row, col)
    """
    for nei in NEIGHBORS:
        if _get_neighbor_loc(coord, nei) == next_coord:
            return True
    return False


def _get_letter(board, coordinate):
    """
    returns value of given coordinate
    :param coordinate: (row, col)
    :type coordinate: tuple (length: 2)
    """
    return board[coordinate[0]][coordinate[1]]


def _does_have_duplicates(container):
    """
    checks if a container has duplicate items by converting container to a set
    :rtype: bool
    """
    return len(set(container)) != len(container)
