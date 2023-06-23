guess_word = Tk()
guess_word.geometry("500x500")
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

counter = 0
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
n = 0
def Hint():
    global n
    global m

    str((len(answer)) * "*")

    amount =answer[:+n] + str((len(answer) - n ) * "*")
    aa = "Hint: " + amount
    n = n + 1

    if len(answer) == 3:

        if n == 3:
            messagebox.showinfo("info", " las hint")
            n = 0

    if 13 > len(answer) > 5:
        if n == 5:
            messagebox.showinfo("info", " last hint")
            n = 0
    if 6 > len(answer) > 3:
        if n == 4:
            messagebox.showinfo("info", " last hint")
            n = 0



    final.config(text=aa)














hint = Button(guess_word, text="Hint", fg="black", font=("Roboto", 15), command=Hint)


next_button = Button(guess_word, text="Next", fg="black", font=("Roboto", 15), command=ask)


submit_button = Button(guess_word, text="submit", fg="black", font=("Roboto", 15), command=check)
submit_button.pack()
hint.pack( )
next_button.pack()



final.pack()
result.pack( )
score.pack(side = BOTTOM)



guess_word.mainloop()