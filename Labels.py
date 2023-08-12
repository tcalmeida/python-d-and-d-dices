from tkinter import *


class Labels:
    def __init__(self, window, dice_result, row):
        self.window = window
        self.dice = dice_result
        self.row = row

        Label(self.window,
              textvariable=self.dice,
              font=('Arial', 15),
              width=20, bg='white') \
            .grid(row=self.row, column=1, pady=5)
