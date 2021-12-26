from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("455x233")
root.title('radio Button')

def order():
    print("order is done")
    tmsg.showinfo("order resived",f"we have reseved youur order {var.get()}, thanks for order")

var = StringVar()
var.set('radio')
Label(root, text='what wound you like to have sir',
    font='lucida 19 bold italic', justify=LEFT, padx=14).pack()

radio = Radiobutton(root, text="Dosa", padx=12, variable=var,value="Dosa").pack(anchor=W)
radio = Radiobutton(root, text="idly", padx=12, variable=var,value="idly").pack(anchor=W)
radio = Radiobutton(root, text="paratha", padx=12, variable=var,value="paratha").pack(anchor=W)
radio = Radiobutton(root, text="samisa", padx=12, variable=var,value="samisa").pack(anchor=W)

Button(text="Order now",command=order).pack()
root.mainloop()
