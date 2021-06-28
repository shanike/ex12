from tkinter import *
from tkinter import messagebox


class Timer:
    def __init__(self, parent, count):
        self.parent = parent
        self.count = count
        self.minute = StringVar()
        self.second = StringVar()

    def set_timer(self):
        # setting the default value as 0
        self.minute.set("03")
        self.second.set("00")

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

            # updating the GUI window after decrementing the
            # temp value every time
            self.parent.update()

            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if count == 0:
                messagebox.showinfo("Time Countdown", "Time's up ")
                self.handle_end_game()
            # after every one sec the value of temp will be decremented by one
            self.parent.after(1000, self.countdown, count - 1)

    def handle_end_game(self):
        pass

# # creating Tk window
# parent = Tk()
#
# # setting geometry of tk window
# parent.geometry("300x250")
#
# # Using title() to display a message in
# # the dialogue box of the message in the
# # title bar.
# parent.title("Time Counter")
#
# timer = Timer(parent, 180)
#
# parent.mainloop()
