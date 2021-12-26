from tkinter import *

def marks():
      mark = 0
      if itv.get() == "namuns":
            mark=mark+2
      print(mark)
      
root = Tk()

Label(root, text='''
located in france, it is a UNESCO world heritage site.
its hallways are worth seeing. it was the hunting lodge
of king Louis XIV.
      
      
      ''', font="comicsanse 18 bold ").grid(row=1,column=1)
st = StringVar()
itv = Entry(root, textvariable=st)
itv.grid(row=1, column=2)
Button(root, text="Submmit", command=marks).grid(row=1,column=3)


Label(root, text='''
it is an important sity of turkey. one half of this city
lies in Europe and the other half lies in asia. important
tourist spots are the Bosporus Stait, Hagia Sophai,
Topkapi palace and Grand Bzar''',font="comicsanse 18 bold ").grid(row=2,column=1)
sr = StringVar()
itr = Entry(root, textvariable=sr)
itr.grid(row=2, column=2)
Button(root, text="Submmit", command=marks).grid(row=2,column=3)


root.mainloop()