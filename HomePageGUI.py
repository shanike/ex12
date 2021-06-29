import tkinter as tk
from tkinter.constants import END, LEFT, RIGHT, TOP


class HomePageGUI:

    START_BTN_TEXT = {"FIRST_LAUNCH": "START", "NOT_FIRST_LAUNCH": "ANOTHER!"}

    def __init__(self, root, bg_color):
        HomePageGUI.BG_COLOR = bg_color
        self.root = root

        self.__scores_overview_container = tk.Frame(self.root, width=200)

        self.__title_name = tk.Label(self.__scores_overview_container, width=20, fg='purple',
                                     font=('Arial', 16, 'bold'),
                                     text="NAME")

        self.__title_score = tk.Label(self.__scores_overview_container, width=20, fg='purple',
                                      font=('Arial', 16, 'bold'),
                                      text="SCORE")
        self.__scores_overview = []

    def add_home_page(self, on_start_game, is_launch=True, player_name=None, player_score=None):
        self.__add_start_btn(on_start_game,
                             text=HomePageGUI.START_BTN_TEXT['FIRST_LAUNCH'] if is_launch else HomePageGUI.START_BTN_TEXT['NOT_FIRST_LAUNCH'])

        if not is_launch:
            new_player = {"name": player_name if player_name else "Sam", "score": player_score if player_score else 0}
            self.__scores_overview.append(new_player)
            # show scores table
            self.__scores_overview_container.pack(side=TOP)
            self.__title_name.grid(row=1, column=1)
            # self.__title_name.insert(END, "NAME")
            self.__title_score.grid(row=1, column=2)
            # self.__title_score.insert(END, "SCORE")

            self.__show_scores()

    def __add_start_btn(self, on_start_game, text):
        # play btn
        self.__start_game_btn = tk.Button(self.root,
                                          font=("", 50),
                                          text=text,
                                          background="#616f9c",
                                          command=lambda: on_start_game()
                                          )
        self.__start_game_btn.pack(pady=(10, 0))

    def __show_scores(self):
        row_cnt = 2  # first row is title
        for i in range(len(self.__scores_overview) - 1, -1, -1):  # reverse display
            player = self.__scores_overview[i]
            tk.Label(self.__scores_overview_container,
                     width=20, fg='blue',
                     font=('Arial', 16, 'bold'),
                     text=player["name"]
                     ).grid(row=row_cnt, column=1)
            tk.Label(self.__scores_overview_container, width=20, fg='blue',
                     font=('Arial', 16, 'bold'),
                     text=player["score"]
                     ).grid(row=row_cnt, column=2)
            row_cnt += 1

    def __remove_score_table(self):
        self.__start_game_btn.destroy()  # initializes (.pack()) on every start of game
        self.__title_name.grid_forget()
        self.__title_score.grid_forget()

    def remove_home_page(self):
        self.__remove_score_table()
        for item in self.__scores_overview_container.grid_slaves():
            item.grid_forget()
        self.__scores_overview_container.pack_forget()
