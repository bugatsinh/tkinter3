from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "ERROR"

        scvalue.set(value)
        screen.update()

    elif text == 'c':
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x970")
root.title("calculator by shreshth")
root.wm_iconbitmap("1.ico")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=9, pady=11)
f1 = Frame(root, background="orange")
f1.pack()
b1 = Button(f1, text="9", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=30, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="8", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="7", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="/", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

f1 = Frame(root, background="orange")
f1.pack()
b1 = Button(f1, text="6", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="5", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="4", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="+", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

f1 = Frame(root, background="orange")
f1.pack()
b1 = Button(f1, text="3", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="2", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="1", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="c", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=20, pady=12)
b1.bind("<Button-1>", click)




f1 = Frame(root, background="orange")
f1.pack()
b1 = Button(f1, text="0", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=5, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="-", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=5, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="*", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=5, pady=12)
b1.bind("<Button-1>", click)
b1 = Button(f1, text="%", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=5, pady=12)
b1.bind("<Button-1>", click)

b1 = Button(f1, text="=", padx=27, pady=18, font="lucida 35 bold")
b1.pack(side=LEFT, padx=5, pady=12)
b1.bind("<Button-1>", click)

root.mainloop()
