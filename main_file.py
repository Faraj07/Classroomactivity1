import math
from tkinter import *
from tkinter import messagebox
import random
import tkinter as tk

main = Tk()
main.config(bg="#56aed6")
main.geometry("700x700")
n = 0
hours, minutes, seconds = 0, 0, 15
counter = 0

words = ["cat", "car", "computer", "plant", "motorcycle", "bus"]

definition = ["House animal ( not dog ) ", "transportation", "Electronic devise", "Flower", "Car with 2 wheels",
                  "Big car"]


wordss = ["cat - House animal ", "Calculator - GDC ", "computer - Electronic devise", "plant - Flower ",
         "motorcycle -Car with 2 wheels", "bus - Big car"]

woor_def = {
        "words": ['cat', 'calculator', 'computer', 'plant', 'motorcycle', 'bus'],
        "definiton": ['House animal ( not dog )', 'GDC', 'Electronic devise', 'Flower', 'Car with 2 wheels', 'Big car']
    }

words_with_def = {'cat': 'House animal ( not dog )', 'calculator': 'GDC', 'computer': 'Electronic devise',
                  'plant': 'Flower',
                  'motorcycle': 'Car with 2 wheels', 'bus': 'Big car'}

words_2 = ['cat', 'calculator', 'computer', 'plant', 'motorcycle', 'bus']




program_name = Label(main, text="+------- Language test ------+", bg="#56aed6",fg= "red", font=("Roboto", 25))
program_name.pack(side=TOP)


rw_for_names = Label(main, text="Choose game ", bg="#56aed6", font=("Roboto", 20))
rw_for_names.pack(side= TOP, pady= 34)

def open_QA():
    global counter
    main.destroy()


    guess_word = Tk()
    guess_word.geometry("600x600")
    guess_word.config(bg="#56aed6")

    result = Label(guess_word, text="", bg="#56aed6", font=("Roboto", 25))
    final = Label(guess_word, text="", bg="#56aed6", font=("Roboto", 25))
    score = Label(guess_word, text="", bg="#56aed6", font=("Roboto", 25))

    program_name = Label(guess_word, text="Q&A", bg="#56aed6", font=("Roboto", 25))
    program_name.pack()

    initial = Label(guess_word, bg="#56aed6", font=("Roboto", 20))
    initial.pack()

    entry = Entry(guess_word, font=("Roboto", 15))
    entry.pack()


    value = "Correct answers: " + str(counter)
    score.config(text=value)

    def check():
        global counter
        if entry.get() == "":
            messagebox.showwarning("error 4x4", "Please enter the answer")
        else:
            if entry.get() == answer:
                result.config(text='Correct ✔')
            else:
                result.config(text='Mistake ❌')
        if entry.get() == answer:
            counter = counter + 1
            value_a = "Correct answers: " + str(counter)
            score.config(text=value_a)

    def ask():
        entry.delete(0, END)
        global random_index

        global answer
        random_index = random.randint(0, len(definition) - 1)
        question = "what is " + definition[random_index] + ":"
        answer = words[random_index]
        initial.config(text=question)
        result.config(text="")
        final.config(text="")

    ask()
    entry.focus()
    m = 0


    def Hint():
        global n
        global m

        str((len(answer)) * "*")

        amount = answer[:+n] + str((len(answer) - n) * "*")
        aa = "Hint: " + amount
        n = n + 1

        if len(answer) == 3:

            if n == 3:
                messagebox.showinfo("info", " las hint")
                n = 0

        if  len(answer) > 4:
            if n == 5:
                messagebox.showinfo("info", " last hint")
                n = 0
        if 6 > len(answer) > 3:
            if n == 4:
                messagebox.showinfo("info", " last hint")
                n = 0

        final.config(text=aa)

    def back():
        guess_word.destroy()










    go_back = Button(guess_word, text="Menu", fg="black", font=("Roboto", 15), command=back)

    hint = Button(guess_word, text="Hint", fg="black", font=("Roboto", 15), command=Hint)

    next_button = Button(guess_word, text="Next", fg="black", font=("Roboto", 15), command=ask)

    submit_button = Button(guess_word, text="submit", fg="black", font=("Roboto", 15), command=check)
    submit_button.pack()
    hint.pack()
    next_button.pack()

    final.pack()
    result.pack()
    score.pack(side=BOTTOM)
    go_back.pack(side="right")


    guess_word.mainloop()


def timer():
    main.destroy()



    Timer = tk.Tk()
    Timer.geometry("600x600")
    Timer.config(bg="#56aed6")

    program_name = Label(Timer, text="---- Rememmber the words ----", bg="#56aed6", font=("Roboto", 25))
    program_name.pack(side=TOP)

    def timer():
        global hours, minutes, seconds

        if hours == 4:
            return

        seconds -= 1

        if seconds == 00:
            Timer.destroy()
            open_matching()

        if minutes == 00 and seconds == 00:
            hours += 1

        scnd_ans.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

        Timer.after(1000, timer)

    def test():

        random.shuffle(wordss)

        for item in wordss:
            wordsss = Label(Timer, text="", bg="#56aed6", font=("Roboto", 20))
            wordsss.pack(anchor=W, pady=6)

            wordsss.config(text=item)

    test()

    scnd_ans = Label(Timer, text="", bg="#56aed6", font=("Roboto", 25))
    scnd_ans.place(x=465, y=500)


    timer()
    Timer.mainloop()

def open_matching():

    options = woor_def.get('definiton')

    matching = Tk()
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

    def new():
        global drop1, drop2, drop3, drop4, drop5, drop6
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
                if clicked1.get() == words_with_def.get(words_2[0]):
                    score.config(text='Correct')
                else:
                    score.config(text='Mistake')
        for l in range(0, 6):
            if woor_def.get('words')[l] == words_2[1]:
                if clicked2.get() == words_with_def.get(words_2[1]):
                    score2.config(text='Correct')
                else:
                    score2.config(text='Mistake')
        for o in range(0, 6):
            if woor_def.get('words')[o] == words_2[2]:
                if clicked3.get() == words_with_def.get(words_2[2]):
                    score3.config(text='Correct')
                else:
                    score3.config(text='Mistake')
        for v in range(0, 6):
            if woor_def.get('words')[v] == words_2[3]:
                if clicked4.get() == words_with_def.get(words_2[3]):
                    score4.config(text='Correct')
                else:
                    score4.config(text='Mistake')
        for e in range(0, 6):
            if woor_def.get('words')[e] == words_2[4]:
                if clicked5.get() == words_with_def.get(words_2[4]):
                    score5.config(text='Correct')
                else:
                    score5.config(text='Mistake')
        for u in range(0, 6):
            if woor_def.get('words')[u] == words_2[5]:
                if clicked6.get() == words_with_def.get(words_2[5]):
                    score6.config(text='Correct')
                else:
                    score6.config(text='Mistake')

    b = Button(matching, text="Check", fg="black", font=("Roboto", 15), command=check)
    b.pack(side=BOTTOM)
    new()
    score = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score.place(x=400, y=64)
    score2 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score2.place(x=400, y=119)
    score3 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score3.place(x=400, y=175)
    score4 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score4.place(x=400, y=230)
    score5 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score5.place(x=400, y=290)
    score6 = Label(matching, text="", bg="#56aed6", font=("Roboto", 15))
    score6.place(x=400, y=340)

    matching.mainloop()

button = Button(main, text="Q&A", bg="RED", font=("Roboto", 17),command= open_QA)
button.pack(side=TOP, pady= 25)

button = Button(main, text="Matching", bg="RED", font=("Roboto", 17),command= timer)
button.pack(side=TOP, pady= 30)


answe =Label(main, text="", bg="#56aed6", font=("Roboto", 25))
answe.pack(side= TOP, pady = 37)

scnd_ans = Label(main, text="", bg="#56aed6", font=("Roboto", 25))
scnd_ans.pack(side= TOP, pady = 37)

main.mainloop()