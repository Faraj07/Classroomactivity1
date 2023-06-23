# Import required libraries
from idlelib import replace
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Create an instance of tkinter window
win = Tk()

# Define the geometry of the window
win.geometry("1000x350")

menu = { "names": ["kebab", "yumurta"],
         "prices": [1.3, 3],
         "pircures": ["keb.jpg", "pomidor-yumurta_1577030806.jpg" ]}


# OOP - Object Oriented Programming


frame = Frame(win, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)




# Create an object of tkinter ImageTk(196x196)
img_pom = ImageTk.PhotoImage(Image.open(menu.get('pircures')[1]))
img_kebab = ImageTk.PhotoImage(Image.open(menu.get('pircures')[0]).resize((196,196)))


# Create a Label Widget to display the text or Image
pl_pom = Label(frame, image = img_pom)
pl_pom.pack(side=TOP,anchor=CENTER)

pl_keb = Label(win, image = img_kebab)
pl_keb.place(x=135)




text = 7.5
symb = " $ 7.5 "
label_text1 = Label(frame, text=symb ,bg='yellow', font=("Roboto", 17))
label_text1.place(x=120, y=160 )



text2 = 8.5
symb2 = " $ 8.5 "
label_text2 = Label(win, text=symb2 ,bg='yellow', font=("Roboto", 17))
label_text2.place(x=255, y=190,anchor=SW)
n=0

label_text3 = Label(frame, text=n, font=("Roboto", 17))
label_text3.place(x=89, y =210 )

def plusik():
    global n
    n = n + 1
    label_text3.config(text=n)
    final = 'Total is: ' + str(n * text) + " $"
    totala.config(text=final)


def minusik():
    global n

    if n < 1:
        messagebox.showinfo("info", "its already zero!")
    else:
        n = n - 1
        label_text3.config(text=n)
        final = 'Total is: ' + str(n * text) + " $"
        totala.config(text=final)

m=0

label_text4 = Label(win, text=m, font=("Roboto", 17))
label_text4.place(x=225, y =205 )

def pluysik2():
    global m
    m = m + 1
    label_text4.config(text=m)
    final = 'Total is: ' + str(m * text2) + " $"
    totala2.config(text=final)

def minusik2():
    global m

    if m < 1:
        messagebox.showinfo("info", "its already zero!")
    else:
        m = m - 1
        label_text4.config(text=m)
        final = 'Total is: ' + str(m * text2) + " $"
        totala2.config(text=final)


plus = Button(frame, text=" + ", font=("Roboto", 15), command=plusik)
plus.place(x=159, y = 205)

minus = Button(frame, text=" - ", font=("Roboto", 15), command= minusik)
minus.place(x=0,y=205)



plus2 = Button(win, text=" + ", font=("Roboto", 15), command=pluysik2)
plus2.place(x=295, y = 200)

minus2 = Button(win, text=" - ", font=("Roboto", 15), command= minusik2)
minus2.place(x=135,y=200)

totala = Label(frame, text="", font=("Roboto", 17))
totala.pack(pady=65)

totala2 = Label(win, text="", font=("Roboto", 17))
totala2.place(x=160, y=260)




def total():
    new = Tk()
    new.geometry("250x250")

    total_cost = (n*text) + (m*text2)

    bill = Label(new, text="Total you need,\n" "to pay is : ", font=("Monospace", 20))
    bill.pack()
    new_one = Label(new, text=total_cost, font=("Monospace", 25))
    new_one.pack(pady= 45)
    dollar = Label(new, text="$", font=("Monospace", 20))
    dollar.place(x=160,y=117)





    new.mainloop()

def change_cost():
    global text, text2, symb, symb2, label_text1, label_text2



    # Create a new window for inputting new costs
    change_win = Tk()
    change_win.geometry("450x250")

    # Create labels and entry boxes for new costs
    label1 = Label(change_win, text="New cost for Pomidor Yumurta: ",font=("Monospace", 15))
    label1.pack(pady=10)
    entry1 = Entry(change_win,font=("Monospace", 15))
    entry1.pack()

    label2 = Label(change_win, text="New cost for Kebab: ", font=("Monospace", 15))
    label2.pack(pady=10)
    entry2 = Entry(change_win,font=("Monospace", 15))
    entry2.pack()


    # Define a function to update the costs and labels
    def update_cost():
        global text, text2, symb, symb2, label_text1, label_text2,n,m
        n = 0
        m = 0
        label_text3.config(text=n)
        label_text4.config(text=m)
        if n == 0:
            new_final = 'Total is: ' + str(n * text2) + " $"
            totala.config(text=new_final)
            final_secnd = 'Total is: ' + str(m * text2) + " $"
            totala2.config(text=final_secnd)


        # Update the values and labels with the new costs
        text = float(entry1.get())
        symb = f" $ {text} "
        label_text1.config(text=symb)

        text2 = float(entry2.get())
        symb2 = f" $ {text2} "
        label_text2.config(text=symb2)

        # Close the window
        change_win.destroy()


    # Add a button to update the costs
    update_button = Button(change_win, text="Update", command=update_cost,font=("Monospace", 10))
    update_button.pack(pady=20)

    change_win.mainloop()

final_total = Label(win, text="", font=("Roboto", 17))
final_total.pack(side='right')





chang = Button(win, text="  Bill  ", font=("Roboto", 15), command=total )
chang.pack(side= "right")


change_cost_button = Button(win, text="Update Cost", font=("Roboto", 15), command=change_cost)
change_cost_button.pack(side='right', anchor=SE)


win.mainloop()