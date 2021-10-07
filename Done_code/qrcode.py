from tkinter import *
from tkinter import messagebox
import pyqrcode
from tkinter import colorchooser  
  

def show_qr_window(color):                    
    ws = Toplevel()
    color_code = color
    ws.config(bg = color_code)
    def generate_QR():
        if len(user_input.get())!=0 :
            global qr,img
            qr = pyqrcode.create(user_input.get())
            img = BitmapImage(data = qr.xbm(scale=8))
        else:
            messagebox.showwarning('warning', 'All Fields are Required!')
        try:
            display_code()
        except:
            pass

    def display_code():
        global img
        img_lbl.config(image = img)
        output.config(text="QR code of " + user_input.get())


    lbl = Label(
        ws,
        text="Enter message or URL",
        bg=color_code
        )
    lbl.pack()

    user_input = StringVar()
    entry = Entry(
        ws,
        textvariable = user_input
        )
    entry.pack(padx=10)


    button = Button(
        ws,
        text = "generate_QR",
        width=15,
        command = generate_QR
        )
    button.pack(pady=10)

    img_lbl = Label(
        ws,
        bg=color_code)
    img_lbl.pack()
    output = Label(
        ws,
        text="",
        bg=color_code
        )
    output.pack()
    
    ws.mainloop()

def choose_color():
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    if color_code != None:
        show_qr_window(color_code[1])
 
root = Tk()
button = Button(root, text = "Select color",
                   command = choose_color)
button.pack()
root.mainloop()