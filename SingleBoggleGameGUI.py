import tkinter as tk
from tkinter import RIGHT
from BorderRadius import RoundedButton
from ex12_utils import bind_values_to_func
from timer import Timer


class SingleBoggleGameGUI:

    UNSELECTED = "#89b0ae"
    UNSELECTED_HOVER = "#b4dbd9"

    SELECTED = "#D7C49E"
    SELECTED_HOVER = "#C7D3D4"

    FIRST = "#195190"
    FIRST_HOVER = "#7b9acc"

    def __init__(self, root, bg_color, on_selection, on_reset, on_guess, on_time_up, vh, vw):
        """
            :param on_selection: {func} -- function to be called when user selects a cell on board. 
            the function will get the value and the location of the selected cell

        """
        SingleBoggleGameGUI.BG_COLOR = bg_color

        self.vh, self.vw = vh, vw
        self.__on_selection = on_selection
        self.__on_reset = on_reset
        self.__on_guess = on_guess

        self.root = root

        # init the timer
        self.__timer = Timer(self.root, 3, on_time_up)

        # score label:

        self.__score_label = tk.Label(self.root,
                                      font=("", 16), background=SingleBoggleGameGUI.BG_COLOR,
                                      highlightbackground="blue", highlightthickness=2)
        # current path on top label:
        self.__curr_word_label = tk.Label(self.root, font=("", 30), background="lightgrey", width=10,
                                          highlightbackground="brown", highlightthickness=1)

        # init board location:
        self.__board_frame = tk.Frame(self.root, background=SingleBoggleGameGUI.BG_COLOR)
        self.__board_frame.grid_columnconfigure(0, weight=1)

        self.__board_buttons = {}

        # check button
        self.__check_img = tk.PhotoImage(file="check.png")
        self.__check_img = self.__check_img.subsample(20)
        self.__check_btn = tk.Button(self.root,
                                     image=self.__check_img,
                                     borderwidth=0,
                                     text='submit',
                                    #  bc='pink',
                                     highlightbackground=SingleBoggleGameGUI.BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.BG_COLOR,
                                     bg=SingleBoggleGameGUI.BG_COLOR,
                                     command=self.__on_guess
                                     )
        # reset button
        self.__reset_btn = tk.Button(self.root,
                                     image=tk.PhotoImage(file="reset.png"),
                                     borderwidth=0,
                                     highlightbackground=SingleBoggleGameGUI.BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.BG_COLOR,
                                     bg=SingleBoggleGameGUI.BG_COLOR,
                                     command=self.__on_reset,
                                     )

        # correct words list:
        self.__words_list_container = tk.Frame(self.root,
                                               bg=SingleBoggleGameGUI.BG_COLOR,
                                               highlightthickness=1, highlightbackground="brown")
        self.locations_to_reset = []

    def add_single_game(self, board):
        """adds all relevant widgets for a single boggle game
            :param board: {[[str]]} -- 2d letter(s) board for boggle game
        """

        self.__init_board(board)

        # score label:
        self.__score_label.pack(pady=(10, 0))

        # current path on top label:
        self.__curr_word_label.pack(side=tk.TOP, pady=10)

        # guess button:

        self.__check_btn.pack(side=RIGHT, padx=15, pady=20)

        # reset button:
        self.__reset_btn.pack()

        # correct words list:
        self.__init_words_list_container()

        # start the timer
        self.__timer.set_timer()

    def __init_board(self, board):
        self.board = board
        self.__board_frame.pack()
        self.__init_board_buttons()

    def __init_board_buttons(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                loc = (i, j)
                value = self.board[i][j]
                self.__board_buttons[loc] = RoundedButton(parent=self.__board_frame,
                                                          width=self.vh(10),
                                                          height=self.vw(4),
                                                          cornerradius=6,
                                                          padding=2,
                                                          color=SingleBoggleGameGUI.UNSELECTED,
                                                          active_color=SingleBoggleGameGUI.UNSELECTED_HOVER,
                                                          bg=SingleBoggleGameGUI.BG_COLOR,
                                                          text_color="white",
                                                          text=value,
                                                          command=bind_values_to_func(self.__on_selection, value, (i, j)), )

                # self.__board_buttons[loc].grid_configure(columnspan=1, padx=5, pady=5)
                self.__board_buttons[loc].grid(row=i, column=j, pady=10, padx=10)

    def __init_words_list_container(self):
        self.__words_list_container.pack(side=tk.LEFT)

        words_list_title = tk.Label(self.__words_list_container, text="Correct words:", bg=SingleBoggleGameGUI.BG_COLOR)
        words_list_title.pack()

    def update_board(self, location, is_selected, prev_loc, prev_loc_is_first):
        self.__board_buttons[location] = RoundedButton(parent=self.__board_frame,
                                                       width=100,
                                                       height=100,
                                                       cornerradius=6,
                                                       padding=2,
                                                       color=SingleBoggleGameGUI.FIRST if is_selected else SingleBoggleGameGUI.UNSELECTED,
                                                       active_color=SingleBoggleGameGUI.FIRST_HOVER if is_selected else SingleBoggleGameGUI.UNSELECTED_HOVER,
                                                       bg=SingleBoggleGameGUI.BG_COLOR,
                                                       text_color="white",
                                                       text=self.board[location[0]][location[1]],
                                                       command=bind_values_to_func(
                                                           self.__on_selection, self.board[location[0]][location[1]], location)
                                                       )
        self.__board_buttons[location].grid(row=location[0], column=location[1], pady=10, padx=10)

        if prev_loc:  # reset color of prev selected button
            self.__board_buttons[prev_loc] = RoundedButton(parent=self.__board_frame,
                                                           width=100,
                                                           height=100,
                                                           cornerradius=6,
                                                           padding=2,
                                                           color=SingleBoggleGameGUI.FIRST if prev_loc_is_first else SingleBoggleGameGUI.SELECTED,
                                                           active_color=SingleBoggleGameGUI.FIRST_HOVER if prev_loc_is_first else SingleBoggleGameGUI.SELECTED_HOVER,
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

    def update_score_label(self, new_score):
        self.__score_label.configure(text="score: " + str(new_score))

    def add_word_to_list(self, word):
        tk.Label(self.__words_list_container,
                 font=("", 14), background=SingleBoggleGameGUI.BG_COLOR,
                 text=word
                 ).pack()

    def remove_single_game(self):
        self.__timer.remove_timer()
        self.__score_label.pack_forget()
        self.set_curr_path_label("")  # reset
        self.__curr_word_label.pack_forget()
        self.__board_frame.pack_forget()
        self.__check_btn.pack_forget()
        self.__reset_btn.pack_forget()
        self.__words_list_container.pack_forget()
        for btn in self.__board_buttons:
            self.__board_buttons[btn].grid_remove()
        self.__board_buttons = {}
