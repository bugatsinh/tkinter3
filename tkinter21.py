from sys import path
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile():
    global file
    root.title("untitle-notpad")
    file = None
    Textarea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        Textarea.delete(1.0, END)
        f = open(file, "r")
        Textarea.insert(1.0, f.read())


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitele.txt", defaultextension=".txt", filetypes=[
                                ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # save as a file
            f = open(file, "w")
            f.write(Textarea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("file sve")
    else:
        # save the file
        f = open(file, "w")
        f.write(Textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    Textarea.event_generate("<<Cut>>")


def copy():
    Textarea.event_generate("<<Copy>>")


def paste():
    Textarea.event_generate("<<Paste>>")


def about():
    showinfo("notepade", "notepad it is a notepad make by shrehsth")


if __name__ == "__main__":
    root = Tk()
    root.geometry("600x700")
    root.title("shreshth - notpad")
    root.wm_iconbitmap("1.ico")

    # Add text aria
    Textarea = Text(root, font="lucida 13")
    file = None
    Textarea.pack(expand=True, fill=BOTH)

    # Lets creat menu bar
    Menubar = Menu(root)
    # file menu start
    filemenu = Menu(Menubar, tearoff=0)
    # to open new file
    filemenu.add_command(label="New", command=newFile)

    # to open alrady exesting file
    filemenu.add_command(label="Open", command=openFile)

    # to save the file
    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitApp)
    Menubar.add_cascade(label="file", menu=filemenu)
    # file menu End

    # Edit menu start
    EditMenu = Menu(Menubar, tearoff=0)
    # to give a feature of cut, copy, and past
    EditMenu.add_command(label="cut", command=cut)
    EditMenu.add_command(label="copy", command=copy)
    EditMenu.add_command(label="paste", command=paste)

    Menubar.add_cascade(label="Edit", menu=EditMenu)
    # file menu End

    # help menu start
    HelpMenu = Menu(Menubar, tearoff=0)
    HelpMenu.add_command(label="adout notepad", command=about)
    Menubar.add_cascade(label="Help", menu=HelpMenu)

    # help menu End

    root.config(menu=Menubar)

    # adding scroll bar using ruls from tkinter lecture no 22
    scroll = Scrollbar(Textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=Textarea.yview)
    Textarea.config(yscrollcommand=scroll.set)

    root.mainloop()
