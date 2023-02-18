import pygame
from pygame.locals import *

size = 900, 600
width, height = size
BLUE = (0, 0, 255)
LIGHT_BLUE = (200, 200, 255)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode(size)
running = True
start = 0, 0
drawing = False
start = 0, 0
end = 0, 0
pygame.mouse.set_visible(True)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            start = event.pos
            end = event.pos
            print(start)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            print(end)
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            print(end)
    screen.fill(WHITE)
    if start != (0, 0) and start != end and drawing:
        if start[0] < end[0] and start[1] < end[1]:
            size = end[0] - start[0], end[1] - start[1]
            right_down = start[0], start[1]
            pygame.draw.rect(screen, LIGHT_BLUE, (right_down, size))
            pygame.draw.rect(screen, BLUE, (right_down, size), 1)
        if start[0] > end[0] and start[1] > end[1]:
            size = start[0] - end[0], start[1] - end[1]
            left_up = end[0], end[1]
            pygame.draw.rect(screen, LIGHT_BLUE, (left_up, size))
            pygame.draw.rect(screen, BLUE, (left_up, size), 1)
        if start[0] > end[0] and start[1] < end[1] :
            size = start[0] - end[0], end[1] - start[1]
            left_down = end[0], start[1]
            pygame.draw.rect(screen, LIGHT_BLUE, (left_down, size))
            pygame.draw.rect(screen, BLUE, (left_down, size), 1)
        if start[0] < end[0] and start[1] > end[1]:
            size = end[0] - start[0], start[1] - end[1]
            right_up = start[0], end[1]
            pygame.draw.rect(screen, LIGHT_BLUE, (right_up, size))
            pygame.draw.rect(screen, BLUE, (right_up, size), 1)
    pygame.display.flip()
pygame.quit()