from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("slide tutoril")

def getdoller():
    print(f"we have credited {myslider2.get()} doller to your bank account")
    tmsg.showinfo("amount crateed",f"we have credited {myslider2.get()} doller to your bank account")
# myslider = Scale(root, from_=0, to=455)
# myslider.pack()
Label(root,text="How amy doller do you want").pack()
myslider2 = Scale(root, from_=0, to=100,orient=HORIZONTAL,tickinterval=20)
myslider2.set(34)
myslider2.pack()
Button(root, text="Get Dollers!",pady=5, command=getdoller).pack()

root.mainloop()