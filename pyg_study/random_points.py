import pygame
from pygame.locals import *
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RANDOM_COLOR = (255, 150, 0)
ANOTHER_C = (0, 255, 255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

dots_list = [0]*100
for i in range(len(dots_list)):
    dots_list[i] = Rect(randint(0, 800), randint(0, 600), 10, 10)
print(dots_list)
kvadrat = Rect(randint(0, 800), randint(0, 600), randint(0, 800), randint(0, 600))
run = True
speed = [5, 5]
while run:
    clock = pygame.time.Clock()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_r:
                kvadrat = Rect(randint(0, 800), randint(0, 600), randint(0, 800), randint(0, 600))

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, kvadrat, 2)
    for dot in dots_list:
        if kvadrat.colliderect(dot):
            pygame.draw.rect(screen, RANDOM_COLOR, dot)
        else:
            pygame.draw.rect(screen, ANOTHER_C, dot)

    pygame.display.flip()

pygame.quit()