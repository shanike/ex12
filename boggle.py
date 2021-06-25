from ex12_utils import _is_my_neighbor
from ScreenGUI import ScreenGUI
from boggle_board_randomizer import randomize_board
from pprint import pprint


class Boggle:
    def __init__(self):
        self.__screen = ScreenGUI()

        # set board:
        self.__board = []

        # set curr path:
        self.__curr_path = []
        self.__curr_path_label = []

        self.set_board()
        self.handle_display_board()

        self.start_game()

    def start_game(self):
        self.__screen.root.mainloop()

    def set_board(self):
        board_list = randomize_board()
        board_dict = []
        for row in board_list:
            board_dict.append([])
            for col in row:
                board_dict[-1].append({col: False})
        self.__board = board_dict

    def handle_display_board(self):
        self.__screen.display_board(self.__board, self.handle_cell_selection)

    def handle_cell_selection(self, cell_value, i, j):
        selected_loc = (i, j)
        if self.__board[i][j][cell_value]:
            # unselect cell:
            # todo check that path will be valid
            self.__board[i][j][cell_value] = False # update board
            self.__curr_path.remove(selected_loc) # update path
            self.__curr_path_label.remove(cell_value) # update label
            self.__screen.display_top_label("".join(self.__curr_path_label))
            self.handle_display_board()
        else:
            if len(self.__curr_path) == 0 or _is_my_neighbor(selected_loc, self.__curr_path[-1]):
                self.__board[i][j][cell_value] = True # update board
                self.__curr_path.append(selected_loc) # update path
                self.__curr_path_label.append(cell_value) # update label
                self.__screen.display_top_label("".join(self.__curr_path_label))
                self.handle_display_board()
            else:
                print("not good")
                self.__screen.set_err_msg("not neighbor")
        self.__screen.add_word_to_list('just for the fun of it')



if __name__ == "__main__":
    Boggle()
