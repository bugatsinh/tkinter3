from tkinter import *
from PIL import Image, ImageTk
import os

r_root = Tk()
r_root.geometry("955x940")
# a = os.listdir("C:/Users/SHRESHTH/Desktop/New folder (3)")
# b = len(a)
# print(b)
# photo = PhotoImage(file="WhatsApp Image.jpg")
img = os.path.join("C:/Users/SHRESHTH/Desktop/New folder (2)/2.png")

image = Image.open(img)
photo = ImageTk.PhotoImage(image)
shreshth = Label(image=photo)
shreshth.pack()

r_root.mainloop()
