import pygame
from pygame.locals import *

pygame.init()

DIMENZIJE = (600, 400)
screen = pygame.display.set_mode(DIMENZIJE)

BLACK = [(0, 0, 0), "black"]
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = [(255, 0, 0), "red"]
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

BOJA = YELLOW

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                BOJA = key_dict[event.key][0]
            caption = 'background color = ' + str(key_dict[event.key][1])
            pygame.display.set_caption(caption)


    screen.fill(BOJA)
    pygame.display.flip()

pygame.quit()

