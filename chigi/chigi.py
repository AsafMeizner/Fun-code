import pygame
import os
import time

pygame.mixer.init()

sections = ['A', 'B']

section_recordings = []
for section in sections:
    section_recordings.append(pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"recordings\\section_{}.mp3".format(section))))

section_recordings[0].play()
time.sleep(0.2)
section_recordings[1].play()
time.sleep(0.2)
section_recordings[0].play()
time.sleep(1)