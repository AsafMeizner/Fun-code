from random import randint
import pygame
import ctypes
import os

exit = False

# Settings
user32 = ctypes.windll.user32
SIZE1 = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
SIZE = width, height = SIZE1
BG_COLOR = (0, 0, 0)  
fullscreen = True 

# if fullscreen:
#     DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     pygame.mouse.set_visible(False)

#     user32 = ctypes.windll.user32
#     screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
logo_path = str(f"{os.path.dirname(__file__)}/assets/dvd/logo.png")
logo = pygame.image.load(logo_path)
# logo = pygame.image.load("C:/Users/User/Desktop/code/fun code/Fun-code/Done_code/assets/dvd/logo.png")
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


while exit == False:
    screen.fill(BG_COLOR)
    if (x + img_size[0] >= width) or (x <= 0):
        x_speed = -x_speed
    if (y + img_size[1] >= height) or (y <= 0):
        y_speed = -y_speed

    x += x_speed
    y += y_speed
    move(x, y)

    # checking if keydown event happened or not
    # if event.type == pygame.KEYDOWN:
               
    #     if event.key == pygame.K_RIGHT:
    #         print("Speed increased")
    #         x_speed += 0.5
    #         y_speed += 0.5
    #     if event.key == pygame.K_LEFT:
    #         print("Speed decreased")
    #         x_speed -= 0.5
    #         y_speed -= 0.5
    #     if event.key == pygame.K_ESCAPE:
    #         print("exitig")
    #         exit = True

    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

pygame.quit()