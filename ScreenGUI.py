import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter.constants import BOTTOM, TOP

from SingleBoggleGameGUI import SingleBoggleGameGUI
from HomePageGUI import HomePageGUI

from boggle_utils import get_random_name


class ScreenGUI:
    """this class is in change of the screen root and of all widgets which will be rendered on the screen
    this class will "route" between the home page and the single game page
    """

    BG_COLOR = "#F8EDEB"

    def __init__(self, on_start_game, on_selection, on_guess, on_reset, on_time_up):
        self.__on_start_game = on_start_game

        self.root = None
        self.__init_root()

        self.__game_container = tk.Frame(self.root, background=ScreenGUI.BG_COLOR)
        self.__top_container = tk.Frame(self.root, background=ScreenGUI.BG_COLOR)
        self.__top_container.pack(side=TOP)
        # create background and static stuff:
        self.__init_top_widgets(self.__top_container)

        self.__home_page_container = tk.Frame(self.__top_container, background=ScreenGUI.BG_COLOR)
        self.__home_page_container.pack()
        self.HomePageGUI = HomePageGUI(self.__home_page_container, self.vh_func, self.vw_func, bg_color=ScreenGUI.BG_COLOR)
        self.HomePageGUI.add_home_page(self.__on_start_game)

        self.SingleBoggleGameGUI = SingleBoggleGameGUI(self.__game_container,
                                                       bg_color=ScreenGUI.BG_COLOR,
                                                       on_selection=on_selection,
                                                       on_reset=on_reset,
                                                       on_guess=on_guess,
                                                       on_time_up=on_time_up,
                                                       vh_func=self.vh_func,
                                                       vw_func=self.vw_func
                                                       )

    def __init_root(self):
        root = tk.Tk()
        root.wm_title("-- best game ever --")

        root.configure(background=ScreenGUI.BG_COLOR)
        self.w, self.h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root = root

    def __init_top_widgets(self, parent):
        title = tk.Label(parent,
                         font=("", 28, "bold"),
                         text="BOGGLE GAME! yay! ☺️",
                         background=ScreenGUI.BG_COLOR,
                         foreground='#1d3652',
                        )
        title.pack(side=tk.TOP, pady=(self.vh_func(4), self.vh_func(1)))

        slogen = tk.Label(parent,
                          font=("", 10,),
                          text="(:"+"תפזורת - אבל מותר לשנות כיוון במסלול "[::-1],
                          background=ScreenGUI.BG_COLOR,
                          foreground='#1d3652',
                        )
        slogen.pack()

        instructions = tk.Label(parent, 
                                font=("", 16, "italic"), 
                                text="find as many words as you can:", 
                                background=ScreenGUI.BG_COLOR,
                                foreground='#1d3652',
                            )
        instructions.pack(side=tk.TOP)

    def end_game(self, score):
        """
        handle game finished, bring home page back and remove single game 
        (with new player score)
        """
        self.SingleBoggleGameGUI.remove_single_game()
        self.__game_container.pack_forget()  # must be after remove_single_game()
        self.HomePageGUI.add_home_page(self.__on_start_game, is_launch=False,
                                       player_name=get_random_name(), player_score=score)
        self.__home_page_container.pack()

    def start_game(self, board):
        self.__game_container.pack(side=BOTTOM, expand=True)
        self.HomePageGUI.remove_home_page()
        self.__home_page_container.pack_forget()
        self.SingleBoggleGameGUI.add_single_game(board)

    def set_curr_path_label(self, text):
        self.SingleBoggleGameGUI.set_curr_path_label(text)

    def update_score_label(self, new_score):
        self.SingleBoggleGameGUI.set_score_label(new_score)

    def update_board(self, *args, **kwargs):
        self.SingleBoggleGameGUI.update_board(*args, **kwargs)

    def set_err_msg(self, text):
        messagebox.showerror("-- Error --", text)

    def add_word_to_list(self, word):
        self.SingleBoggleGameGUI.add_word_to_list(word)

    def vh_func(self, percent):
        """utils function for gui. converts height percent values to pxs

            :param percent: {int}

        Returns:
            int -- pxs
        """
        return int((percent * self.h) / 100)

    def vw_func(self, percent):
        """utils function for gui. converts width percent values to pxs

            :param percent: {int}

        Returns:
            int -- pxs
        """
        return int((percent * self.w) / 100)
