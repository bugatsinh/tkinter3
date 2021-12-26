from tkinter import *

root = Tk()
root.geometry("655x444")
root.title("shreshth - Title of my gui")
root.wm_iconbitmap("1.ico")
root.config(background="gray")

Width = root.winfo_screenwidth()
hight = root.winfo_screenheight()

print(f"{Width}x{hight}")


root.mainloop()
