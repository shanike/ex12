from ex12_utils import _is_my_neighbor, get_words, is_valid_path
from boggle_utils import calc_score
from ScreenGUI import ScreenGUI
from boggle_board_randomizer import randomize_board


class Boggle:
    def __init__(self):
        self.__gui = ScreenGUI(on_start_game=self.__start_game,
                               on_guess=self.__handle_guess,
                               on_reset=self.___reset_selection,
                               on_selection=self.__handle_cell_selection,
                               on_time_up=self.__handle_time_up)

        # init board:
        self.__board = []

        # init words:
        self.__words = []

        # init curr path:
        self.__curr_path = []
        self.__curr_word_label = []
        self.__curr_word = []

        # init score:
        self.__score = 0

        # init correct words:
        self.__correct_words = []

        self.__gui.root.mainloop()

    def __start_game(self):
        self.__init_board()
        self.__gui.start_game(self.__board)
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
        self.__gui.set_curr_path_label("".join(self.__curr_word_label))

    def __update_score(self):
        self.__gui.update_score_label(self.__score)

    def __handle_cell_selection(self, cell_value, selected_loc):
        """function to be called when user presses on a cell in boggle board
        available cells to click are only cells which are:
        neighbors of last selected cell, or the last selected cell itself
        
        :param cell_value: {str} -- letter(s) value
        :param i: {int} -- row location
        :param j: {int} -- column location
        """
        if selected_loc in self.__curr_path:
            if selected_loc != self.__curr_path[-1]:
                return
            # unselect last cell (current cell)
            self.__curr_path.pop()  # update path
            self.__curr_word_label.pop()  # update label
            self.__gui.update_board(selected_loc, False,
                                    prev_loc=None if len(self.__curr_path) < 1 else self.__curr_path[-1],
                                    prev_loc_is_first=True
                                    )
            self.__update_path_label()
            return

        if not len(self.__curr_path) or _is_my_neighbor(selected_loc, self.__curr_path[-1]):
            # if no length in self.__curr_path, or is_my_neighbor and can select
            self.__curr_path.append(selected_loc)  # update path
            self.__curr_word_label.append(cell_value)  # update label
            self.__gui.update_board(selected_loc, True,
                                    prev_loc=None if len(self.__curr_path) < 2 else self.__curr_path[-2],  # second last
                                    prev_loc_is_first=False  # to turn back to regular bg-color
                                    )
            self.__update_path_label()

    def __handle_guess(self):
        word = is_valid_path(self.__board, self.__curr_path, self.__words)
        if not word:
            self.___reset_selection()
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

            # reset board
            self.___reset_selection()

    def ___reset_selection(self):

        for loc in self.__curr_path:  # change board
            self.__gui.update_board(loc, False)

        self.__curr_path = []  # change path
        self.__curr_word_label = []  # change word
        self.__update_path_label()

    def __handle_time_up(self):
        """
        game over, reset all variables and call home page
        """
        self.__gui.end_game(self.__score)

        # reset board:
        self.__board = []

        # reset words:
        self.__words = []

        # reset curr path:
        self.__curr_path = []
        self.__curr_word_label = []
        self.__correct_paths = []

        # reset score:
        self.__score = 0

        # reset correct words:
        self.__correct_words = []


if __name__ == "__main__":
    Boggle()
