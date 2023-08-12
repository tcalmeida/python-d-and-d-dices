import random
from tkinter import *
from Labels import Labels


def row_d4():
    num = str(random.randint(1, 4))
    result_d4.set(num)


def row_d6():
    num = str(random.randint(1, 6))
    result_d6.set(num)


def row_d8():
    num = str(random.randint(1, 8))
    result_d8.set(num)


def row_d10():
    num = str(random.randint(1, 10))
    result_d10.set(num)


def row_d12():
    num = str(random.randint(1, 12))
    result_d12.set(num)


def row_d20():
    num = str(random.randint(1, 20))
    result_d20.set(num)


dices = ['D4', 'D6', 'D8', 'D10', 'D12', 'D20']
dice_row = [row_d4, row_d6, row_d8, row_d10, row_d12, row_d20]

window = Tk()
window.title('D&D Dices')
window.geometry('400x250')

result_d4 = StringVar()
result_d6 = StringVar()
result_d8 = StringVar()
result_d10 = StringVar()
result_d12 = StringVar()
result_d20 = StringVar()

Labels(window, result_d4, 1)
Labels(window, result_d6, 2)
Labels(window, result_d8, 3)
Labels(window, result_d10, 4)
Labels(window, result_d12, 5)
Labels(window, result_d20, 6)

row = 1
index = 0

for dice in dices:
    Label(window, text=dice, font=('Arial', 15, 'bold'), fg='red', width=5).grid(row=row, column=0)
    Button(window, text='Roll', font=('Arial', 15), command=dice_row[index]).grid(row=row, column=2, padx=10)
    row += 1
    index += 1

window.mainloop()
