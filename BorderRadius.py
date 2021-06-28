# from tkinter import *
import tkinter as tk
from tkinter.constants import ANCHOR

# root = Tk()


class RoundedButton(tk.Canvas):
    def __init__(self, parent, width, height, cornerradius, padding, color, active_color, bg, text, text_color, command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="flat", highlightthickness=0, bg=bg)

        self.width = width
        self.height = height
        self.cornerradius = cornerradius
        self.padding = padding
        self.color = color
        self.active_color = active_color
        self.bg = bg
        self.text = text
        self.text_color = text_color
        self.command = command
        self.command = command

        if cornerradius > 0.5 * width:
            return None

        if cornerradius > 0.5 * height:
            return None

        self.rad = 2 * cornerradius

        id = self.shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1 - x0)
        height = (y1 - y0)
        self.configure(width=width, height=height)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self.handle_enter)
        self.bind("<Leave>", self.handle_leave)

    def shape(self, active=False):

        self.create_polygon((self.padding,
                             self.height - self.cornerradius - self.padding,
                             self.padding,
                             self.cornerradius + self.padding,
                             self.padding + self.cornerradius,
                             self.padding,
                             self.width - self.padding - self.cornerradius,
                             self.padding,
                             self.width - self.padding,
                             self.cornerradius + self.padding,
                             self.width - self.padding,
                             self.height - self.cornerradius - self.padding,
                             self.width - self.padding - self.cornerradius,
                             self.height - self.padding,
                             self.padding + self.cornerradius,
                             self.height - self.padding),
                            fill=self.color if not active else self.active_color,
                            # activefill=active_color,
                            outline=self.color if not active else self.active_color)

        self.create_text(self.width / 2, self.height / 2, fill=self.text_color,
                         font=("Vernada", 20, "bold"), text=self.text,)
        self.create_arc((self.padding, self.padding + self.rad, self.padding + self.rad, self.padding),
                        start=90, extent=90, fill=self.color if not active else self.active_color, outline=self.color if not active else self.active_color)
        self.create_arc((self.width - self.padding - self.rad, self.padding, self.width - self.padding,
                        self.padding + self.rad), start=0, extent=90, fill=self.color if not active else self.active_color, outline=self.color if not active else self.active_color)
        self.create_arc((self.width - self.padding, self.height - self.rad - self.padding, self.width - self.padding - self.rad,
                        self.height - self.padding), start=270, extent=90, fill=self.color if not active else self.active_color, outline=self.color if not active else self.active_color)
        self.create_arc((self.padding, self.height - self.padding - self.rad, self.padding + self.rad, self.height -
                        self.padding), start=180, extent=90, fill=self.color if not active else self.active_color, outline=self.color if not active else self.active_color)

    def _on_press(self, event):
        self.configure(relief="sunken")

    def _on_release(self, event):
        self.configure(relief="raised")
        if self.command is not None:
            self.command()

    def handle_enter(self, event):
        self.shape(True)

    def handle_leave(self, event):
        self.shape(False)

        # canvas = Canvas(root, height=300, width=500)
        # canvas.pack()

        # button = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=test)
        # button.place(relx=.1, rely=.1)

        # root.mainloop()
