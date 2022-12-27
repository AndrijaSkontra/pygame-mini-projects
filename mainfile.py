import pygame
import os

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

LIK_SIRINA = 100
LIK_VISINA = 100
PROJEKTIL_SIRINA = 100
PROJEKTIL_VISINA = 50
BRZINA_LIKA = 3
BRZINA_SKOKA = 2
MAX_PROJEKTILA = 2
BRZINA_PROJEKTILA = 5
MAX_SKOKOVA = 2


LIK_IMAGE = pygame.image.load(os.path.join('R-modified.png'))
LIK = pygame.transform.scale(LIK_IMAGE, (LIK_SIRINA, LIK_VISINA))
LIK_DRUGA_STRANA_IMAGE = pygame.image.load(os.path.join('R.png'))
LIK_DRUGA_STRANA = pygame.transform.scale(LIK_DRUGA_STRANA_IMAGE, (LIK_SIRINA, LIK_VISINA))
PROJEKTIL_IMAGE = pygame.image.load(os.path.join('34c645_d40947803670443dbcfd33d1ee205d0f.png'))
PROJEKTIL_IMAGE2 = pygame.image.load(os.path.join('34c645_d40947803670443dbcfd33d1ee205d0f-modified.png'))
PROJEKTIL = pygame.transform.scale(PROJEKTIL_IMAGE, (PROJEKTIL_SIRINA, PROJEKTIL_VISINA))
PROJEKTIL2 = pygame.transform.scale(PROJEKTIL_IMAGE2, (PROJEKTIL_SIRINA, PROJEKTIL_VISINA))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('ecec9f0dbde599a13bb61512654552ba.png'))
BACKGROUD = pygame.transform.scale(BACKGROUND_IMAGE, (WIDTH, HEIGHT))

pygame.display.set_caption("Game by Andrija")


def draw_window(moj_lik, lista_projektila, lista_projektila2, orijentacija):
    WIN.blit(BACKGROUD, (0, 0))
    if orijentacija == 1:
        WIN.blit(LIK, (moj_lik.x, moj_lik.y))
    if orijentacija == 0:
        WIN.blit(LIK_DRUGA_STRANA, (moj_lik.x, moj_lik.y))
    for projektil in lista_projektila:
        WIN.blit(PROJEKTIL, (projektil.x, projektil.y))
    for projektil2 in lista_projektila2:
        WIN.blit(PROJEKTIL2, (projektil2.x, projektil2.y))
    pygame.display.update()


def projektil_movement(lista_projektila, lista_projektila2, orijentacija):
    if orijentacija == 1:
        for projektil in lista_projektila:
            projektil.x += BRZINA_PROJEKTILA
            if projektil.x > WIDTH:
                lista_projektila.remove(projektil)
    if orijentacija == 0:
        for projektil2 in lista_projektila2:
            projektil2.x -= BRZINA_PROJEKTILA
            if projektil2.x < 0:
                lista_projektila2.remove(projektil2)


def moj_lik_movement(moj_lik):
    if pygame.key.get_pressed()[pygame.K_d]:
        moj_lik.x += BRZINA_LIKA
    if pygame.key.get_pressed()[pygame.K_a]:
        moj_lik.x -= BRZINA_LIKA




def main():
    moj_lik = pygame.Rect(550, 380, LIK_SIRINA, LIK_VISINA)
    lik_ubrzanje = 0
    gravitacija = 1
    snaga_skoka = -15
    brojac_skokova = 0
    orijentacija = 1  # desno
    lista_projektila = []
    lista_projektila2 = []
    run = True
    while run:
        clock = pygame.time.Clock()
        clock.tick(90)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and (len(lista_projektila) + len(
                        lista_projektila2)) < MAX_PROJEKTILA:
                    if orijentacija == 1:
                        moj_projektil = pygame.Rect(moj_lik.x, moj_lik.y, PROJEKTIL_SIRINA,
                                                    PROJEKTIL_VISINA)
                        lista_projektila.append(moj_projektil)
                    if orijentacija == 0:
                        moj_projektil2 = pygame.Rect(moj_lik.x, moj_lik.y, PROJEKTIL_SIRINA,
                                                    PROJEKTIL_VISINA)
                        lista_projektila2.append(moj_projektil2)

                if event.key == pygame.K_w and brojac_skokova < MAX_SKOKOVA:  # JUMP
                    lik_ubrzanje = snaga_skoka
                    brojac_skokova += 1
        lik_ubrzanje += gravitacija
        moj_lik.y += lik_ubrzanje
        if moj_lik.y > 380:
            lik_ubrzanje = 0
            moj_lik.y = 380
            brojac_skokova = 0
        if pygame.key.get_pressed()[pygame.K_d]:
            orijentacija = 1
        if pygame.key.get_pressed()[pygame.K_a]:
            orijentacija = 0
        moj_lik_movement(moj_lik)
        projektil_movement(lista_projektila, lista_projektila2, orijentacija)
        draw_window(moj_lik, lista_projektila, lista_projektila2, orijentacija)
        print(orijentacija)
    pygame.quit()


main()







