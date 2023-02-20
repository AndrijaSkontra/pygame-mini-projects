import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLOR = (150,100,255)

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)

keys_dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
kvadrat = Rect(50, 60, 200, 80)
kvadrat_0 = Rect(100, 20, 100, 140)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key in keys_dir:
                vector = keys_dir[event.key]
                kvadrat.move_ip(vector)  #MORA BITI MOVE_IP?

    screen.fill(WHITE)
    clip = kvadrat_0.clip(kvadrat)
    union = kvadrat_0.union(kvadrat)
    pygame.draw.rect(screen, (255, 0, 0), union, 0)
    pygame.draw.rect(screen, (0, 255, 0), clip, 0)
    pygame.draw.rect(screen, BLACK, kvadrat, 4)
    pygame.draw.rect(screen, RANDOM_COLOR, kvadrat_0, 1)

    pygame.display.flip()

pygame.quit()
