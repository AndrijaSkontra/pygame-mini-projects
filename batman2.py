import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

LIK_SIRINA = 100
LIK_VISINA = 100
PROJEKTIL_SIRINA = 100
PROJEKTIL_VISINA = 50
BRZINA_LIKA = 1.5

BATMAN_IMAGE = pygame.image.load(os.path.join('R.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE,(BATMAN_SIRINA,BATMAN_VISINA))
SHURIKEN_IMAGE = pygame.image.load(os.path.join('34c645_d40947803670443dbcfd33d1ee205d0f.png'))
SHURIKEN = pygame.transform.scale(SHURIKEN_IMAGE,(SHURIKEN_SIRINA,SHURIKEN_VISINA))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('ecec9f0dbde599a13bb61512654552ba.png'))
BACKGROUD = pygame.transform.scale(BACKGROUND_IMAGE,(WIDTH,HEIGHT))