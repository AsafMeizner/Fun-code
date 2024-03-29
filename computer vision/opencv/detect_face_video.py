import cv2
import os


xml_path = str(f"{os.path.dirname(__file__)}/xmls/haarcascade_frontalface_default.xml")
# Load the cascade
face_cascade = cv2.CascadeClassifier(xml_path)

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # specify the font and draw the key using puttext
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,"Face",(x,y-10), font, .5,(255,0,0),1,cv2.LINE_AA)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        