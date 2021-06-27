from tkinter import font
from ex12_utils import bind_values_to_func
import tkinter as tk
from tkinter import messagebox


class ScreenGUI:

    BG_COLOR = "lightblue"

    def __init__(self, on_start_game):

        self.root = None
        self.__init_root()

        # create background and static stuff:
        self.__static_widgets()

        # play btn
        self.__start_game_btn = tk.Button(self.root,
                  font=("", 50),
                  text="Start",
                  background="#49c7a8",
                  command=lambda: on_start_game()
                  )
        self.__start_game_btn.pack(pady=(10, 0))

        # score label:
        self.__score_label = None

        # current path on top label:
        self.__curr_word_label = None

        # init board location:
        self.__board_frame = None
        self.__board_buttons = {}
        self.__selected_cells = []

        # correct words list:
        self.__words_list_container = None

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

    def __remove_score_table(self):
        self.__start_game_btn.destroy()
        pass

    def init_game(self, board, on_selection, on_guess, on_reset):
        self.__remove_score_table()
        self.__init_board(board, on_selection)
        
        # score label:
        self.__score_label = tk.Label(self.root,
                                      font=("", 16), background=ScreenGUI.BG_COLOR,
                                      highlightbackground="blue", highlightthickness=2)
        self.__score_label.pack(pady=(10, 0))
        # current path on top label:
        self.__curr_word_label = tk.Label(self.root, font=("", 30), background="lightgrey", width=10,
                                          highlightbackground="brown", highlightthickness=1)
        self.__curr_word_label.pack(side=tk.TOP, pady=10)

        # guess button:
        tk.Button(self.root, text="CHECK", bg="yellow", command=on_guess).pack()

        # reset button:
        tk.Button(self.root, text="-RESET-", bg="#631166", command=on_reset).pack()

        # correct words list:
        self.__init_words_list_container()

    def __init_board(self, board, on_selection):
        self.__board_frame = tk.Frame(self.root, bd=5, relief="solid")
        self.__board_frame.grid_columnconfigure(0, weight=1)
        self.__board_frame.pack()
        self.__init_board_buttons(board, self.__board_frame, on_selection)

    def __init_words_list_container(self):
        self.__words_list_container = tk.Frame(self.root)
        self.__words_list_container.configure(bg=ScreenGUI.BG_COLOR, highlightthickness=1, highlightbackground="brown")
        self.__words_list_container.pack(side=tk.LEFT)

        words_list_title = tk.Label(self.__words_list_container, text="Correct words:", bg=ScreenGUI.BG_COLOR)
        words_list_title.pack()

    def update_curr_path_label(self, text):
        """ sets <text> to be displayed in label at the top of the screen (the word guessing label)
        :param text: {str} -- text to be displayed
        """
        self.__curr_word_label.configure(text=text)

    def update_score_label(self, new_score):
        self.__score_label.configure(text="score: " + str(new_score))

    def __init_board_buttons(self, board, board_container, on_selection):
        for i in range(len(board)):
            for j in range(len(board[i])):
                loc = (i, j)
                value = board[i][j]
                is_selected = loc in self.__selected_cells
                self.__board_buttons[loc] = tk.Button(board_container,
                                                      text=value,
                                                      font=("", 30),
                                                      bg="#db3545" if is_selected else "#4ec78a",
                                                      activebackground="#d9717c"if is_selected else "#90deb7",
                                                      command=bind_values_to_func(on_selection, value, i, j),
                                                      )

                self.__board_buttons[loc].grid_configure(columnspan=1, padx=5, pady=5)
                self.__board_buttons[loc].grid(row=i, column=j)

    def update_board(self, location, is_selected):
        self.__board_buttons[location].configure(
            bg="#db3545" if is_selected else "#4ec78a",
            activebackground="#d9717c"if is_selected else "#90deb7",)

    def set_err_msg(self, text):
        messagebox.showerror("Error", text)

    def add_word_to_list(self, word):
        word_label = tk.Label(self.__words_list_container,
                              font=("", 14), background=ScreenGUI.BG_COLOR,
                              text=word
                              )
        word_label.pack()
