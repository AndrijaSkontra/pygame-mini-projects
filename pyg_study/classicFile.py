import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (150, 100, 255)
LIGHT_BLUE = (0, 255, 255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(WHITE)
    pygame.display.flip()

pygame.quit()