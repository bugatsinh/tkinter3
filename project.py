from tkinter import *
from tkinter import messagebox
from typing import MutableSequence
card_info = {
    "895231645213": {"name":"shreshth","amount": 59688675585, "expiry_date": "2036", "pin": "8954"},

    "625555145585": {"name":"Rishab ","amount": 59688685655, "expiry_date": "2036", "pin": "306"},
    "547475948175": {"name":"Ayush ","amount": 59688545214, "expiry_date": "2036", "pin": "302"},
    "985217555465": {"name":"Shibe ","amount": 59688625628, "expiry_date": "2036", "pin": "506"},
    "894584749994": {"name":"Shubham ","amount": 59688625628, "expiry_date": "2036", "pin": "908"},
    "866588866656": {"name":"Dhairya ","amount": 59688625628, "expiry_date": "2036", "pin": "110"},
}
    
class varify(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.geometry("300x100")
        self.maxsize(300,100)
        self.minsize(300,100)
        self.iconbitmap("1.ico")
    def card_varify(self):
        Label(text="Entir_your_card_number_pleas", bg="orange").grid(row=1,column=1,)
        adv = StringVar()
        self.ast = Entry(textvariable=adv,bg="orange")
        self.ast.grid(row=1, column=2)
        Button(text="submit", command=self.ok).grid(row=2, column=2)
    def ok(self):
        try:
            psj = messagebox.showinfo("name", f"walcome {card_info[self.ast.get()]['name']}")
            self.destroy()
            sv = pin()
            sv.PIN()
            sv.mainloop()
        except Exception:
            messagebox.showerror("not_name_found", "sorry your Acount is not found")
            self.destroy()

class pin(varify):
    def __init__(self) -> None:
        super().__init__()
    def PIN(self):
        Label(text="pleas_Entir_your_pin", bg="orange").grid(row=1,column=1,)
        adv = StringVar()
        self.ass = Entry(textvariable=adv,bg="orange")
        self.ass.grid(row=1, column=2)
        Button(text="submit", command=self.place).grid(row=2, column=2)
    def place(self):
        for i in range(4):
            i -= 1
            if i == 1 and pin != card_info[self.ast.get()]['pin']:
                print("your pin is  blocked")
                exit()

            elif pin == card_info[self.ast.get()]["pin"]:
                print("your pin is varified: ")
                break

            else:
                print("your pin is not found")
    
        
st = varify()
st.card_varify()
st.mainloop()
