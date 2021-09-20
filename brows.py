# Import the required Libraries
from tkinter import *
from tkinter import ttk, filedialog
from tkinter.filedialog import askopenfile

# Create an instance of tkinter frame
win = Tk()

# Set the geometry of tkinter frame
win.geometry("700x350")

def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('*.png', '*.jpeg')])
   if file:
        print(file)

        word_list = ["<_io.TextIOWrapper name='", "' mode='r' encoding='cp1255'>"]

        for word in word_list:
            if word in file:

                query = file
                stopwords = ['<_io.TextIOWrapper name=']
                querywords = query.split()

                resultwords  = [word for word in querywords if word.lower() not in stopwords]
                result11 = ' '.join(resultwords)

                print(result11)

                file.close()

  

# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

win.mainloop()