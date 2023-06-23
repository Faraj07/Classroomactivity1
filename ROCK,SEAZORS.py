from tkinter import*
import random
from tkinter import messagebox
main = Tk()
main.geometry('2000x2000')
frame = Frame(main, width=500, height=250 , bg ='#935ab0')
frame.pack()
frame.place(anchor='center', x=280, y=480)

frame2 = Frame(main, width=500, height=250 , bg ='#935ab0')
frame2.pack()
frame2.place(anchor='center', x=1635, y=480)

color_1 = Frame(main, width=100, height=100 , bg ='#cc9e1f')
color_1.pack()
color_1.place(anchor='center', x=690, y=495)

color_2 = Frame(main, width=100, height=100 , bg ='#cc9e1f')
color_2.pack()
color_2.place(anchor='center', x=1200, y=495)

correct = 0
draw = 0
lost_game = 0




list_of_items = ["Rock", "Paper", "Scissors"]
list_of_icons =["🪨","📄",'✂']

playing = True
player2 = True
def button_1():
    global playing,player2,draw,correct,lost_game,score_text
    score_text = f"Correct: {correct} | Loose: {lost_game} | Draw:  {draw}"
    score.config(text=score_text)
    playing = False
    player_choice.configure(text="🪨")
    rock_button.config(bg="red")
    rndm = random.randint(0, 2)
    player2 = False
    robot.configure(text = list_of_icons[rndm])
    value = "you have lost robot choose: " + list_of_items[rndm]#items 1
    value_2 = "you won robot choose: " + list_of_items[rndm]#items 2
    value_3 = "its draw: " + list_of_items[rndm]#items 0
    if list_of_items[rndm] == list_of_items[0]:
        draw += 1
        color_1.config(bg="gray")
        color_2.config(bg="gray")
        messagebox.showinfo("oops" ,value_3)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    elif list_of_items[rndm] == list_of_items[1]:
        lost_game +=1
        color_1.config(bg="red")
        color_2.config(bg="green")
        messagebox.showinfo("oops" ,value)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    elif list_of_items[rndm] == list_of_items[2]:
        correct +=1
        color_1.config(bg="green")
        color_2.config(bg="red")
        messagebox.showinfo("oops" ,value_2)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")


    playing = True
    player2 = True
    rock_button.config(bg="white")
    random_1()
    random_2()





def button_2():
    global playing,player2,draw,lost_game,correct,score_text
    score_text = f"Correct: {correct} | Loose: {lost_game} | Draw:  {draw}"
    score.config(text=score_text)
    paper_button.config(bg="red")
    playing = False
    player_choice.configure(text="📄")
    rndm = random.randint(0, 2)
    player2 = False
    robot.configure(text=list_of_icons[rndm])
    value = "you have lost robot choose: " + list_of_items[rndm]#item 2
    value_2 = "you won robot choose: " + list_of_items[rndm]#items 0
    value_3 = "its draw , robot chose: " + list_of_items[rndm]#items 1
    if list_of_items[rndm] == list_of_items[2]:
        lost_game +=1
        color_1.config(bg="red")
        color_2.config(bg="green")
        messagebox.showinfo("oops", value)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    elif list_of_items[rndm] == list_of_items[0]:
        correct += 1
        color_1.config(bg="green")
        color_2.config(bg="red")
        messagebox.showinfo("oops", value_2)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    elif list_of_items[rndm] == list_of_items[1]:
        draw +=1
        color_1.config(bg="gray")
        color_2.config(bg="gray")
        messagebox.showinfo("oops", value_3)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    playing = True
    player2 = True
    random_1()
    random_2()
    paper_button.config(bg="white")


def button_3():
    global playing,player2,draw, correct, lost_game,score_text
    playing = False
    player_choice.configure(text='✂')
    scissors_button.config(bg="red")
    rndm = random.randint(0, 2)
    player2 = False
    robot.configure(text=list_of_icons[rndm])
    value = "you have lost robot choose: " + list_of_items[rndm]#item 0
    value_2 = "you won robot choose: " + list_of_items[rndm]#items 1
    value_3 = "its draw , robot chose: " + list_of_items[rndm]#items 2
    if list_of_items[rndm] == list_of_items[2]:
        draw +=1
        color_1.config(bg="gray")
        color_2.config(bg="gray")
        messagebox.showinfo("oops", value_3)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")
    elif list_of_items[rndm] == list_of_items[0]:
        lost_game += 1
        color_1.config(bg="red")
        color_2.config(bg="green")
        messagebox.showinfo("oops", value)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")

    elif list_of_items[rndm] == list_of_items[1]:
        correct += 1
        color_1.config(bg="green")
        color_2.config(bg="red")
        messagebox.showinfo("oops", value_2)
        color_1.config(bg="#cc9e1f")
        color_2.config(bg="#cc9e1f")


    player2 = True
    playing = True
    random_1()
    random_2()
    scissors_button.config(bg="white")
    score_text = f"Correct: {correct} | Loose: {lost_game} | Draw:  {draw}"
    score.config(text=score_text)

player_choice = Label(color_1, text='🪨', font=('Roboto', 40))
player_choice.place(y=16, x=16)
robot = Label(color_2, text='🪨', font=('Roboto', 40))
robot.place(y=16, x=16)

def random_1():
    if playing == True:
        if player_choice['text'] == '🪨':
            player_choice.config(text='📄')
        elif player_choice['text'] == '📄':
            player_choice.config(text='✂')
        else:
            player_choice.config(text='🪨')
        player_choice.after(100, random_1)



random_1()


def random_2():
    if player2 == True:

        if robot['text'] == '🪨':
            robot.config(text='📄')
        elif robot['text'] == '📄':
            robot.config(text='✂')
        else:
            robot.config(text='🪨')
        robot.after(100, random_2)

random_2()







title = Label(main, text = "Rock-Paper-Scissors Game ", font= ('Roboto', 20))
title.pack()

choice = Label(frame, text = " Make your choice ",bg = "#935ab0", font= ('Roboto', 20))
choice.place(x= 134 , y = 20)
choice2 = Label(frame2, text = " ROBOT CHOOICE ",bg = "#935ab0", font= ('Roboto', 20))
choice2.place(x= 134 , y = 20)


rock_button = Button(frame, text = '🪨', font= ("Roboto", 24), command=button_1)
rock_button.place(x = 90 , y = 100)
paper_button = Button(frame, text = "📄", font= ("Roboto", 24), command=button_2)
paper_button.place(x =215 , y = 100)
scissors_button = Button(frame, text = '✂', font= ("Roboto", 24), command=button_3)
scissors_button.place(x =350 , y = 100)


disable = Button(frame2, text = '🪨', font= ("Roboto", 24))
disable.place(x = 90 , y = 100)
disable2 = Button(frame2, text = "📄", font= ("Roboto", 24))
disable2.place(x =215 , y = 100)
disable3 = Button(frame2, text = '✂', font= ("Roboto", 24))
disable3.place(x =350 , y = 100)
score = Label(main, text="", font=('Roboto', 30))
score.place(x=1100, y=930)

main.mainloop()