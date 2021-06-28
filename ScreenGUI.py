import tkinter as tk
from tkinter import messagebox

from SingleBoggleGameGUI import SingleBoggleGameGUI
from HomePageGUI import HomePageGUI

from ex12_utils import bind_values_to_func


class ScreenGUI:
    """this class is in change of the screen root and of all widgets which will be rendered on the screen
    this class will "route" between the home page and the single game page
    """

    BG_COLOR = "lightblue"

    def __init__(self, on_start_game ,on_selection, on_guess, on_reset):
        self.__on_start_game = on_start_game
        self.root = None
        self.__init_root()

        # create background and static stuff:
        self.__static_widgets()

        self.HomePageGUI = HomePageGUI(self.root, bg_color=ScreenGUI.BG_COLOR)
        self.HomePageGUI.add_home_page(self.__on_start_game)

        self.SingleBoggleGameGUI = SingleBoggleGameGUI(
            self.root, bg_color=ScreenGUI.BG_COLOR, on_selection=on_selection, on_reset=on_reset, on_guess=on_guess)

    def __init_root(self):
        root = tk.Tk()
        root.wm_title("-- best game ever --")

        root.configure(background=ScreenGUI.BG_COLOR)
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w / 2, h))
        self.root = root

    def __static_widgets(self):
        title = tk.Label(self.root, font=("", 20), text="BOGGLE GAME! YAY", background=ScreenGUI.BG_COLOR)
        title.pack(side=tk.TOP, pady=10)

        instructions = tk.Label(self.root, font=(
            "", 16), text="find as many words as you can:", background=ScreenGUI.BG_COLOR)
        instructions.pack(side=tk.TOP)

    def start_game(self, board):
        self.HomePageGUI.remove_home_page()
        self.SingleBoggleGameGUI.add_single_game(board)

    def set_curr_path_label(self, text):
        self.SingleBoggleGameGUI.set_curr_path_label(text)

    def update_score_label(self, new_score):
        self.SingleBoggleGameGUI.update_score_label(new_score)

    def update_board(self, *args, **kwargs):
        self.SingleBoggleGameGUI.update_board(*args, **kwargs)

    def set_err_msg(self, text):
        messagebox.showerror("-- Error --", text)

    def add_word_to_list(self, word):
        self.SingleBoggleGameGUI.add_word_to_list(word)
