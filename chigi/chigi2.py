# a python game in pygame that has a grid of 9 by 3 where there are predetairment cordinents and the user when the countdown ends needs to click on the correct slot to get a point and the user is timed for the amout of time from saying the cordinet to pressing it

import pygame
import os
import time

pygame.init()

pygame.mouse.set_cursor(*pygame.cursors.arrow)

window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

absolute_path = os.path.dirname(__file__)
relative_path = "backround.png"
full_path = os.path.join(absolute_path, relative_path)
print(full_path)

background = pygame.image.load(full_path).convert()
background = pygame.transform.smoothscale(background, window.get_size())

window.blit(background, (0, 0))
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				os._exit(0)

# pygame.quit()
# exit()
