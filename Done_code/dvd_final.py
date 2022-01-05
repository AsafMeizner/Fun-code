#dvd screensaver that runs when the computer is idle for a certain amount of time

from ctypes import Structure, windll, c_uint, sizeof, byref #afktime imports

#visual imports
from random import randint
import pygame
import ctypes
#visual imports

exit = False

# Settings
user32 = ctypes.windll.user32
SIZE1 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
SIZE = width, height = SIZE1
BG_COLOR = (0, 0, 0)  
fullscreen = True 
#settings

#afktime
class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0
#adktime

#main loop
while True:
    print(get_idle_duration()) #print afktime
    if get_idle_duration >= 10: #if afktime is greater than 10 seconds
        print("You are idle")

        #visual portion
        logo = pygame.image.load("C:/Users/User/Desktop/all_code/Fun_code/Done_code/assets/logo.png")
        logo = pygame.transform.scale(logo, (100, 50))
        clock = pygame.time.Clock()
        img_size = logo.get_rect().size
        screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption('DVD Corner')

        if fullscreen:
            DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            pygame.mouse.set_visible(False)


        x = randint(50, width-60)
        y = randint(50, height-60)
        x_speed = 2.5
        y_speed = 2.5


        def move(x, y):
            screen.blit(logo, (x, y))


        while exit == False or get_idle_duration >= 10:
            screen.fill(BG_COLOR)
            if (x + img_size[0] >= width) or (x <= 0):
                x_speed = -x_speed
            if (y + img_size[1] >= height) or (y <= 0):
                y_speed = -y_speed

            x += x_speed
            y += y_speed
            move(x, y)

            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True


        pygame.quit()
        #visual portion


#main loop
