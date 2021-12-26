from tkinter import *

root = Tk()

root.geometry("655x333")
f1=Frame(root, bg="gray",borderwidth=6 , relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2=Frame(root, bg="gray",borderwidth=6 , relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1,text="project Tkinter - pycharm",font="Helvetica 16 bold", fg="red")
l.pack(pady=142)

l = Label(f2,text="Welcome to sublime text",font="Helvetica 16 bold", fg="red")
l.pack()

root.mainloop()