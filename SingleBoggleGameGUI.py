import tkinter as tk

from BorderRadius import RoundedButton

from ex12_utils import bind_values_to_func


class SingleBoggleGameGUI():

    def __init__(self, root, bg_color, on_selection, on_reset, on_guess):
        SingleBoggleGameGUI.BG_COLOR = bg_color

        self.__on_selection = on_selection
        self.__on_reset = on_reset
        self.__on_guess = on_guess

        self.root = root

        # score label:
        self.__score_label = tk.Label(self.root,
                                      font=("", 16), background=SingleBoggleGameGUI.BG_COLOR,
                                      highlightbackground="blue", highlightthickness=2)
        # current path on top label:
        self.__curr_word_label = tk.Label(self.root, font=("", 30), background="lightgrey", width=10,
                                          highlightbackground="brown", highlightthickness=1)

        # init board location:
        self.__board_frame = tk.Frame(self.root, bd=5, relief="solid")
        self.__board_frame.grid_columnconfigure(0, weight=1)

        self.__board_buttons = {}
        self.__selected_cells = []

        # check button
        # self.__check_img = tk.PhotoImage(file="check.png")
        # self.__check_img = self.__check_img.subsample(20)
        self.__check_btn = tk.Button(self.root,
                                     #  image=self.__check_img,
                                     borderwidth=0,
                                     highlightbackground=SingleBoggleGameGUI.BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.BG_COLOR,
                                     bg=SingleBoggleGameGUI.BG_COLOR,
                                     command=self.__on_guess)
        # reset button
        self.__reset_btn = tk.Button(self.root,
                                    #  image=tk.PhotoImage(file="reset.png"),
                                     command=on_reset,
                                     borderwidth=0,
                                     highlightbackground=SingleBoggleGameGUI.BG_COLOR,
                                     activebackground=SingleBoggleGameGUI.BG_COLOR,
                                     bg=SingleBoggleGameGUI.BG_COLOR)

        # correct words list:
        self.__words_list_container = tk.Frame(self.root,
                                               bg=SingleBoggleGameGUI.BG_COLOR,
                                               highlightthickness=1, highlightbackground="brown")

    def add_single_game(self, board):
        """adds all relevant widgets for a single boggle game

            :param board: {[[str]]} -- 2d letter(s) board for boggle game
            :param on_selection: {func} -- function to be called when user selects a cell on board. 
            the function will get the value and the location of the selected cell
        """

        self.__init_board(board)

        # score label:
        self.__score_label.pack(pady=(10, 0))

        # current path on top label:
        self.__curr_word_label.pack(side=tk.TOP, pady=10)

        # guess button:

        self.__check_btn.pack()

        # reset button:
        self.__reset_btn.pack()

        # correct words list:
        self.__init_words_list_container()

    def __init_board(self, board):

        self.__board_frame.pack()
        self.__init_board_buttons(board, self.__board_frame)

    def __init_board_buttons(self, board, board_container):
        for i in range(len(board)):
            for j in range(len(board[i])):
                loc = (i, j)
                value = board[i][j]
                is_selected = loc in self.__selected_cells
                self.__board_buttons[loc] = RoundedButton(parent=self.__board_frame,
                                                          width=100,
                                                          height=100,
                                                          cornerradius=6,
                                                          padding=2,
                                                          color="#ffd6ba" if is_selected else "#89b0ae",
                                                          active_color="#ffe7d6"if is_selected else "#b4dbd9",
                                                          bg=SingleBoggleGameGUI.BG_COLOR,
                                                          text_color="white",
                                                          text=value,
                                                          command=bind_values_to_func(self.__on_selection, value, i, j), )

                # self.__board_buttons[loc].grid_configure(columnspan=1, padx=5, pady=5)
                self.__board_buttons[loc].grid(row=i, column=j, pady=10, padx=10)

    def __init_words_list_container(self):
        self.__words_list_container.pack(side=tk.LEFT)

        words_list_title = tk.Label(self.__words_list_container, text="Correct words:", bg=SingleBoggleGameGUI.BG_COLOR)
        words_list_title.pack()

    def update_board(self, location, is_selected):
        self.__board_buttons[location].configure(
            bg="#db3545" if is_selected else "#4ec78a",
            activebackground="#d9717c"if is_selected else "#90deb7",)

    def set_curr_path_label(self, text):
        """ sets <text> to be displayed in label at the top of the screen (the word guessing label)
        :param text: {str} -- text to be displayed
        """
        self.__curr_word_label.configure(text=text)

    def update_score_label(self, new_score):
        self.__score_label.configure(text="score: " + str(new_score))

    def add_word_to_list(self, word):
        word_label = tk.Label(self.__words_list_container,
                              font=("", 14), background=SingleBoggleGameGUI.BG_COLOR,
                              text=word
                              )
        word_label.pack()
