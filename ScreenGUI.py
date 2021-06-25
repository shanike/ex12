from tkinter import font
from ex12_utils import bind_values_to_func
import tkinter as tk
from tkinter import messagebox


class ScreenGUI:

    BG_COLOR = "lightblue"

    def __init__(self, on_guess, on_reset):

        self.root = None
        self.init_root()

        # create background and static stuff:
        self.static_widgets()

        # score label:
        self.__score_label = tk.Label(self.root)
        self.__score_label.configure(font=("", 16), background=ScreenGUI.BG_COLOR,
                                     highlightbackground="blue", highlightthickness=2)
        self.__score_label.pack(pady=(10, 0))

        # current path on top label:
        self._curr_path_label = tk.Label(self.root)
        self._curr_path_label.configure(font=("", 30), background="lightgrey", width=10,
                                        highlightbackground="brown", highlightthickness=1)
        self._curr_path_label.pack(side=tk.TOP, pady=10)

        # guess button:
        tk.Button(self.root, text="CHECK", bg="yellow", command=on_guess).pack()

        # reset button:
        tk.Button(self.root, text="-RESET-", bg="#631166", command=on_reset).pack()

        # init board location:
        self.__board_frame = None
        self.__init_board_frame(self.root)

        # correct words list:
        self.__words_list_container = None
        self.__init_words_list_container()

    def init_root(self):
        root = tk.Tk()
        root.wm_title("-- best game ever --")

        root.configure(background=ScreenGUI.BG_COLOR)
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.geometry("%dx%d+0+0" % (w / 2, h))
        self.root = root

    def static_widgets(self):
        title = tk.Label(self.root, font=("", 20), text="BOGGLE GAME! YAY", background=ScreenGUI.BG_COLOR)
        title.pack(side=tk.TOP, pady=10)

        instructions = tk.Label(self.root, font=(
            "", 16), text="find as many words as you can:", background=ScreenGUI.BG_COLOR)
        instructions.pack(side=tk.TOP)

    def __init_board_frame(self, parent):
        self.__board_frame = tk.Frame(parent, bd=5, relief="solid")
        self.__board_frame.grid_columnconfigure(0, weight=1)
        self.__board_frame.pack()

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
        self._curr_path_label.configure(text=text)

    def update_score_label(self, new_score):
        self.__score_label.configure(text="score: " + str(new_score))

    def display_board(self, board, on_selection):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                value, is_selected = list(cell.items())[0]
                cell_btn = tk.Button(self.__board_frame,
                                     text=value,
                                     command=bind_values_to_func(on_selection, value, i, j),
                                     font=("", 30),
                                     bg="#db3545" if is_selected else "#4ec78a",  # todo, colors to constants(!)
                                     activebackground="#e09fa6"if is_selected else "#c5edd9",
                                     )

                cell_btn.grid(row=i, column=j)
                cell_btn.grid_configure(columnspan=1, padx=5, pady=5)

    def set_err_msg(self, text):
        messagebox.showerror("Error", text)

    def add_word_to_list(self, word):
        word_label = tk.Label(self.__words_list_container,
                              font=("", 14), background=ScreenGUI.BG_COLOR,
                              text=word
                              )
        word_label.pack()
