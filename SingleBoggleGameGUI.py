import tkinter as tk
from tkinter import RIGHT
from tkinter.constants import BOTTOM, LEFT, N, NE, TOP, TRUE
from RoundedButton import RoundedButton
from boggle_utils import bind_values_to_func
from timer import Timer


class SingleBoggleGameGUI:

    CELL_COLORS = {
        "UNSELECTED": "#89b0ae",
        "UNSELECTED_HOVER": "#b4dbd9",

        "SELECTED": "#7b9acc",
        "SELECTED_HOVER": "#7b9acc",

        "HEAD": "#195190",
        "HEAD_HOVER": "#5294e0",
    }
    LEFT_BG_COLOR = "#195190"
    RIGHT_BG_COLOR = "#195190"
    TIMER_SEC = 180

    def __init__(self, parent, bg_color, on_selection, on_reset, on_guess, on_time_up, vh_func, vw_func):
        """
            :param bg_color: {str} -- hex color of screen's background color
            :param on_selection: {func} -- function to be called when user selects a cell on board.
            the function will get the value and the location of the selected cell
            :param on_reset: {func} -- function to be called when user clicks the reset button.
            :param on_guess: {func} -- function to be called when user clicks the check button.
            :param on_time_up: {func} -- function to be called when time is up, and game is supposed to be over.
            :param vh_func: {func} -- convert hight percents to numbers that can be used for Tk (px?)
            :param vw_func: {func} -- convert width percents to numbers that can be used for Tk (px?)
        """
        SingleBoggleGameGUI.BG_COLOR = bg_color

        self.vh_func, self.vw_func = vh_func, vw_func
        self.__cube_width = self.vw_func(5)
        self.__cube_height = self.vh_func(8)
        self.__on_selection = on_selection
        self.__on_reset = on_reset
        self.__on_guess = on_guess

        self.__parent = parent

        #: right side:
        self.__right_side_fr = tk.Frame(
            self.__parent, background=SingleBoggleGameGUI.BG_COLOR)
        # check button
        self.__check_btn = tk.Button(self.__right_side_fr,
                                     borderwidth=0,
                                     text='submit',
                                     font=("", 22, "bold"),
                                     highlightbackground=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     background=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     foreground="white",
                                     activeforeground="white",
                                     command=self.__on_guess
                                     )
        # reset button
        self.__reset_btn = tk.Button(self.__right_side_fr,
                                     borderwidth=0,
                                     text='reset',
                                     font=("", 22, "bold"),
                                     highlightbackground=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     background=SingleBoggleGameGUI.RIGHT_BG_COLOR,
                                     foreground="white",
                                     activeforeground="white",
                                     command=self.__on_reset,
                                     )
        #: center:
        self.__center_fr = tk.Frame(self.__parent, background=SingleBoggleGameGUI.BG_COLOR, width=self.vw_func(50))
        # create timer obj:
        self.__timer_container = tk.Frame(self.__center_fr, background="green")
        self.__timer = Timer(self.__timer_container, SingleBoggleGameGUI.TIMER_SEC, on_time_up)
        # init board location:
        self.__board_frame = tk.Frame(self.__center_fr, background=SingleBoggleGameGUI.BG_COLOR)
        self.__board_frame.grid_columnconfigure(0, weight=1)
        # current path label:
        self.__curr_word_label = tk.Label(self.__center_fr, font=("", 30), background="lightgrey", width=10)
        self.__board_buttons = {}

        #: left side:
        self.__left_side_fr = tk.Frame(self.__parent,
                                       background=SingleBoggleGameGUI.LEFT_BG_COLOR, width=self.vw_func(25))
        # score label:
        self.__score_label = tk.Label(self.__left_side_fr,
                                      font=("", 22, "bold"), background=SingleBoggleGameGUI.LEFT_BG_COLOR, foreground="white",
                                      text="score: 0")
        # correct words list:
        self.__words_list_container = tk.Frame(self.__left_side_fr,
                                               background=SingleBoggleGameGUI.LEFT_BG_COLOR,)

    def add_single_game(self, board):
        """adds all relevant widgets for a single boggle game
            :param board: {[[str]]} -- 2d letter(s) board for boggle game
        """

        #: init right side:
        self.__init_right_side()
        #: init center:
        self.__init_center(board)
        #: init left side:
        self.__init_left_side()

    def __init_right_side(self):
        self.__right_side_fr.grid(padx=(100), column=5, row=1)
        # guess button:
        self.__check_btn.pack(side=TOP, pady=(10))
        # reset button:
        self.__reset_btn.pack(side=BOTTOM)

    def __init_center(self, board):
        self.__center_fr.grid(padx=(100), column=2, row=1, columnspan=3)

        # start the timer
        self.__timer_container.pack(side=TOP)
        self.__timer.init_timer()
        # board
        self.__init_board(board)
        # current path on top label:
        self.__curr_word_label.pack(side=tk.TOP, pady=10)

    def __init_left_side(self):
        self.__left_side_fr.grid(padx=(100), column=1, row=1)
        # score label:
        self.__score_label.pack(side=TOP)
        # correct words list:
        self.__init_words_list_container()

    def __init_board(self, board):
        """renders board Frame and calls init board buttons
        """
        self.board = board
        self.__board_frame.pack(side=TOP, anchor=N)
        self.__init_board_buttons()

    def __init_board_buttons(self):
        """renders board buttons inside board Frame
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                loc = (i, j)
                value = self.board[i][j]
                self.__board_buttons[loc] = RoundedButton(parent=self.__board_frame,
                                                          width=self.__cube_width,
                                                          height=self.__cube_height,
                                                          cornerradius=6,
                                                          padding=2,
                                                          color=SingleBoggleGameGUI.CELL_COLORS["UNSELECTED"],
                                                          active_color=SingleBoggleGameGUI.CELL_COLORS["UNSELECTED_HOVER"],
                                                          bg=SingleBoggleGameGUI.BG_COLOR,
                                                          text_color="white",
                                                          text=value,
                                                          command=bind_values_to_func(self.__on_selection, value, (i, j)), )

                # self.__board_buttons[loc].grid_configure(columnspan=1, padx=5, pady=5)
                self.__board_buttons[loc].grid(row=i, column=j, pady=10, padx=10)

    def __init_words_list_container(self):
        """renders correct words list Frame
        """
        self.__words_list_container.pack(side=TOP, pady=(30, 0), expand=True)

        words_list_title = tk.Label(self.__words_list_container,
                                    font=("", 16),
                                    text="Correct words:",
                                    background=SingleBoggleGameGUI.LEFT_BG_COLOR,
                                    foreground="white"
                                    )
        words_list_title.pack()

    def update_board(self, location, is_selected, prev_loc=None, prev_loc_is_first=None):
        """update single cell on board (and if provided, update previous cell, the one on the user's path before <location>)

            :param location: {tuple} -- location of cell to update
            :param is_selected: {bool} -- whether to color the cell with the "head cell" color or the unselected colors

        Keyword Arguments:
            prev_loc {tuple} -- previous location on user's path, if needs to be updated as well (specifically the color of the cell) (default: {None})
            prev_loc_is_first {bool} -- whether to color the previous cell with the selected color, or the "head cell" color (default: {None})
        """
        self.__board_buttons[location] = RoundedButton(parent=self.__board_frame,
                                                       width=self.__cube_width,
                                                       height=self.__cube_height,
                                                       cornerradius=6,
                                                       padding=2,
                                                       color=SingleBoggleGameGUI.CELL_COLORS["HEAD"] if is_selected else SingleBoggleGameGUI.CELL_COLORS["UNSELECTED"],
                                                       active_color=SingleBoggleGameGUI.CELL_COLORS[
                                                           "HEAD_HOVER"] if is_selected else SingleBoggleGameGUI.CELL_COLORS["UNSELECTED_HOVER"],
                                                       bg=SingleBoggleGameGUI.BG_COLOR,
                                                       text_color="white",
                                                       text=self.board[location[0]][location[1]],
                                                       command=bind_values_to_func(
                                                           self.__on_selection, self.board[location[0]][location[1]], location)
                                                       )
        self.__board_buttons[location].grid(row=location[0], column=location[1], pady=10, padx=10)

        if prev_loc:  # reset color of prev selected button
            self.__board_buttons[prev_loc] = RoundedButton(parent=self.__board_frame,
                                                           width=self.__cube_width,
                                                           height=self.__cube_height,
                                                           cornerradius=6,
                                                           padding=2,
                                                           color=SingleBoggleGameGUI.CELL_COLORS[
                                                               "HEAD"] if prev_loc_is_first else SingleBoggleGameGUI.CELL_COLORS["SELECTED"],
                                                           active_color=SingleBoggleGameGUI.CELL_COLORS[
                                                               "HEAD_HOVER"] if prev_loc_is_first else SingleBoggleGameGUI.CELL_COLORS["SELECTED_HOVER"],
                                                           bg=SingleBoggleGameGUI.BG_COLOR,
                                                           text_color="white",
                                                           text=self.board[prev_loc[0]][prev_loc[1]],
                                                           command=bind_values_to_func(
                                                               self.__on_selection, self.board[prev_loc[0]][prev_loc[1]], prev_loc)
                                                           )
            self.__board_buttons[prev_loc].grid(row=prev_loc[0], column=prev_loc[1], pady=10, padx=10)

    def set_curr_path_label(self, text):
        """ sets <text> to be displayed in label at the top of the screen (the word guessing label)
        :param text: {str} -- text to be displayed
        """
        self.__curr_word_label.configure(text=text)

    def set_score_label(self, new_score):
        """sets the score text in the score_label

            :param new_score: {int} -- user's score
        """
        self.__score_label.configure(text="score: " + str(new_score))

    def add_word_to_list(self, word):
        """adds a word to the words_list_container Frame

            :param word: {str} -- word to add
        """
        tk.Label(self.__words_list_container,
                 font=("", 14), background=SingleBoggleGameGUI.LEFT_BG_COLOR, foreground="white",
                 text=word
                 ).pack()

    def remove_single_game(self):
        """removes all widgets to do with the single game
        """
        self.__timer.remove_timer()
        self.set_score_label("")  # reset
        self.__score_label.pack_forget()
        self.set_curr_path_label("")  # reset
        self.__curr_word_label.pack_forget()
        self.__board_frame.pack_forget()
        self.__check_btn.pack_forget()
        self.__reset_btn.pack_forget()
        for word in self.__words_list_container.pack_slaves():
            word.pack_forget()
        self.__words_list_container.pack_forget()
        for btn in self.__board_buttons:
            self.__board_buttons[btn].grid_remove()
        self.__board_buttons = {}

        for left_elem in self.__left_side_fr.slaves():
            left_elem.pack_forget()
        for right_elem in self.__right_side_fr.slaves():
            right_elem.pack_forget()
        for center_item in self.__center_fr.slaves():
            center_item.pack_forget()
        self.__left_side_fr.grid_forget()
        self.__right_side_fr.grid_forget()
        self.__center_fr.grid_forget()
