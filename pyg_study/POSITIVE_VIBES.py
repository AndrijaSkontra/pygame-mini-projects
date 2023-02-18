import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
size = 800, 600
screen = pygame.display.set_mode(size)

keys_dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}
kvadrat = pygame.Rect(200, 200, 200, 200)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key in keys_dir:
                vector = keys_dir[event.key]
                print(vector)
                kvadrat.move_ip(vector)  #MORA BITI MOVE_IP?

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, kvadrat, 3)

    pygame.display.flip()

pygame.quit()
