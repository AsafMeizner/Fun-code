# it is  a python game in Pygame that has a 18 see though squares with outline (in a grid of 3 height by 18 width) where there are coordinates look like this 

#          A              B                C
#    -------------  -------------    -------------
#      1   2   3      1   2   3        1   2   3
#    -------------  -------------    -------------
# H  | x | x | x |  | x | x | x |    | x | x | x |
#    -------------  -------------  ---------------
# M  | x | x | x |  | x | x | x |    | x | x | x |
#    -------------  -------------   --------------
# L  | x | x | x |  | x | x | x |    | x | x | x |
#    -------------  -------------    -------------

# every couple seconds it plays a recording of a person saying the character of the cell (the 3x3 area)
# and then a recording of a person saying the height and then a recording of the number 
# then the user needs to click on the correct slot to get a point 
# and the user is timed for the amount of time from saying the coordinate to pressing it


import pygame
import os
import random
import time
import keyboard

# Initialize Pygame
pygame.init()
pygame.mixer.init()

#font
font = pygame.font.SysFont(os.path.join(os.path.dirname(__file__),"ARIAL.ttf"), 24)

# Set the cursor to an arrow
pygame.mouse.set_cursor(*pygame.cursors.arrow)

# Get the screen size
screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

# Create the window with a size of the screen size
window = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

#main menue 
def main_menu():
    exit=False

    background = pygame.image.load(os.path.join(os.path.dirname(__file__),"background2.JPG")).convert()
    background = pygame.transform.smoothscale(background, window.get_size())
    window.blit(background, (0, 0))
    pygame.display.update()
    
    #create a button
    button = pygame.Rect(0, 0, 200, 50)
    button.center = (screen_size[0] / 2, screen_size[1] / 2)
    pygame.draw.rect(window, (255, 255, 255), button)
    text = font.render("Start", True, (0, 0, 0))
    text_rect = text.get_rect(center=button.center)
    window.blit(text, text_rect)

    pygame.display.update()

    while exit != True:

        #either pressing a button on the screen on pressing s will start the game
        for event in pygame.event.get():
            if keyboard.is_pressed('q'):
                pygame.quit()
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    game()
                    exit=True
            if keyboard.is_pressed('s'):
                game()
                exit=True

# Main game loop
def game():
    # Get the screen size
    screen_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

    # Create the window with a size of the screen size
    window = pygame.display.set_mode(screen_size, pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # Create a list of all the squares, each represented by a tuple of the form (x, y)
    squares = [(x, y) for x in range(3) for y in range(9)]

    # Create a list of all the letters for the rows
    letters = ['L', 'M', 'H']
    numbers = ['1', '2', '3']
    sections = ['A', 'B', 'C']

    # Create a list of all the recordings for the letters and numbers
    letter_recordings = []
    for letter in letters:
        letter_recordings.append(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"recordings\\letter_{}.mp3".format(letter))))
    number_recordings = []
    for number in numbers:
        number_recordings.append(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"recordings\\number_{}.mp3".format(number))))
    section_recordings = []
    for section in sections:
        section_recordings.append(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"recordings\\section_{}.mp3".format(section))))

    # Create a variable to keep track of the score
    score = 0
    old_score = 0

    # Create a variable to keep track of the time
    start_time = None

    # Load the background image and scale it to the size of the window
    absolute_path = os.path.dirname(__file__)
    relative_path = "background.png"
    full_path = os.path.join(absolute_path, relative_path)
    background = pygame.image.load(full_path).convert()
    background = pygame.transform.smoothscale(background, window.get_size())

    # Define the square size as a fraction of the screen size
    square_size = 0.1

    # Get a random square
    square = random.choice(squares)

    # Draw the background
    window.blit(background, (0, 0))

    while True:
        # Get a random square
        square = random.choice(squares)

        time.sleep(1)
        # Play the recording for the section of the square
        section_recordings[square[0]].play()
        time.sleep(1)
        # Play the recording for the letter of the square
        letter_recordings[square[1] % 2].play()
        time.sleep(1)
        # Play the recording for the number of the square
        number_recordings[square[1] // 3].play()

        # Set the start time
        start_time = pygame.time.get_ticks()
        
        # # Draw the background
        window.blit(background, (0, 0))
        time.sleep(0.2)

        # Draw the 9 squares on each sections
        for x in range(3):
            for z in range(3):
                t=z
                if z == 2:
                    z = 3
                    t=0
                if z==0:
                    t=2
                for y in range(3):
                    # square_settings = (y * square_size * screen_size[0] + (screen_size[0] / 3) * x + 50, z + (screen_size[1] / 9) * x+300, square_size * screen_size[0], square_size * screen_size[1] + 20)
                    square_settings = (y * square_size * screen_size[0] + (screen_size[0] / 3) * x * 0.93 + 0.05 * screen_size[0], z * square_size * screen_size[1] + (screen_size[1] / 9) * z/3 + screen_size[1] * 0.35, square_size * screen_size[0], square_size * screen_size[1] + 20)

                    # pygame.draw.rect(window, (255, 255, 255, 100), square_settings)
                    # pygame.draw.rect(window, (255, 255, 255, 100), square_settings)
                    pygame.draw.rect(window, (0, 0, 0), square_settings, 2)
                    # label = font.render(sections[x] + letters[y % 2] + numbers[y // 3], 1, (0, 0, 0))
                    label = font.render(sections[x] + letters[t] + str(y+1), 1, (0, 0, 0))
                    # pos = (x * square_size * screen_size[0] + (screen_size[0] / 3) * y + 40 + (square_size * screen_size[0])/2, z + (screen_size[1] / 9) * y + 290 + (square_size * screen_size[1])/2)
                    pos = (y * square_size * screen_size[0] + (screen_size[0] / 3) * x * 0.93 + 0.05 * screen_size[0] + 0.3 * square_size * screen_size[0], z * square_size * screen_size[1] + (screen_size[1] / 9) * z/3 + screen_size[1] * 0.35 + 0.3 * square_size * screen_size[1])
                    window.blit(label, pos)
                pygame.display.update()

                # draw a white line for text to be drawn over
                pygame.draw.rect(window, (255, 255, 255,100), (0, screen_size[0] - 50, screen_size[0], 50))

            pygame.display.update()

        # Wait for the user to click on the square
        # while True:
        old_score = score
        while score == old_score:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the position of the click
                    click_pos = event.pos

                    #set x and y and z as correct cordinates
                    # sections[square[0]] |||| letters[square[1] % 2] |||| numbers[square[1] // 3]
                    if square[1] == 0:
                        x = 2
                    elif square[1] == 2:
                        x = 0

                    # Check if the click was within the bounds of the square
                    if click_pos[0] > ((square[1] // 3) * square_size * screen_size[0] + (screen_size[0] / 3) * (square[0]) * 0.93 + 0.05 * screen_size[0]) and click_pos[0] < (((square[1] // 3) * square_size * screen_size[0] + (screen_size[0] / 3) * (square[0]) * 0.93 + 0.05 * screen_size[0])+(square_size * screen_size[0])) and screen_size[1] > ((square[1] % 2) * square_size * screen_size[1] + (screen_size[1] / 9) * (square[1] % 2) / 3 + screen_size[1] * 0.35) and screen_size[1] < (((square[1] % 2) * square_size * screen_size[1] + (screen_size[1] / 9) * (square[1] % 2) / 3 + screen_size[1] * 0.35)+(square_size * screen_size[1] + 20)):
                    # if (square[0] * square_size * screen_size[0] <= click_pos[0] < (square[0] + 1) * square_size * screen_size[0]) and (square[1] * square_size * screen_size[1] <= click_pos[1] < (square[1] + 1) * square_size * screen_size[1]):
                    # if click_pos[0] > (y * square_size * screen_size[0] + (screen_size[0] / 3) * x * 0.93 + 0.05 * screen_size[0]) and click_pos[0] < ((y * square_size * screen_size[0] + (screen_size[0] / 3) * x * 0.93 + 0.05 * screen_size[0])+(square_size * screen_size[0])) and screen_size[1] > (z * square_size * screen_size[1] + (screen_size[1] / 9) * z/3 + screen_size[1] * 0.35) and screen_size[1] < ((z * square_size * screen_size[1] + (screen_size[1] / 9) * z/3 + screen_size[1] * 0.35)+(square_size * screen_size[1] + 20)):
                        score += 1
                        break
                
                #exit game
                if keyboard.is_pressed('q'):  # if key 'q' is pressed 
                    pygame.quit()
                    os._exit(0)
                
                #restart game to main menu
                if keyboard.is_pressed('r'):  # if key 'r' is pressed
                    main_menu()
                

            # draw a white line for text to be drawn over
            pygame.draw.rect(window, (255, 255, 255), (0, screen_size[1]-40, screen_size[0], 40))

            # Draw the score
            score_label = font.render("Score: {}".format(score), 1, (0, 0, 0))
            pos = screen_size[0] - score_label.get_width() - 20, screen_size[1] - 20
            window.blit(score_label, pos)

            # Draw the time
            time_label = font.render("Time: {}".format((pygame.time.get_ticks() - start_time)/1000), 1, (0, 0, 0))
            pos = time_label.get_width() - 20, screen_size[1] - 20
            window.blit(time_label, pos)

            #write the chosen square to the top of the screen
            label = font.render("Square: {}".format(sections[square[0]] + letters[square[1] % 2] + numbers[square[1] // 3]), 1, (0, 0, 0))
            window.blit(label, (screen_size[0]/2, 0))

            #draw a box of the spot you need to click
            pygame.draw.rect(window, (255, 255, 255, 100), (square[0] * square_size * screen_size[0] + (screen_size[0] / 3) * square[1], (screen_size[1] / 9) * square[1], square_size * screen_size[0], square_size * screen_size[1]))
            pygame.draw.rect(window, (0, 0, 0), (square[0] * square_size * screen_size[0] + (screen_size[0] / 3) * square[1], (screen_size[1] / 9) * square[1], square_size * screen_size[0], square_size * screen_size[1]), 2)
            label = font.render(sections[square[0]] + letters[square[1] % 2] + numbers[square[1] // 3], 1, (0, 0, 0))
            pos = (square[0] * square_size * screen_size[0] + (screen_size[0] / 3) * square[1] + 20, (screen_size[1] / 9) * square[1] + 20)
            window.blit(label, pos)

            pygame.display.update()


            # if pygame.time.get_ticks() - start_time > 2000:
            #     break
        # time.sleep(2)
        print(score)
        print(pygame.time.get_ticks() - start_time)

        pygame.display.update()

main_menu()
game()
# %%
