# from tkinter import *
# from tkinter import messagebox
 
# messagebox = Tk()

# messagebox.geometry("500x100+300+300")
# # messagebox.showerror("Title", "Message")

# messagebox.mainloop()

from tkinter import *
from tkinter import messagebox
import os
import asyncio

def top():
    if entry1.get() == "ASAF1511":
       log.destroy()
       root.deiconify()
       os._exit(0)
    else:
        while True:
            messagebox.showerror("error", "F U")
            messagebox.showinfo("my message","F U")
            messagebox.showwarning("warning", "F U" ) 


root = Tk()
root.geometry("400x400")

log = Toplevel(root)
log.geometry("200x200")


label1 = Label(log, text="password")
entry1 = Entry(log)
button1 = Button(log, text="login", command=top)

label1.pack()
entry1.pack()
button1.pack(side="bottom")

lab = Label(root, text="welcome bro").pack()


root.withdraw()
root.mainloop()
