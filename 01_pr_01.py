import tkinter.messagebox as tmsg
from tkinter import *


root = Tk()


def gr():
    with open("clint_detale.txt", "a")as f:
        f.write(f" clinte name is {NAMEVALUE.get()}\n")

    with open("clint_detale.txt", "a")as f:
        f.write(f" clintes father name is {FATHER_NAMEVALUE.get()}\n")

    with open("clint_detale.txt", "a")as f:
        f.write(f" clintes mother name is {MOTHER_NAMEVALUE.get()}\n\n")


name = Label(text="enter your name", bg="orange")
father_name = Label(text=f"enter your father name", bg="white")
mother_name = Label(text="enter your mother name", bg="lightgreen")
name.grid()
father_name.grid(row=1)
mother_name.grid(row=2)

NAMEVAR = StringVar()
FATHER_NAMEVAR = StringVar()
MOTHER_NAMEVAR = StringVar()

NAMEVALUE = Entry(root, textvariable=NAMEVAR,)
FATHER_NAMEVALUE = Entry(root, textvariable=FATHER_NAMEVAR)
MOTHER_NAMEVALUE = Entry(root, textvariable=MOTHER_NAMEVAR)
NAMEVALUE.grid(row=0, column=1)
FATHER_NAMEVALUE.grid(row=1, column=1)
MOTHER_NAMEVALUE.grid(row=2, column=1)

Button(text="submit", command=gr).grid()

root.mainloop()


root = Tk()


def gef():
    print("value submited")


root.geometry("300x400")

Label(root, text="Exersise is in the down",
      font="comicsansms 13 bold italic", pady=15).grid(row=0, column=3)

username = Label(root, text="Enter the user name",
                 font="comicsansms 13 italic")
pasword = Label(root, text="Enter the pasword name",
                font="comicsansms 13 italic")
username.grid(row=1, column=2)
pasword.grid(row=2, column=2)

usernamevalue = StringVar()
passvalue = StringVar()

usernamevar = Entry(root, textvariable=usernamevalue)
passvar = Entry(root, textvariable=passvalue)
usernamevar.grid(row=1, column=3)
passvar.grid(row=2, column=3)

Button(text="SUBMIT", command=gef).grid(row=3, column=2)

root.mainloop()


def gmsd():
    print("thanks for rating us to ", mas.get())
    if mas.get() >= 2:
        tmsg.showinfo(
            "rate us ", "thanks for rating us plees rate us on the google playstor")
    else:
        tmsg.showinfo("not rate", "we will fix your problsnm soon")


root = Tk()
root.geometry("400x300")

root.title("rastorent")

mas = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=2)
mas.pack()

Button(root, text="submit", command=gmsd).pack()

root.mainloop()
