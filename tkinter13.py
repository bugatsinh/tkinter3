from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")
root.title("Pychame")


def myFunc():
    print("I am a very funney function")
    
def help():
    print("I will help you")
    tmsg.showinfo("help","Shreshth will help you with this gui")

def rate():
    print("gate us")
    value = tmsg.askquestion("was your experienc good","you use this gui...was your experienc good")
    print(value)
    if value == "yes":
        msg = "grate...rate us on appstore please"
    else:
        msg = "Tell what want wrong. we call you soon"
    tmsg.showinfo("Experinse", msg)

def divya():
    ams = tmsg.askretrycancel("Divyansh sa dosti karlo","sory Divyansh nahi banaga tumahara dost")
    if ams:
        print("retry karna pa bki kuch nahi hoga")
    
    else:
        print("Bahut badiya bhai cansel kar diya varna pitta")
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

m3 = Menu(manemenu, tearoff=0)

root.config(menu=manemenu)
m3.add_command(label="Help", command=help)
m3.add_command(label="rate us", command=rate)
m3.add_command(label="bfriend divysnsh", command=divya)
manemenu.add_cascade(label="Help", menu=m3)
root.config(menu=manemenu)

root.mainloop()
