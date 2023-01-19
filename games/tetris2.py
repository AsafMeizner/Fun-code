import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
width = 600
height = 600
screen = pygame.display.set_mode((width, height))

# Set the title of the window
pygame.display.set_caption('Snake')

# Set the background color
bg_color = (0, 0, 0)

# Create the snake
snake = [(200, 200), (210, 200), (220, 200)]

# Set the direction of the snake
snake_dir = 'RIGHT'

# Set the initial score
score = 0

# Set the font for the score
font = pygame.font.Font('freesansbold.ttf', 18)

# Define a function to display the score on the screen
def show_score(surf, text, size, x, y):
    score_font = pygame.font.Font(font, size)
    score_text = score_font.render(text, True, (255, 255, 255))
    surf.blit(score_text, (x, y))

# Set the game over flag to False
game_over = False

# Run the game loop
while not game_over:
    # Fill the background color
    screen.fill(bg_color)

    # Get the events from the user
    for event in pygame.event.get():
        # If the user clicks the 'X' button, set the game over flag to True
        if event.type == pygame.QUIT:
            game_over = True
        # If the user presses a key, set the direction of the snake
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake_dir = 'UP'
            elif event.key == pygame.K_DOWN:
                snake_dir = 'DOWN'
            elif event.key == pygame.K_LEFT:
                snake_dir = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                snake_dir = 'RIGHT'

    # Move the snake
    if snake_dir == 'UP':
        snake[0] = (snake[0][0], snake[0][1] - 10)
    elif snake_dir == 'DOWN':
        snake[0] = (snake[0][0], snake[0][1] + 10)
    elif snake_dir == 'LEFT':
        snake[0] = (snake[0][0] - 10, snake[0][1])
    elif snake_dir == 'RIGHT':
        snake[0] = (snake[0][0] + 10, snake[0][1])

    # Check if the snake has hit the wall or itself
    if (snake[0][0] > width - 10 or snake[0][0] < 0 or
        snake[0][1] > height - 10 or snake[0][1] < 0 or
        snake[0] in snake[1:]):
        # game_over = True
        pass

    # If the snake has not hit the wall or itself, move
