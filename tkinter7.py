from tkinter import *


def getwall():
    print(f"the value of user name is {uservelue.get()}")
    print(f"the value of pasword is {passvelue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root, text="user name")
pasword = Label(root, text="pasword")
user.grid()
pasword.grid(row=1)

# variable classer in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

uservelue = StringVar()
passvelue = StringVar()

usesEnter = Entry(root, textvariable=uservelue)
passEnter = Entry(root, textvariable=passvelue)

usesEnter.grid(row=0, column=1)
passEnter.grid(row=1, column=1)

Button(text="submite", command=getwall).grid()

root.mainloop()
