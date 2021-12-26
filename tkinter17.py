from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutoeril")
# for connecting scroolbar to a width
# 1. widget(yscrollcommand=scroollbar.set)
# scroollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

# listbox = Listbox(root,yscrollcommand=scrollbar.set)
# for i in range(344):
#     listbox.insert(END, f"Item {i}")
    
# listbox.pack(fill="both")
# scrollbar.config(command=listbox.yview)

text = Text(root, yscrollcommand=scrollbar.set)
text.pack(fill=X)
scrollbar.config(command=text.yview)

root.mainloop()
