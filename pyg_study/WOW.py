import pygame
from pygame.locals import *
pygame.init()
pts = ('topleft', 'topright', 'bottomleft', 'bottomright',
'midtop', 'midright', 'midbottom', 'midleft', 'center')
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 0, 0)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
rect = Rect(300, 200, 200, 200)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, rect, 3)
    for dot in pts:
        command = eval('rect.' + dot)
        pygame.draw.circle(screen, BLUE, command, 2)
    pygame.display.flip()
pygame.quit()

