import pygame
from pygame.locals import *
from random import randint

size = 900, 600
width, height = size
BLUE = (0, 0, 255)
LIGHT_BLUE = (200, 200, 255)
MAGENTA = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(size)
running = True
rect_list = []
rect_size = [50, 50]
pygame.mouse.set_visible(True)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            start = event.pos
            rect_size[0] += 20
            rect_size[1] += 20
            rect = pygame.Rect(start, rect_size)
            rect_list.append(rect)
            color1 = randint(5, 250)
            color2 = randint(5, 250)
            color3 = randint(5, 250)
    screen.fill(MAGENTA)
    for i in rect_list:
        pygame.draw.rect(screen, (color1, color2, color3), i)
    pygame.display.flip()
pygame.quit()