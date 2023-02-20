import pygame
from pygame.locals import *
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (150, 100, 255)
LIGHT_BLUE = (0, 255, 255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

run = True

slika = pygame.image.load("download.jpg")
slika0 = slika.copy()
slika.convert()
kut = 0
velicina = 1
rect_slike = slika.get_rect()
center = 800//2, 600//2
rect_slike.center = center
#mouse = pygame.mouse.get_pos()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                kut -= 10
            elif event.key == K_LEFT:
                kut += 10
            elif event.key == K_UP:
                velicina *= 1.1
                print(velicina)
            elif event.key == K_DOWN:
                velicina *= 0.9
                print(velicina)
            elif event.key == K_o:
                velicina = 1
                kut = 0
                slika = slika0
            elif event.key == K_h:
                slika = pygame.transform.flip(slika, True, False)
            elif event.key == K_v:
                slika = pygame.transform.flip(slika, False, True)
            elif event.key == K_2:
                slika = pygame.transform.laplacian(slika)
            slika = pygame.transform.rotozoom(slika, kut, velicina)
            rect_slike = slika.get_rect()
            rect_slike.center = center
            slika.convert()

    screen.fill(WHITE)
    screen.blit(slika, rect_slike)
    pygame.display.flip()

pygame.quit()