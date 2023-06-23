from os import sep
from tkinter import *
import random
from tkinter.constants import *
import tkinter as tk


words = [ "cat - House animal ", "Calculator - GDC  ", "computer - Electronic devise", "plant - Flower ","motorcycle -Car with 2 wheels", "bus - Big car"]






Timer = tk.Tk()
Timer.geometry("600x600")
Timer.config(bg="#56aed6")



program_name = Label(Timer, text="---- Rememmber the words ----", bg="#56aed6", font=("Roboto", 25))
program_name.pack(side=TOP)



def timer():
    global hours , minutes, seconds

    if hours == 4:
        return

    seconds -=1

    if seconds == 00:
        Timer.destroy()
        import Matching



    if minutes == 00 and seconds == 00:
        hours +=1

    scnd_ans.config(text= f'{hours:02}:{minutes:02}:{seconds:02}')

    Timer.after(1000 , timer)

def test():

    random.shuffle(words)

    for item in words:
        wordss = Label(Timer, text="", bg="#56aed6", font=("Roboto", 20))
        wordss.pack(anchor=W, pady = 6)

        wordss.config(text=item)


test()






scnd_ans = Label(Timer, text="", bg="#56aed6", font=("Roboto", 25))
scnd_ans.place(x = 465 , y = 500)


hours ,minutes, seconds = 0, 0, 15
timer()
Timer.mainloop()