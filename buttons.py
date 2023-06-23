import random
from tkinter import *

root = Tk()
root.geometry("1000x1000")
pressed = -1
not_pressed = 0
play_Aim = False

def new():
    global pressed,value
    new1 = Tk()
    final = not_pressed - pressed
    vaue_a = "buttons were pressed: " + str(pressed)
    vaue_b= "buttons were miss: " + str(final)

    Presed =Label(new1, text= vaue_a)
    Presed.pack()
    not_Presed = Label(new1, text=vaue_b)
    not_Presed.pack()

    new1.mainloop()
xx = random.randint(0,800)
yy = random.randint(200,300)
n = False
def start():
    global xx,yy,button,pressed,play_Aim
    button.destroy()
    pressed = pressed + 1
    xx = xx + random.randint(0, 800)
    yy = yy + random.randint(100, 300)


    n = False
    while n == False:
        if not play_Aim:
            play_Aim = True
            timer()
        def left_click(event):
            global not_pressed
            not_pressed = not_pressed + 1

            print("Left-click detected at", event.x, event.y)

        # Bind the left mouse button click event to the root window
        root.bind("<Button-1>", left_click)

        button = Button(root, text="Press me", command=start)
        button.place(x=xx,y=yy)

        n = True






hours ,minutes, seconds = 0, 0, 5
def timer():
    global hours , minutes, seconds



    seconds -=1

    if seconds == 00:
        new()




    if minutes == 00 and seconds == 00:
        hours +=1

    scnd_ans.config(text= f'{hours:02}:{minutes:02}:{seconds:02}')

    root.after(1000 , timer)

scnd_ans = Label(root, text="", font=("Roboto", 25))
scnd_ans.pack()



button = Button(root, text= "Start  ", command= start )
button.pack(side=TOP)
root.mainloop()
