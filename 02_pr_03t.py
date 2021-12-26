from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import asksaveasfilename
import os


class atv(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("700x800")
        self.minsize(200, 120)
        self.title("GYAAN")
        self.wm_iconbitmap("1.ico")

    def tack(self):
        with open("pass.txt", "a") as f:
            f.write(self.ev.get())
        self.destroy()

    def Makepass(self):
        self.tsv = StringVar()
        self.ev = Entry(self, textvariable=self.tsv)
        self.ev.grid(row=1, column=3)
        Button(self, text="submit", command=self.tack).grid(row=1, column=4)

    def chackpass(self):
        self.asv = Label(
            self, text="if you want to make a pasword so click hear")
        self.asv.grid(row=1, column=1)
        Button(self, text="pasword", command=self.Makepass).grid(row=1, column=2)


class sta(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("700x800")
        self.minsize(200, 120)
        self.title("GYAAN")
        self.wm_iconbitmap("1.ico")

    def svg(self):
        self.destroy()

    def wrong(self):
        Label(self, text="wrong password").grid(row=3, column=2)

    def gtv(self):
        with open("pass.txt", "r") as f:
            ast = f.read()
        print(ast)
        self.pasv = ast
        self.ac = self.var.get()
        # ac = int(ac)
        print(self.ac)
        print(self.pasv)
        if self.ac == self.pasv:
            avs = Button(text="Submit", command=self.svg)
            avs.grid(row=2, column=2)
        else:
            avc = Button(text="Submit", command=self.wrong)
            avc.grid(row=2, column=2)

    def passv(self):
        Label(self, text="ENTER PASSWORD").grid(row=1, column=1)
        self.var = StringVar()
        value = Entry(self, textvariable=self.var)
        value.grid(row=1, column=2)
        Button(text="if the pasword is correct",
               command=self.gtv).grid(row=4, column=3)


class scg(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("700x800")
        self.minsize(200, 120)
        self.title("GYAAN")
        self.wm_iconbitmap("1.ico")

    def saveFile(self):
        global file
        if file == None:
            file = asksaveasfilename(initialfile="Untitele.txt", defaultextension=".txt", filetypes=[
                                    ("All Files", "*.*"), ("Text Documents", "*.txt")])
            if file == "":
                file = None
            else:
                # save as a file
                f = open(file, "w")
                f.write(self.get(1.0, END))
                f.close()

                self.title(os.path.basename(file) + " - GIYAN")
                print("file sve")
        else:
            # save the file
            f = open(file, "w")
            f.write(self.get(1.0, END))
            f.close()

    def quitApp(self):
        self.destroy()

    def copy(self):
        # global Textarea
        self.value.event_generate("<<Copy>>")

    def cut(self):
        # global Textarea
        self.value.event_generate("<<Cut>>")

    def paste(self):
        # global Textarea
        self.value.event_generate("<<Paste>>")

    def chang_pass(self):
        self.vay = StringVar()
        valu = Entry(self, textvariable=self.vay)
        valu.grid(row=1, column=11)
        self.pasv = self.vay.get()

    def about():
        showinfo("notepade", "notepad it is a notepad make by shrehsth")

    def searchbox(self) -> None:

        var = StringVar()
        self.value = Entry(self, textvariable=var,
                           font="lucida 13 bold italic", bg="yellow")
        self.value.grid(row=1, column=3)
        Button(self, text="search", bg="gray",
               font="lucida 13 bold italic").grid(row=1, column=4)
        self.config(bg="green")
        self.config(bg="lightgreen")
        self.wm_iconbitmap("1.ico")
    #     Button(self, text="submit", command=self.SBM).grid(row=6, column=3)

    def menu(self):
        global Textarea
        Textarea = Text(self, font="lucida 13")
        file = None
        # Textarea.grid(row=6, column=8)
        manemenu = Menu(self)
        mmenu = Menu(manemenu, tearoff=0)
        mmenu.add_command(label="copy", command=self.copy)
        mmenu.add_command(label="past", command=self.paste)
        mmenu.add_separator()
        mmenu.add_command(label="cut", command=self.cut)
        mmenu.add_command(label="quitApp", command=self.quitApp)
        mmenu.add_command(label="saveFile", command=self.saveFile)
        manemenu.add_cascade(menu=mmenu, label="EDIT")

        pasv = Menu(manemenu, tearoff=0)
        pasv.add_command(label="change_pass", command=self.chang_pass)
        manemenu.add_cascade(label="password", menu=pasv)
        self.config(menu=manemenu)


if __name__ == "__main__":
    scr = atv()
    scr.chackpass()
    scr.mainloop()
    screen = sta()
    screen.passv()
    screen.mainloop()
    if screen.ac == screen.pasv:
        sav = scg()
        sav.searchbox()
        sav.menu()
        sav.mainloop()
