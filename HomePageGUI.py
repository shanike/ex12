from boggle_utils import get_random_name
import tkinter as tk
from tkinter.constants import BOTTOM, END, LEFT, RIGHT, TOP
from RoundedButton import RoundedButton


class HomePageGUI:

    START_BTN_TEXT = {"FIRST_LAUNCH": "START", "NOT_FIRST_LAUNCH": "ANOTHER!"}

    SCORES_TABLE_BG = "#ECE4DB"

    def __init__(self, parent, vh_func, vw_func, bg_color):
        HomePageGUI.BG_COLOR = bg_color
        self.vh_func, self.vw_func = vh_func, vw_func
        self.score_width = self.vw_func(1.2)
        self.circle_w_and_h = self.vw_func(7.5)
        self.__parent = parent


        self.__score_table_title = tk.Label(self.__parent,
                                            text="Previous Scores:",
                                            font=('', 22),
                                            background=HomePageGUI.BG_COLOR,
                                            foreground='#091c33',
                                            )
        self.__scores_table_fr = tk.Frame(self.__parent,)
        self.__score_tablehead_name = tk.Label(self.__scores_table_fr, width=self.score_width, fg='#1d3652',
                                               font=('Arial', 16, 'bold'),
                                               text="NAME",
                                               background=HomePageGUI.SCORES_TABLE_BG,
                                               foreground="#7a71a8",
                                               )

        self.__score_tablehead_score = tk.Label(self.__scores_table_fr, width=self.score_width, fg='#1d3652',
                                                font=('Arial', 16, 'bold'),
                                                text="SCORE",
                                                background=HomePageGUI.SCORES_TABLE_BG,
                                                foreground="#7a71a8",
                                            )
        self.__scores_overview = []

        self.__start_game_btn = None
        self.__start_game_label = None


    def add_home_page(self, on_start_game, is_launch=True, player_name=None, player_score=None):
        if not is_launch:
            new_player = {"name": player_name if player_name else "Sam", "score": player_score if player_score else 0}
            self.__scores_overview.append(new_player)

            # scores table title
            self.__score_table_title.pack(side=TOP)  # pady=(0, 10)

            # show scores table
            self.__scores_table_fr.pack(side=TOP)  # pady=(20, 50)

            self.__score_tablehead_name.grid(row=1, column=1)
            self.__score_tablehead_score.grid(row=1, column=2)
            self.__show_scores()

        self.__add_start_btn(on_start_game, is_launch)

    def __add_start_btn(self, on_start_game, is_launch):
        # play btn
        self.__start_game_btns_ctr = tk.Frame(self.__parent, background=HomePageGUI.BG_COLOR)
        
        text = HomePageGUI.START_BTN_TEXT['FIRST_LAUNCH'] if is_launch else HomePageGUI.START_BTN_TEXT['NOT_FIRST_LAUNCH']

        self.__start_game_label = tk.Label(self.__start_game_btns_ctr,
                                           text=text, 
                                           background=HomePageGUI.BG_COLOR, 
                                           font=("", 20, "bold", "italic"),
                                           foreground='#6d9983',
                                           )

        self.__start_game_btn = RoundedButton(parent=self.__start_game_btns_ctr,
                                              width=self.circle_w_and_h,
                                              height=self.circle_w_and_h,
                                              cornerradius=60,
                                              padding=0,
                                              color="#006d77",
                                              active_color="#139eab",
                                              bg=HomePageGUI.BG_COLOR,
                                              text_color="white",
                                              font=40,
                                              text='▶',
                                              command=lambda: on_start_game()
                                              )
        self.__start_game_btns_ctr.pack(side=TOP, pady=(self.vh_func(4)))
        self.__start_game_label.pack(pady=(0, self.vh_func(1))) # pady=(self.vh_func(3), 0) ayala
        self.__start_game_btn.pack()

    def __show_scores(self):
        row_cnt = 2  # first row is title
        for i in range(len(self.__scores_overview) - 1, -1, -1):  # reverse display
            player = self.__scores_overview[i]
            # values of names
            tk.Label(self.__scores_table_fr,
                     width=self.score_width, fg='#1d3652',
                     font=('Arial', 16, 'bold'),
                     text=player["name"],
                     background=HomePageGUI.SCORES_TABLE_BG
                     ).grid(row=row_cnt, column=1)
            # values of names
            tk.Label(self.__scores_table_fr, width=self.score_width, fg='#1d3652',
                     font=('Arial', 16, 'bold'),
                     text=player["score"],
                     background=HomePageGUI.SCORES_TABLE_BG
                     ).grid(row=row_cnt, column=2)
            row_cnt += 1

    def __remove_score_table(self):
        self.__score_table_title.pack_forget()
        try:
            self.__score_tablehead_name.grid_remove()
        except Exception as e:
            # exception due to not packing these elements to begin with (cos they're optional-they're not on first launch)
            pass
        else:
            self.__score_tablehead_score.grid_remove()
            for item in self.__scores_table_fr.grid_slaves():
                item.grid_forget()
            self.__scores_table_fr.pack_forget()

    def remove_home_page(self):
        self.__remove_score_table()
        self.__start_game_label.pack_forget()
        self.__start_game_btn.pack_forget()  # initializes (.pack()) on every start of game
