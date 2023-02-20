import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLOR = (150,100,255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

kvadrat = Rect(200, 300, 200, 80)

run = True
moving = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            if kvadrat.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            kvadrat.move_ip(event.rel) #mici kvadrat isto kako se mice mis
            print(event.rel)

    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK, kvadrat)
    if moving:
        pygame.draw.rect(screen, RANDOM_COLOR, kvadrat, 4)
    pygame.display.flip()

pygame.quit()