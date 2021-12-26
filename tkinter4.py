from tkinter import *
root = Tk()

root.geometry("744x433")
root.title("My GUI with Harry")


# importent Label  option

# Text= adds the text
# bd = Background
# fg = forground
# 1. font = sets the font
# 2. font=("comicsanse 12 bold italic"))
# pedx = x pesing
# pedy = y pesing
# relief = border styling = SUNKEN, RAISED, GROOVE, RIDE

titel_label = Label(text='''
\nAbdul Rashid Salim Salman Khan (Hindi: [səlˈmɑːn xɑːn];
\n27 December 1965)[4] is an Indian actor, film producer,
\nsinger, painter[5] and television personality who works
\nin Hindi films. In a film career spanning over thirty years,
\nKhan has received numerous awards, including two National 
\nFilm Awards as a film producer, and two Filmfare Awards for
\nacting.[6] He is cited in the media as one of the most
\ncommercially successful actors of Indian cinema.[7][8] Forbes
\nincluded him in their 2015 list of Top-Paid 100 Celebrity
\nEntertainers in the world; Khan tied with Amitabh Bachchan
\nfor No. 71 on the list, both with earnings of $33.5 million.
\n[9][10] According to the Forbes 2018 list of Top-Paid 100
\nCelebrity Entertainers in world, Khan was the highest-ranked
\nIndian with 82nd rank with earnings of $37.7 million.[11][12]
\nHe is also known as the host of the reality show, Bigg Boss
\nsince 2010.[13]''', bg="lightgreen", fg="red", padx=10, pady=10, font="comicsanse 12 bold italic", relief=SUNKEN)

# imporeny pack option
# ancher
# side = top, botum, left right
# fill
# pedx
# pedy


# two ways to dow it FIRST IS
# titel_label.pack(anchor=NW)

# SECOND IS
# titel_label.pack(side= BOTTOM,anchor="se",fill=X)
titel_label.pack(side=BOTTOM, anchor="se", fill=Y, padx=34, pady=34)

root.mainloop()
