import tkinter as tk
from tkinter.constants import LEFT, RIGHT, TOP


class HomePageGUI:

    def __init__(self, root, bg_color):
        HomePageGUI.BG_COLOR = bg_color
        self.root = root

        self.__scores_overview_container = tk.Frame(self.root, width=200)

        self.__title_fr = tk.Frame(self.__scores_overview_container, width=200)
        self.__title_name = tk.Label(self.__title_fr, text="NAME")
        self.__title_score = tk.Label(self.__title_fr, text="SCORE")

    def __add_start_btn(self, on_start_game):
        # play btn
        self.__start_game_btn = tk.Button(self.root,
                                          font=("", 50),
                                          text="Start",
                                          background="#616f9c",
                                          command=lambda: on_start_game()
                                          )
        self.__start_game_btn.pack(pady=(10, 0))

    def __remove_score_table(self):
        self.__start_game_btn.destroy()

    def add_home_page(self, on_start_game, is_launch=True, player_name=None, player_score=None):
        self.__add_start_btn(on_start_game)

        if not is_launch:

            self.__scores_overview_container.pack(side=TOP)
            self.__title_fr.pack(side=TOP)
            self.__title_name.pack(side=LEFT, expand=True)
            self.__title_score.pack(side=RIGHT, expand=True)
            self.__add_new_player(player_name, player_score)

    def __add_new_player(self, name, score):
        player_fr = tk.Frame(self.__scores_overview_container, width=200)
        player_fr.pack(side=TOP)
        tk.Label(player_fr, text=name).pack(side=LEFT, expand=True)
        tk.Label(player_fr, text=score).pack(side=RIGHT, expand=True)

    def remove_home_page(self):
        self.__remove_score_table()
        self.__scores_overview_container.pack_forget()
