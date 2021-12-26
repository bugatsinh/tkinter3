from tkinter import *
root = Tk()
root.geometry("733x566")
root.title("Pychame")


def myFunc():
    print("I am a very funney function")


# use this to creat known drop down menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myFunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

manemenu = Menu(root)

m1 = Menu(manemenu, tearoff=0)
m1.add_command(label="save", command=myFunc)
m1.add_command(label="save as", command=myFunc)
m1.add_separator()
m1.add_command(label="new project", command=myFunc)
m1.add_command(label="print", command=myFunc)
root.config(menu=manemenu)
manemenu.add_cascade(label="File", menu=m1)

m2 = Menu(manemenu, tearoff=0)
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="copy", command=myFunc)
m2.add_separator()
m2.add_command(label="past", command=myFunc)
m2.add_command(label="find", command=myFunc)
root.config(menu=manemenu)
manemenu.add_cascade(label="Edit1", menu=m2)

root.mainloop()
