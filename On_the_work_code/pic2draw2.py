import cv2

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
        
        image = cv2.imread(file)

        file.close()

  

# Add a Label widget
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray.png", gray_image)
inverted_image = 255 - gray_image
cv2.imwrite("inv.png", inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imwrite("blur.png", blurred)
inverted_blurred = 255 - blurred
cv2.imwrite("invblur.png", inverted_blurred)
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imwrite("Sketch.png", pencil_sketch)

win.mainloop()