from tkinter import *

root = Tk()

canves_width = 800
canves_hight = 400

root.title("shreshth ka Gui")

root.geometry(f"{canves_width}x{canves_hight}")
can_widget = Canvas(root, width=canves_width, height=canves_hight)
can_widget.pack()

# x1 = width of base
# y1 = hight of left hend side
# the ling goes from the line poit x1,y1 to x2 y2
can_widget.create_line(0, 0, 800, 400)
can_widget.create_line(0, 400, 800, 0)

# to crieat a rectange spacify paramiter in this order = cordinate to top left and cordinate of bottum right
can_widget.create_rectangle(3, 5, 700, 300, fill="orange")

can_widget.create_text(200, 200, text="python is the best",
                       font=" comicsansms 13 bold italic")

can_widget.create_oval(300, 200, 400, 400)
root.mainloop()
