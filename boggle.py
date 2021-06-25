from ex12_utils import _is_my_neighbor, calc_score, get_words, is_valid_path
from ScreenGUI import ScreenGUI
from boggle_board_randomizer import randomize_board
from pprint import pprint


class Boggle:
    def __init__(self):
        self.__screen = ScreenGUI(self._handle_guess)

        # init board:
        self.__board = []
        self.__board_list = []
        self.__init_board()

        # init words:
        self.__words = []
        self.__init_words()

        # init curr path:
        self.__curr_path = []
        self.__curr_path_label = []

        # init score:
        self.__score = 0
        self.__update_score()

        self.__update_board()

        self.start_game()

    def start_game(self):
        self.__screen.root.mainloop()

    def __init_board(self):
        board_list = randomize_board()
        board_dict = []
        for row in board_list:
            board_dict.append([])
            for col in row:
                board_dict[-1].append({col: False})
        self.__board = board_dict
        self.__board_list = board_list

    def __init_words(self):
        """saves words from ./boggle_dict.txt file in __words list
        """
        self.__words = get_words('./boggle_dict.txt')

    def __update_board(self):
        """updates board
        """
        self.__screen.display_board(self.__board, self.handle_cell_selection)

    def __update_path_label(self):
        """update screen's current words path text
        """
        self.__screen.update_curr_path_label("".join(self.__curr_path_label))

    def __update_score(self):
        self.__screen.update_score_label(self.__score)

    def handle_cell_selection(self, cell_value, i, j):
        selected_loc = (i, j)
        if self.__board[i][j][cell_value]:
            # unselect cell:
            # todo check that path will be valid
            self.__board[i][j][cell_value] = False  # update board
            self.__curr_path.remove(selected_loc)  # update path
            self.__curr_path_label.remove(cell_value)  # update label
            self.__update_path_label()
            self.__update_board()
        else:
            if len(self.__curr_path) == 0 or _is_my_neighbor(selected_loc, self.__curr_path[-1]):
                self.__board[i][j][cell_value] = True  # update board
                self.__curr_path.append(selected_loc)  # update path
                self.__curr_path_label.append(cell_value)  # update label
                self.__update_path_label()
                self.__update_board()
            else:
                print("not good")
                self.__screen.set_err_msg("not neighbor")

    def _handle_guess(self):
        word = is_valid_path(self.__board_list, self.__curr_path, self.__words)
        if not word:
            self.__screen.set_err_msg("not a valid word, sorry (:")
        else:
            # found valid word:
            self.__screen.set_err_msg("nice job!")
            self.__score += calc_score(self.__curr_path)  # change score

            for loc in self.__curr_path:  # change board
                val = list(self.__board[loc[0]][loc[1]].items())[0][0]
                self.__board[loc[0]][loc[1]] = {val: False}

            self.__screen.add_word_to_list("".join(self.__curr_path_label))

            self.__curr_path = []  # change path
            self.__curr_path_label = []  # change word
            self.__update_score()
            self.__update_board()
            self.__update_path_label()


if __name__ == "__main__":
    Boggle()
