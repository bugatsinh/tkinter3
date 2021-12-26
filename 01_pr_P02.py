from time import time
init = int(time())
from tkinter import *
import datetime

root = Tk()


class Globel:
    Scrollba = Scrollbar(root)
    root.geometry("744x433")
    root.minsize(700, 550)
    # root.maxsize(1000,550)
    root.title("this is by shrehsht")

    f1 = Label(text=datetime.datetime.now(), bg="black", fg="red",
               font="comicsanse 12 bold italic", relief=SUNKEN)
    f1.pack(side=RIGHT, anchor="nw")

    Hedline = Label(text="this the news program", bg="gray",
                    fg="white", font="comicsanse 12 bold italic", relief=SUNKEN)
    Hedline.pack(side=TOP, anchor=N)


class Local(Globel):
    phot = PhotoImage(file="0.png")
    a = Label(image=phot)
    a.pack(anchor=NW)
    titel = Label(text="""(CNN)Former President Donald Trump shows every sign of aspiring to
            a new presidency that would shake America's democracy to its core. But
            a highly charged congressional hearing Tuesday will underscore the institutional
            and political wreckage still smoldering in the wake of his first White House term
            Gen. Mark Milley, the chairman of the Joint Chiefs of Staff, is scheduled to appear
            before the Senate Armed Services Committee along with other senior Pentagon officials
            to testify over the chaotic withdrawal from Afghanistan. This issue is crucially important
            by itself, not least because of the deaths of 13 US service personnel in Kabul in a suicide
            attack and the killing of Afghan civilians -- including seven children -- in a botched US drone
            strike last month. Milley, Defense Secretary Lloyd Austin and Gen. Frank McKenzie, the head of
            Central Command, are expected to face a grilling on the much-criticized planning and execution
            of the end of America's longest war.""", bg="orange", fg="black", font="comicsanse 12 bold italic", relief=SUNKEN)
    titel.pack(side=TOP, anchor="nw", padx=150, fill=X)
    photos = PhotoImage(file="1.png")
    a = Label(image=photos)
    a.pack(anchor=NW)
    titel = Label(text="""(CNN)Former President Donald Trump shows every sign of aspiring to
            a new presidency that would shake America's democracy to its core. But
            a highly charged congressional hearing Tuesday will underscore the institutional
            and political wreckage still smoldering in the wake of his first White House term
            Gen. Mark Milley, the chairman of the Joint Chiefs of Staff, is scheduled to appear
            before the Senate Armed Services Committee along with other senior Pentagon officials
            to testify over the chaotic withdrawal from Afghanistan. This issue is crucially important
            by itself, not least because of the deaths of 13 US service personnel in Kabul in a suicide
            attack and the killing of Afghan civilians -- including seven children -- in a botched US drone
            strike last month. Milley, Defense Secretary Lloyd Austin and Gen. Frank McKenzie, the head of
            Central Command, are expected to face a grilling on the much-criticized planning and execution
            of the end of America's longest war.""", bg="orange", fg="black", font="comicsanse 12 bold italic", relief=SUNKEN)
    titel.pack(side=TOP, anchor=NW, padx=150, fill=X)
    photoes = PhotoImage(file="2.png")
    a = Label(image=photoes)
    a.pack(side=TOP, anchor=NW)
    titel = Label(text="""(CNN)Former President Donald Trump shows every sign of aspiring to
            a new presidency that would shake America's democracy to its core. But
            a highly charged congressional hearing Tuesday will underscore the institutional
            and political wreckage still smoldering in the wake of his first White House term
            Gen. Mark Milley, the chairman of the Joint Chiefs of Staff, is scheduled to appear
            before the Senate Armed Services Committee along with other senior Pentagon officials
            to testify over the chaotic withdrawal from Afghanistan. This issue is crucially important
            by itself, not least because of the deaths of 13 US service personnel in Kabul in a suicide
            attack and the killing of Afghan civilians -- including seven children -- in a botched US drone
            strike last month. Milley, Defense Secretary Lloyd Austin and Gen. Frank McKenzie, the head of
            Central Command, are expected to face a grilling on the much-criticized planning and execution
            of the end of America's longest war.""", bg="orange", fg="black", font="comicsanse 12 bold italic", relief=SUNKEN)
    titel.pack(side=TOP, anchor=NW, padx=150, fill=X)
    

    root.mainloop()
# print(init-time())

# L = Local()

# import datetime
# from tkinter import *


# def HelloW():
#         a = input("Enter your name: ")
#         if a == "harry" or a == "Harry":
#                 print("thanks for teaching us sir")

#         print("Welcomw to our program",a)
# def Hello():
#         print(datetime.datetime.now())
# def hello():
#         a = (datetime.datetime.now().minute)
#         b =(datetime.datetime.now().hour)
#         c =(datetime.datetime.now().second)
#         print(f"the time is {b}:{a}:{c}")


# root = Tk()

# root.geometry("400x333")
# root.minsize(300,333)
# root.maxsize(400,333)

# B1 = Frame(root, borderwidth=20,bg="orange",relief=SUNKEN)
# B1.pack(side=TOP,anchor=N)

# b1 = Button(B1, text="DATE AND TIME",command=Hello)
# b1.pack()

# B2 = Frame(root, borderwidth=20,bg="orange",relief=SUNKEN,)
# B2.pack(side=TOP,anchor=N)

# b2 = Button(B2, text="TIME",command=hello)
# b2.pack()

# B3 = Frame(root, borderwidth=20,bg="orange",relief=SUNKEN)
# B3.pack(side=TOP,anchor=N)

# b3 = Button(B3, text="NAME",command=HelloW)
# b3.pack()


# root.mainloop()

# from tkinter import *

# root = Tk()

# def frd():
#         widt = widthvalue.get()
#         high = hightvalue.get()
#         root.geometry(f"{widt}x{high}")
# def get():
#         def frd():
#                 widt = widthvalue.get()
#                 high = hightvalue.get()
#                 root.geometry(f"{widt}x{high}")


#         def gdf():
#                 widt = widthvalue.get()
#                 high = hightvalue.get()
#                 Button(root, text=f"if you weite \nthe width is {widt}, and hight is {high}\nclick hear \nother wise click on no",command=frd).grid(row=4,column=2)
#                 Button(root, text="no",command=get).grid(row=5,column=2)
#         root.geometry("290x190")
#         widthvalue = StringVar()
#         hightvalue = StringVar()

#         widthver = Entry(root, textvariable=widthvalue)
#         hightver = Entry(root, textvariable=hightvalue)
#         widthver.grid(row=1,column=3)
#         hightver.grid(row=2,column=3)

#         Button(root, text="appely",command=gdf).grid(row=3,column=2)

# def gdf():
#         widt = widthvalue.get()
#         high = hightvalue.get()
#         Button(root, text=f"if you weite \nthe width is {widt}, and hight is {high}\nclick hear \nother wise click on no",command=frd).grid(row=4,column=2)
#         Button(root, text="no",command=get).grid(row=5,column=2)


# root.geometry("290x190")
# root.title("Exersise 2")

# width = Label(root, text="width of the screen", font="comicsansms 13 bold italic")
# hight = Label(root, text="hight of the screen", font= "comicsansms 13 bold italic")
# width.grid(row=1,column=2)
# hight.grid(row=2,column=2)

# widthvalue = StringVar()
# hightvalue = StringVar()

# widthver = Entry(root, textvariable=widthvalue)
# hightver = Entry(root, textvariable=hightvalue)
# widthver.grid(row=1,column=3)
# hightver.grid(row=2,column=3)


# Button(root, text="appely",command=gdf).grid(row=3,column=2)

# root.mainloop()
# from tkinter import *
# import tkinter.messagebox as tmsg
# root = Tk()
# root.geometry("733x566")
# root.title("Pychame")


# def who():
#         print("I am a very funney function")
#         # it return only ok
#         a = tmsg.showerror(title="Error",message="STT Errir\n 0x154215bf")
#         #it return retry and calsel
#         b = tmsg.askretrycancel("AFFs", "your net work is slow")
#         if b == True and a==True:
#                 print("there is any error is occure", a)
#         else:
#                 print("all fine")
# def why():
#         print("why are you dowing it")
#         c = tmsg.askyesno("who are you","you are harry")
#         if c==True:
#                 print("welcone sir to our program")
#         else:
#                 print("dont come hear agane")


# manemenu = Menu(root)
# m1 = Menu(manemenu,tearoff=0)
# m1.add_command(label="who",command=who)
# m1.add_command(label="why",command=why)
# root.config(menu=manemenu)

# manemenu.add_cascade(label="help",menu=m1)

# root.mainloop()
from pygame import *


