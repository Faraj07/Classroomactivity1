from fpdf import FPDF
from tkinter import *
import json

main = Tk()
main.geometry("500x500")
bottomframe = Frame(main)

def adding():
    global new, name_entry, buttons_frame
    new = Tk()
    new.geometry("250x200")
    name_entry = Entry(new, font=("Roboto", 20))
    name_entry.pack()
    SAVE = Button(new, text="Add", font=("Roboto", 20), command=add_name_button)
    SAVE.pack(pady=35)


def add_name_button():
    global name_2
    name_2 = name_entry.get()
    tmpr.append(name_2)
    new.destroy()
    for widgets in bottomframe.winfo_children():
        widgets.destroy()
    diplay()






def save_to_jasn():
    global json_fil
    json_file = open("students.json", "w")
    json.dump(tmpr, json_file)
    json_file.close()

add_button = Button(main, text="Add / + ", font=("Roboto", 20),command=adding)
add_button.pack()

btn = Button(main, text="save", font=("Roboto", 15), command=save_to_jasn)
btn.pack()
def load_to_json():
    with open("students.json", "r") as read_file:
        return json.load(read_file)
tmpr = load_to_json()

def diplay():

    for n in range(len(tmpr)):

        btn = Button(bottomframe, text=tmpr[n], font=("Roboto", 15))
        btn.pack(anchor=W)

diplay()

bottomframe.pack( anchor=W )


def start():
    marking = Toplevel(main)
    marking.geometry("250x400")
    options = ['1', '2', '3', '4', '5', '6', '7']
    clicked = StringVar()

    def temp_text(e):
        student_comment_entry.delete(0, "end")

    student_mark = Label(marking, text= 'Student mark: ', font=("Roboto", 18))
    student_mark.pack()

    marks = OptionMenu(marking, clicked, *options)
    marks.pack(pady=20)
    marks.config(width=8)



    student_comment_entry = Entry(marking, font=("Roboto", 18))
    student_comment_entry.insert(0, "Student Comments...")

    student_comment_entry.pack(pady=30)
    student_comment_entry.bind("<FocusIn>", temp_text)
    def save_pdf():
        global comment
        if student_comment_entry.get() == "Student Comments...":
          comment = "No Comment"
          mark = clicked.get()

          pdf = FPDF()

          pdf.add_page()

          pdf.set_font("Arial", size=18)
          pdf.cell(0, 10, f"{name_2}", align="C")
          pdf.ln()
          pdf.cell(0, 10, f"Mark: {mark}", align="L")
          pdf.ln()
          pdf.cell(0, 10, f"Comment: {comment}", align="L")
          marking.destroy()
          pdf.output("example.pdf")
        else:
            comment = student_comment_entry.get()

            mark = clicked.get()

            pdf = FPDF()

            pdf.add_page()

            pdf.set_font("Arial", size=18)
            pdf.cell(0, 10, f"{name_2}", align="C")
            pdf.ln()
            pdf.cell(0, 10, f"Mark: {mark}", align="L")
            pdf.ln()
            pdf.cell(0, 10, f"Comment: {comment}", align="L")
            marking.destroy()
            pdf.output("example.pdf")

    save_button = Button(marking, text="Save ", font=("Roboto", 10), command=save_pdf)
    save_button.pack()

    marking.mainloop()

main.mainloop()