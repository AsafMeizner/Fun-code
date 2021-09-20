import numpy as np
from PIL import ImageGrab
import cv2
from directKeys import PressAndReleaseKey, A, S, D, F, queryMousePosition
import time

def screen_record(box): 
    last_time = time.time()
    while(True):
        #printscreen =  np.array(ImageGrab.grab(bbox=(755,560, 1150,600)))
        printscreen =  np.array(ImageGrab.grab(box))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def pianoTilesHack(numberOfPresses, box):
    pressed = 0
    while(pressed != numberOfPresses):
        printscreen =  np.array(ImageGrab.grab(box))
        pressed = pressed + clickOneBlackSquare(printscreen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

def clickOneBlackSquare(img):
    for x in range(4):
        #calculate pixel position in square
        x_pos = 6 + (x * 99)

        #check if that pixel is black
        if np.any(img[1, x_pos] == [17, 17, 17]):
            if(x == 0):
                PressAndReleaseKey(A)
            elif(x == 1):
                PressAndReleaseKey(S)
            elif(x == 2):
                PressAndReleaseKey(D)
            else:
                PressAndReleaseKey(F)
            return 1
    return 0



#wait untill the mouse goes to the next screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        break

print("Mouse On Second Monitor Detected - Starting Program")
first=(753,570, 1151,719)
box1_half=(753,495, 1151,719)
second=(753,421, 1151,719)
box2_half=(753,346, 1151,719)
third=(753,274, 1151,719)
time.sleep(5)

a0=(753,644, 1151,719)
a1=(753,570, 1151,719)
a2=(753,510, 1151,719)

#classic 30 blocks timing
while(True):
    pianoTilesHack(1, first)
    pianoTilesHack(1, box1_half)
    pianoTilesHack(1, second)
    pianoTilesHack(1, box2_half)
    pianoTilesHack(1, third)
    time.sleep(.53)

##arcade
#pianoTilesHack(1, a1)
#time.sleep(.2)

#for x in range(40):
#    pianoTilesHack(1, a0)
#    time.sleep(.3)

#for x in range(59):
#    pianoTilesHack(1, a1)
#    time.sleep(.2)

#while(True):
#    pianoTilesHack(1, first)
#    pianoTilesHack(1, box1_half)
#    pianoTilesHack(1, second)
#    pianoTilesHack(1, box2_half)
#    pianoTilesHack(1, third)
#    time.sleep(.53)
