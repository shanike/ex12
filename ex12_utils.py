from constants import NEIGHBORS, FOUNT_MAX_FOR_WORD


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
            if not _is_my_neighbor(coord, path[i + 1]):
                # not last coord in path + next coord is a neighbor of mine
                return None
        word += board[row][col]

    return word if word in words else None


def find_length_n_paths(n, board, words):
    """
       returns a list of all paths which are as long as <n> and which create a word which is in <words>
       e.g: for n == 2, return value might be [[(0,0), (1,0)], [(0,0), (0,1)]]

        :param n: {int} -- length of paths to find
        :param board: {[[str]]} -- board game
        :param words: {[str]} -- container of words
    """
    if n > (len(board) * len(board[0])):
        # not enough items on board to create a <n>'s length path
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
        # finished this path, check word
        if curr_word in words:
            paths.append(curr_path)
        return

    for neighbor in NEIGHBORS:
        new_loc = _get_neighbor_loc(start, neighbor)  # jump to next location
        # check if new location is on the board...
        # or if current path already traveled to this loc
        if not _is_coord_on_board(new_loc, board) or new_loc in curr_path:
            continue
        new_word = curr_word + _get_letter(board, new_loc)

        _find_length_n_paths_helper(n, board, {word for word in words if word.startswith(curr_word)}, new_loc, paths, curr_path + [new_loc], new_word)


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
            _find_length_n_words_helper(n, board, list(words_n_length), curr_loc, paths, [curr_loc],
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
    if not len(words):
        return
    for neighbor in NEIGHBORS:
        new_loc = _get_neighbor_loc(start, neighbor)  # jump to next location
        if not _is_coord_on_board(new_loc, board) or new_loc in curr_path:
            continue
        curr_letter = _get_letter(board, new_loc)

        _find_length_n_words_helper(n, board, {word for word in words if word.startswith(curr_word)},
                                    new_loc, paths,
                                    curr_path + [new_loc],
                                    curr_word + curr_letter)


# def find_length_n_words_2(n, board, words):
#     paths = []
#     for word in words:
#         _find_length_n_words_2_helper(n, board, words, paths, )
#
#     return paths


# def _find_length_n_words_2_helper(n, board, words, paths, start, curr_path, curr_word):
#     for row in range(len(board)):
#         for col in range(len(board[0])):
#             _find_length_n_words_2_helper(n, board, words, paths, )


def max_score_paths(board, words):
    # go over words, for each word: find path that might make word out
    paths = {}
    for word in words:
        break_to_next_word = False
        for row in range(len(board)):
            if break_to_next_word:
                break
            for col in range(len(board[0])):
                curr_loc = (row, col)
                cell_res = _max_score_paths_helper(board, paths, curr_loc, word, [curr_loc],
                                                   _get_letter(board, curr_loc))
                if cell_res == FOUNT_MAX_FOR_WORD:
                    break_to_next_word = True
                    break
    return list(paths.values())


def _max_score_paths_helper(board, paths, curr_loc, word, curr_path, curr_word):
    if not word.startswith(curr_word):
        # no reason to check paths from this cell in board, cos none will match <word>
        return

    if curr_word == word:
        if len(curr_path) == len(word):
            # max points for this word,
            paths[word] = curr_path
            return FOUNT_MAX_FOR_WORD
        if word not in paths or len(curr_path) > len(paths[word]):
            paths[word] = curr_path
        return

    for neighbor in NEIGHBORS:
        new_loc = _get_neighbor_loc(curr_loc, neighbor)  # jump to next location
        if not _is_coord_on_board(new_loc, board) or new_loc in curr_path:
            continue
        curr_letter = _get_letter(board, new_loc)
        _max_score_paths_helper(board, paths, new_loc, word, curr_path + [new_loc], curr_word + curr_letter)


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


##########################################
#                                        #
#      utils, used in other files:       #
#                                        #
##########################################

def bind_values_to_func(fn, *args, **kwargs):
    """
        returns a function that calls given <fn> with given params 
        (will pass the relevant information thanks to this closure)
        """
    return lambda: fn(*args, **kwargs)
