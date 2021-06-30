from tkinter import Label, StringVar, messagebox
from tkinter.constants import LEFT, RIGHT


class Timer:
    def __init__(self, parent, count, on_time_up):
        self.__on_time_up = on_time_up
        self.__parent = parent
        self.__count = count
        # setting the default value as 0
        self.__time_val = StringVar(self.__parent, "03")
        self.__second = StringVar(self.__parent, "00")

        self.__time_label = Label(self.__parent, width=6, font=("Arial", 18, ""),
                                  textvariable=self.__time_val, bg="#ffc59c", foreground="white")
        # self.__second_label = Label(self.__parent, width=3, font=("Arial", 18, ""),
        #                           textvariable=self.__second, bg="#ffc59c", foreground="white")

    def init_timer(self):
        """renders timer elements to the screen
        """
        # set labels
        self.__time_label.pack(side=LEFT)

        # self.__second_label.pack(side=RIGHT)

        self.__countdown(self.__count)

    def __countdown(self, count):
        """updates screen to show current time left
        """
        if count > -1:

            mins, secs = divmod(count, 60)
            if mins > 60:
                mins = count % 60

            # using format () method to store the value up to
            self.__time_val.set("{0:0=2d}".format(
                mins)+" : " + "{0:0=2d}".format(secs))
            # self.__second.set()

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if count == 0:
                messagebox.showinfo("Time Countdown", "Time's up ")
                self.__on_time_up()
            # after every one sec the value of temp will be decremented by one
            self.__parent.after(1000, self.__countdown, count - 1)

    def remove_timer(self):
        """removes timer from view
        """
        self.__time_label.pack_forget()
        # self.__second_label.pack_forget()
