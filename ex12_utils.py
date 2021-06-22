def is_valid_path(board, path, words):
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
        if not valid_point(coord, board):
            # print("invalid location -- not on board") # debugging purposes
            return None  # invalid location -- not on board
        word += board[row][col]

    # print('is_valid_path found word: ', word)  # debugging purposes
    return word if word in words else None


NEIGHBORS = [
    (-1, 0),  # up
    (0, 1),  # right
    (1, 0),  # down
    (0, -1),  # left
    (-1, 1),  # dur
    (1, 1),  # ddr
    (1, -1),  # ddl
    (-1, -1)  # dul
]


def find_length_n_paths(n, board, words):
    """
       returns a list of all paths who are as long as <n>
       e.g: for n == 2, return value might be [[(0,0), (1,0)], [(0,0), (0,1)]]

        :param n: {int} -- length of paths to find
        :param board: {[[str]]} -- board game
        :param words: {[str]} -- list of words
    """
    paths = []
    words_me = []
    #  todo change iterates
    for row in range(len(board)):
        for col in range(len(board[0])):
            _find_length_n_paths_helper(n, board, words, (row, col), paths, [(row, col)], words_me)
    return paths


# * changes <paths> list:
def _find_length_n_paths_helper(n, board, words, start, paths, curr_path, words_me):
    if len(curr_path) == n:
        res = is_valid_path(board, curr_path, words)
        if res:
            words_me.append(res)  # todo check for what
            paths.append(curr_path)
        return False

    for neighbor in NEIGHBORS:
        new_loc = tuple(loc + nei for loc, nei in zip(start, neighbor))
        if valid_point(new_loc, board):
            _find_length_n_paths_helper(n, board, words, new_loc, paths, curr_path + [new_loc], words_me)


def valid_point(coordinate, board):
    row, col = coordinate
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
        return False
    return True


def find_length_n_words(n, board, words):
    pass


def max_score_paths(board, words):
    pass


def get_words(words_file):
    with open(words_file, 'r') as file:
        return [word.rstrip() for word in file]
