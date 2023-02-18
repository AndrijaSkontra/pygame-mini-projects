import pygame
from pygame.locals import *

pygame.init()

size = 800, 600

pygame.display.set_mode(size)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False