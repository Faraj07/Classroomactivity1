from tkinter import *
import random
from typing import List
from tkinter import messagebox

woor_def = {
    "words":['cat', 'calculator' ,  'computer' , 'plant' , 'motorcycle', 'bus' ],
    "definiton":['House animal ( not dog )','GDC', 'Electronic devise','Flower','Car with 2 wheels','Big car']
}

words = { 'cat' : 'House animal ( not dog )',  'calculator': 'GDC', 'computer' :  'Electronic devise', 'plant': 'Flower','motorcycle':'Car with 2 wheels', 'bus': 'Big car'}

words_2= ['cat', 'calculator','computer', 'plant',  'motorcycle','bus' ]


options =woor_def.get('definiton')



matching =Tk()
matching.geometry("600x600")
matching.config(bg="#56aed6")
matching.title("Mathcing game")
clicked1 = StringVar()
clicked2 = StringVar()
clicked3 = StringVar()
clicked4 = StringVar()
clicked5 = StringVar()
clicked6 = StringVar()




program_name = Label(matching, text="---- Match the words ----", bg="#56aed6", font=("Roboto", 25))
program_name.pack(side=TOP)

def new () :
    global drop1,drop2,drop3,drop4,drop5,drop6
    random.shuffle(options)
    random.shuffle(words_2)


    word1 = Label(matching, text=words_2[0], bg="#56aed6", font=("Roboto", 20))
    word1.pack(anchor=SW, pady=10)
    word2 = Label(matching, text=words_2[1], bg="#56aed6", font=("Roboto", 20))
    word2.pack(anchor=SW, pady=10)
    word3 = Label(matching, text=words_2[2], bg="#56aed6", font=("Roboto", 20))
    word3.pack(anchor=SW, pady=10)
    word4 = Label(matching, text=words_2[3], bg="#56aed6", font=("Roboto", 20))
    word4.pack(anchor=SW, pady=10)
    word5 = Label(matching, text=words_2[4], bg="#56aed6", font=("Roboto", 20))
    word5.pack(anchor=SW, pady=10)
    word6 = Label(matching, text=words_2[5], bg="#56aed6", font=("Roboto", 20))
    word6.pack(anchor=SW, pady=10)














    drop5 = OptionMenu(matching, clicked5, *options)
    drop5.place(x=185, y=290)
    drop4 = OptionMenu(matching, clicked4, *options)
    drop4.place(x=185, y=230)
    drop3 = OptionMenu(matching, clicked3, *options)
    drop3.place(x=185, y=175)
    drop2 = OptionMenu(matching, clicked2, *options)
    drop2.place(x=185, y=120)
    drop1 = OptionMenu(matching, clicked1, *options)
    drop1.place(x=185, y=63)
    drop6 = OptionMenu(matching, clicked6, *options)
    drop6.place(x=185, y=344)
    drop1.config(fg="black")
    clicked1.set("Choose answer")
    clicked2.set("Choose answer")
    clicked3.set("Choose answer")
    clicked4.set("Choose answer")
    clicked5.set("Choose answer")
    clicked6.set("Choose answer")

    drop1.config(font=("Roboto", 10))






def check():
    for i in range(0, 6):
        if woor_def.get('words')[i] == words_2[0]:
            if clicked1.get() == words.get(words_2[0]):
                score.config(text='Correct')
            else:
                score.config(text='Mistake')
    for l in range(0, 6):
        if woor_def.get('words')[l] == words_2[1]:
            if clicked2.get() == words.get(words_2[1]):
                score2.config(text='Correct')
            else:
                score2.config(text='Mistake')
    for o in range(0, 6):
        if woor_def.get('words')[o] == words_2[2]:
            if clicked3.get() == words.get(words_2[2]):
                score3.config(text='Correct')
            else:
                score3.config(text='Mistake')
    for v in range(0, 6):
        if woor_def.get('words')[v] == words_2[3]:
            if clicked4.get() == words.get(words_2[3]):
                score4.config(text='Correct')
            else:
                score4.config(text='Mistake')
    for e in range(0, 6):
        if woor_def.get('words')[e] == words_2[4]:
            if clicked5.get() == words.get(words_2[4]):
                score5.config(text='Correct')
            else:
                score5.config(text='Mistake')
    for u in range(0, 6):
        if woor_def.get('words')[u] == words_2[5]:
            if clicked6.get() == words.get(words_2[5]):
                score6.config(text='Correct')
            else:
                score6.config(text='Mistake')


b = Button(matching, text="Check", fg="black", font=("Roboto", 15), command=check)
b.pack(side=BOTTOM)
new()
score = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score.place(x = 400 , y = 64)
score2 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score2.place(x = 400 , y = 119)
score3 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score3.place(x = 400 , y = 175)
score4 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score4.place(x = 400 , y = 230)
score5 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score5.place(x = 400 , y = 290)
score6 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
score6.place(x = 400 , y = 340)



matching.mainloop()