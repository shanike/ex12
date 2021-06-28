from tkinter import *
from tkinter import messagebox


class Timer:
    def __init__(self, parent, count):
        self.parent = parent
        self.count = count
        # setting the default value as 0
        self.minute = StringVar("03")
        self.second = StringVar("00")

    def set_timer(self):
        # set labels
        minute_label = Label(self.parent, width=3, font=("Arial", 18, ""),
                             textvariable=self.minute, bg="#ffd6ba", foreground="white")
        minute_label.place(x=130, y=20)

        second_label = Label(self.parent, width=3, font=("Arial", 18, ""),
                             textvariable=self.second, bg="#ffd6ba", foreground="white")
        second_label.place(x=180, y=20)

        self.countdown(self.count)

    def countdown(self, count):
        if count > -1:

            mins, secs = divmod(count, 60)
            if mins > 60:
                mins = count % 60

            # using format () method to store the value up to
            self.minute.set("{0:0=2d}".format(mins))
            self.second.set("{0:0=2d}".format(secs))

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if count == 0:
                messagebox.showinfo("Time Countdown", "Time's up ")
                self.handle_end_game()
            # after every one sec the value of temp will be decremented by one
            self.parent.after(1000, self.countdown, count - 1)

    def handle_end_game(self):
        pass
