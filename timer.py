from tkinter import *
from tkinter import messagebox


class Timer:
    def __init__(self, parent, count, on_time_up):
        self.__on_time_up = on_time_up
        self.__parent = parent
        self.__count = count
        # setting the default value as 0
        self.__minute = StringVar(self.__parent, "03")
        self.__second = StringVar(self.__parent, "00")

        self.__minute_label = Label(self.__parent, width=3, font=("Arial", 18, ""),
                                  textvariable=self.__minute, bg="#ffd6ba", foreground="white")
        self.__second_label = Label(self.__parent, width=3, font=("Arial", 18, ""),
                                  textvariable=self.__second, bg="#ffd6ba", foreground="white")

    def init_timer(self):
        """renders timer elements to the screen
        """
        # set labels
        self.__minute_label.place(x=130, y=20)

        self.__second_label.place(x=180, y=20)

        self.__countdown(self.__count)

    def __countdown(self, count):
        """updates screen to show current time left
        """
        if count > -1:

            mins, secs = divmod(count, 60)
            if mins > 60:
                mins = count % 60

            # using format () method to store the value up to
            self.__minute.set("{0:0=2d}".format(mins))
            self.__second.set("{0:0=2d}".format(secs))

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if count == 0:
                messagebox.showinfo("Time Countdown", "Time's up ")
                self.__on_time_up()
            # after every one sec the value of temp will be decremented by one
            self.__parent.after(1000, self.__countdown, count - 1)

    def __on_time_up(self):
        self.__on_time_up()

    def remove_timer(self):
        """removes timer from view
        """
        self.__minute_label.pack_forget()
        self.__second_label.pack_forget()