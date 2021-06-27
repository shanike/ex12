from ex12_utils import _is_my_neighbor, calc_score, get_words, is_valid_path
from ScreenGUI import ScreenGUI
from boggle_board_randomizer import randomize_board
from pprint import pprint


class Boggle:
    def __init__(self):
        self.__gui = ScreenGUI(on_start_game=self.__start_game)

        # init board:
        self.__board = []

        # init words:
        self.__words = []

        # init curr path:
        self.__curr_path = []
        self.__curr_word_label = []

        # init score:
        self.__score = 0

        # init correct words:
        self.__correct_words = []

        self.__gui.root.mainloop()

    def __start_game(self):
        self.__init_board()
        self.__gui.init_game(self.__board,
                             on_guess=self._handle_guess,
                             on_reset=self.___reset_selection,
                             on_selection=self.__handle_cell_selection,)
        self.__init_words()

    def __init_board(self):
        self.__board = randomize_board()

    def __init_words(self):
        """saves words from ./boggle_dict.txt file in __words list
        """
        self.__words = get_words('./boggle_dict.txt')

    def __update_path_label(self):
        """update screen's current words path text
        """
        self.__gui.update_curr_path_label("".join(self.__curr_word_label))

    def __update_score(self):
        self.__gui.update_score_label(self.__score)

    def __handle_cell_selection(self, cell_value, i, j):
        selected_loc = (i, j)
        if selected_loc in self.__curr_path:
            # unselect cell:
            # todo check that path will be valid
            self.__curr_path.remove(selected_loc)  # update path
            self.__curr_word_label.remove(cell_value)  # update label
            self.__gui.update_board(selected_loc, False)
        else:
            if len(self.__curr_path) == 0 or _is_my_neighbor(selected_loc, self.__curr_path[-1]):
                self.__curr_path.append(selected_loc)  # update path
                self.__curr_word_label.append(cell_value)  # update label
                self.__gui.update_board(selected_loc, True)
            else:
                print("not good")
                self.__gui.set_err_msg("not neighbor")
                return
        self.__update_path_label()

    def _handle_guess(self):
        word = is_valid_path(self.__board, self.__curr_path, self.__words)
        if not word:
            self.__gui.set_err_msg("not a valid word, sorry (:")
        else:
            # found valid word:
            if self.__curr_word_label in self.__correct_words:
                self.__gui.set_err_msg("you correctly guessed this word already")
                return

            # update correct words:
            self.__correct_words.append(self.__curr_word_label)
            self.__gui.add_word_to_list("".join(self.__curr_word_label))

            # change & update score
            self.__score += calc_score(self.__curr_path)  # change score
            self.__update_score()

            self.___reset_selection()

    def ___reset_selection(self):

        for loc in self.__curr_path:  # change board
            self.__gui.update_board(loc, False)

        self.__curr_path = []  # change path
        self.__curr_word_label = []  # change word
        self.__update_path_label()


if __name__ == "__main__":
    Boggle()
