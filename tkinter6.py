from tkinter import *

root = Tk()

root.geometry("655x333")

def Hello():
    print("hellow tkinter Button")

def Name():
    print("MY name is shreshth")

frame = Frame(root, borderwidth=6, bg="green", relief=SUNKEN)
frame.pack(side=LEFT, anchor=NW)

b1 = Button(frame, fg="orange", text="print now",command=Hello)
b1.pack(side=LEFT,padx=24)

b2 = Button(frame, fg="orange", text="print now",command=Hello)
b2.pack(side=LEFT,padx=24)

b3 = Button(frame, fg="orange", text="Tell me name now",command=Name)
b3.pack(side=LEFT,padx=24)

b4 = Button(frame, fg="orange", text="print now",command=Hello)
b4.pack(side=LEFT,padx=24)

b5 = Button(frame, fg="orange", text="print now",command=Hello)
b5.pack(side=LEFT,padx=24)

root.mainloop()
