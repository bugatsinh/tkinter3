from tkinter import *

root = Tk()

root.geometry("644x344")

def getwell():
    print("it works")
# heading
Label(root, text="welcome to shreshht travels"
      ,font="comicsansms 13 bold",pady=15).grid(row=0, column=3)

# text for our form
name = Label(root, text="name")
phone = Label(root, text="phone")
gender = Label(root, text="gender")
Emergensy = Label(root, text="Emergensy_contect")
payment_Mode = Label(root, text="payment_Mode")

#pack the text by grid for our frogram
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
Emergensy.grid(row=4, column=2)
payment_Mode.grid(row=5, column=2)

# tkinter viriable for storing variable
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
Emergensyvalue=StringVar()
payment_Modevalue=StringVar()
foodscrvesvalue=IntVar()


# Entrys for your form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergensyentry = Entry(root, textvariable=Emergensyvalue)
payment_modentry = Entry(root, textvariable=payment_Modevalue)

#packing the progeram
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergensyentry.grid(row=4,column=3)
payment_modentry.grid(row=5,column=3)

# chack button and packing it
foodscrves = Checkbutton(text="want to pry book your meals",variable=foodscrvesvalue)
foodscrves.grid(row=6,column=3)

Button(text="submit to harry travels", command=getwell).grid(row=7,column=3)

root.mainloop()
