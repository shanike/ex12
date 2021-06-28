import tkinter as tk


class HomePageGUI:

    def __init__(self, root, bg_color):
        HomePageGUI.BG_COLOR = bg_color
        self.root = root

    def __add_start_btn(self, on_start_game):
        # play btn
        self.__start_game_btn = tk.Button(self.root,
                                          font=("", 50),
                                          text="Start",
                                          background="#49c7a8",
                                          command=lambda: on_start_game()
                                          )
        self.__start_game_btn.pack(pady=(10, 0))

    def __remove_score_table(self):
        self.__start_game_btn.destroy()

    def add_home_page(self, on_start_game):
        self.__add_start_btn(on_start_game)
    
    def remove_home_page(self):
        self.__remove_score_table()