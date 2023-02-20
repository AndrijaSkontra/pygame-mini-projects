import time

import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (150, 100, 255)
LIGHT_BLUE = (0, 255, 255)

pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

font1 = pygame.font.SysFont("comicsansms", 100)
editable = "Editable text"
font1 = pygame.font.SysFont("ebrima", 72)
slika_fonta_2 = font1.render("MisterCool", True, PURPLE)
fonts = pygame.font.get_fonts()
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key == K_BACKSPACE:
                editable = editable[:-1]
    slika_fonta_1 = font1.render(f"{editable}", True, LIGHT_BLUE)
    rect_slike = slika_fonta_1.get_rect()
    screen.fill(WHITE)
    screen.blit(slika_fonta_1, rect_slike)
    screen.blit(slika_fonta_2, (50,400))
    cursor_postion1 = rect_slike.topright[0] + 10, rect_slike.topright[1]
    cursor_position2 = rect_slike.bottomright[0] + 10, rect_slike.bottomright[1]
    if time.time() % 1 < 0.5:
        pygame.draw.line(screen, BLACK, cursor_postion1, cursor_position2, 1)

    pygame.display.flip()

pygame.quit()
