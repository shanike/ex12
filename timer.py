from tkinter import *
from tkinter import messagebox


class Timer:
    def __init__(self, parent, count, on_time_up):
        self.__on_time_up = on_time_up
        self.parent = parent
        self.count = count
        # setting the default value as 0
        self.minute = StringVar(self.parent, "03")  # todo set afterward or now?
        self.second = StringVar(self.parent, "00")  # todo set afterward or now?

        self.minute_label = Label(self.parent, width=3, font=("Arial", 18, ""),
                                  textvariable=self.minute, bg="#ffd6ba", foreground="white")
        self.second_label = Label(self.parent, width=3, font=("Arial", 18, ""),
                                  textvariable=self.second, bg="#ffd6ba", foreground="white")

    def set_timer(self):
        # set labels
        self.minute_label.place(x=130, y=20)

        self.second_label.place(x=180, y=20)

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
                self.on_time_up()
            # after every one sec the value of temp will be decremented by one
            self.parent.after(1000, self.countdown, count - 1)

    def on_time_up(self):
        self.__on_time_up()

    def remove_timer(self):
        self.minute_label.pack_forget()
        self.second_label.pack_forget()