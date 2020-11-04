from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

root = Tk()
w = Label(root, text="Guess Number Game")
w.pack()

mb.showinfo("Welcome", "Welcome to Guess Number Game")

number = 59
while True:
    guess = dl.askinteger("Number", "What's your guess number")

    if guess == number:
        output = 'Bingo, you guessed it right!'
        mb.showinfo("Hint: ", output)
        break
    elif guess < number:
        output = 'No, the number is a higer than that'
        mb.showinfo("Hint: ", output)
    else:
        output = 'No, the number is a lower than that'
        mb.showinfo("Hint: ", output)
print('Done')
mb.showinfo("Output: ", 'Game Over!')
