from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

main = Tk()
main.geometry("500x500")
name_display = Tk()
name_display.geometry("300x300")

FR = Frame(main ,width=500, height=250)
Displayin_name_on_the_main_screen = Label(FR, text="", font=("Roboto", 16))
Displayin_name_on_the_main_screen.pack()
play = False
def zapustit_igru():
    global start_label

    for l in range(len(names)):

        for n in range(len(names)):
            value_a = "User " + names[n] + " can start now!"
            Displayin_name_on_the_main_screen.config(text=value_a)

    if pb['value'] == 100:
        stop()
        progress()
start_button = Button(name_display,text="Start", font=("Roboto", 13),command=zapustit_igru)
start_button.pack(side=BOTTOM)


def new_window():
    global entry_1,name_display
    name_entry = Tk()
    name_entry.geometry("200x200")

    entry_1 = Entry(name_entry,font=("Roboto", 20))
    entry_1.pack()
    entry_1.focus()
    add_button = Button(name_entry,text="Add name", font=("Roboto", 16),command = add_names)
    add_button.pack(pady=10)


def add_names():
    global names
    names =[]

    name_itself = entry_1.get()
    names.append(name_itself)

    for item in names:
        namz = Label(name_display, text="", font=("Roboto", 16))
        namz.pack(anchor=W)

        namz.config(text=item)

    entry_1.delete(0, END)


n = True
def timer():
    global hours , minutes, seconds,n

    if hours == 4 or pb['value'] == 100 :
        return

    seconds +=1

    if seconds == 60:
        seconds = 00
        minutes +=1




    if minutes == 00 and seconds == 00:
        hours +=1

    scnd_ans.config(text= f'{hours:02}:{minutes:02}:{seconds:02}')

    main.after(1000 , timer)

scnd_ans = Label(main, text="", font=("Roboto", 25))
scnd_ans.pack()


hours ,minutes, seconds = 0, 0, 0




def update_progress_label():
    return f"Current Progress: {pb['value']}%"



def progress():
    global play,seconds,start_label,n,Displayin_name_on_the_main_screen
    if not play:
        play = True
        timer()
    value = "The progress completed at: " + str(seconds) + " Seconds"

    if pb['value'] < 100:
        pb['value'] += 5
        value_label['text'] = update_progress_label()
    else:
        showinfo(message=value)
        Displayin_name_on_the_main_screen.config(text="")
        n = False
        stop()
        mb()
        reset_timer()


def mb():
    scr = []
    scr.append(seconds)

    for item_2 in scr:
        scr = Label(name_display, text="", font=("Roboto", 16))
        scr.config(text=item_2)


    scr.pack(anchor=NE)

def reset_timer():
    global hours, minutes, seconds,play
    play = False
    hours, minutes, seconds = 0, 0, 0
    scnd_ans.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar( main,orient='horizontal',mode='determinate',length=280)
pb.pack()

# label
value_label = ttk.Label(main, text=update_progress_label())
value_label.pack()

# start button
start_button = ttk.Button(main,text='Slap mee!',command=progress)
start_button.pack()

stop_button = ttk.Button(main,text='Reset',command=stop)
stop_button.pack()


new_window()
FR.pack()
main.mainloop()