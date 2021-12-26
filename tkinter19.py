# from tkinter import *


# class GUI(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("744x377")

#     def status(self):
#         self.var = StringVar()
#         self.var.set("Ready")
#         self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor=W)
#         self.statusbar.pack(side=BOTTOM, fill=X)

#     def click(self):
#         print("Buttin is clicked")

#     def creatbuttom(self, inptext):
#         Button(text=inptext, command=self.click).pack()


# if __name__ == "__main__":
#     window = GUI()
#     window.creatbuttom("who are you")
#     window.status()
#     window.mainloop()

# root == self == window
from tkinter import *
import tkinter.messagebox as tmsg

class clicke(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")

    def ipBtn(self):
        asr = tmsg.askquestion(title="question", message="Enter your name")
        if asr == "yes":
            self.var = StringVar()
            self.value = Entry(self, textvariable= self.var)
            self.value.pack()
        
    def submit(self):
        if self.var.get() == "":
            tmsg.askokcancel(title="name is correct ", message=f"plees enter somthing")
        else:
            tmsg.askokcancel(title="name is correct ", message=f"this is name your {self.var.get()}")

    def creatButton(self, name):
        a = Button(text="click", command=self.ipBtn)
        a.pack()
        
        Button(text="Submnit", command=self.submit).pack()


if __name__ == "__main__":
    window = clicke()
    window.creatButton("fgtry")
    window.mainloop()
