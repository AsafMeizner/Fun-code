from keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np

from tkinter import *
from tkinter import messagebox
Tk().wm_withdraw() #to hide the main window

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("tenserflow\models\me_and_nir\keras_model.h5", compile=False)

# Load the labels
class_names = open("tenserflow\models\me_and_nir\labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(0)

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()

    # Resize the raw image into (224-height,224-width) pixels
    try:
        image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    except Exception as e:
        print(str(e))

    # Show the image in a window
    cv2.imshow("Webcam Image", image)

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    text = "Class: " + class_name[2:] + " | Confidence Score: " + str(np.round(confidence_score * 100))[:-2] + "%"
    cordinates = (0,0)

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Listen to the keyboard for presses.
    keyboard_input = cv2.waitKey(1)

    # 27 is the ASCII for the esc key on your keyboard.
    if keyboard_input == 27:
        break
    

    messagebox.showinfo('Continue','OK')

camera.release()
cv2.destroyAllWindows()
