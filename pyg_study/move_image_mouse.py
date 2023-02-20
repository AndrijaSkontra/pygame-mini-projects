import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (150, 100, 255)
LIGHT_BLUE = (0, 255, 255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

BALL = pygame.image.load("lopta-removebg-preview.png")
BALL.convert()

ball_rect = BALL.get_rect()
center = 800//2, 600//2
ball_rect.center = center
run = True
moving = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEBUTTONDOWN:
            if ball_rect.collidepoint(event.pos):
                moving = True
        elif event.type == MOUSEBUTTONUP:
            moving = False
        elif event.type == MOUSEMOTION and moving:
            ball_rect.move_ip(event.rel) #rel je kao vektor kretanja misa
            print(event.rel)

    screen.fill(WHITE)
    screen.blit(BALL, ball_rect)
    pygame.display.flip()

pygame.quit()