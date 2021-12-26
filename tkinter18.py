from tkinter import *

def uplode():
    statusvar.set("Busy.....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("ready Now")
root = Tk()
root.geometry("455x233")
root.title("Sctatus bar tutoeril")


statusvar = StringVar()
statusvar.set("ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN,anchor=W)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="upload", command=uplode).pack()
root.mainloop()