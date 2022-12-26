import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

BATMAN_SIRINA = 100
BATMAN_VISINA = 100
SHURIKEN_SIRINA = 100
SHURIKEN_VISINA = 50
BRZINA_BATMANA = 1.5

BATMAN_IMAGE = pygame.image.load(os.path.join('R.png'))
BATMAN = pygame.transform.scale(BATMAN_IMAGE,(BATMAN_SIRINA,BATMAN_VISINA))
SHURIKEN_IMAGE = pygame.image.load(os.path.join('34c645_d40947803670443dbcfd33d1ee205d0f.png'))
SHURIKEN = pygame.transform.scale(SHURIKEN_IMAGE,(SHURIKEN_SIRINA,SHURIKEN_VISINA))
BACKGROUND_IMAGE = pygame.image.load(os.path.join('ecec9f0dbde599a13bb61512654552ba.png'))
BACKGROUD = pygame.transform.scale(BACKGROUND_IMAGE,(WIDTH,HEIGHT))


pygame.display.set_caption("Jump")

def draw_window(batman, postojanje_shurikena, shuriken):
    WIN.blit(BACKGROUD, (0, 0))
    WIN.blit(BATMAN,(batman.x,batman.y))# kordinate batmana
    if postojanje_shurikena == 1:
        WIN.blit(SHURIKEN, (shuriken.x, shuriken.y))
    else:
        shuriken.x = 200
    pygame.display.update()

def kretanje(batman):
    if pygame.key.get_pressed()[pygame.K_d]:
        batman.x += BRZINA_BATMANA*2
    if pygame.key.get_pressed()[pygame.K_a]:
        batman.x -= BRZINA_BATMANA*2
    if pygame.key.get_pressed()[pygame.K_w]:
        for i in range(30):
            batman.y -= BRZINA_BATMANA
            if pygame.key.get_pressed()[pygame.K_d]:
                batman.x += BRZINA_BATMANA
            elif pygame.key.get_pressed()[pygame.K_a]:
                batman.x -= BRZINA_BATMANA/2
            draw_window(batman)
            pygame.time.delay(7)
        for i in range(30):
            batman.y -= BRZINA_BATMANA/2
            if pygame.key.get_pressed()[pygame.K_d]:
                batman.x += BRZINA_BATMANA
            elif pygame.key.get_pressed()[pygame.K_a]:
                batman.x -= BRZINA_BATMANA/2
            draw_window(batman)
            pygame.time.delay(7)
        for i in range(30):
            batman.y += BRZINA_BATMANA*2
            if pygame.key.get_pressed()[pygame.K_d]:
                batman.x += BRZINA_BATMANA
            elif pygame.key.get_pressed()[pygame.K_a]:
                batman.x -= BRZINA_BATMANA/2
            draw_window(batman)
            pygame.time.delay(12)



def main():
    postojanje_shurikena = 0
    clock = pygame.time.Clock()
    batman = pygame.Rect(300,  300, BATMAN_SIRINA, BATMAN_VISINA)
    shuriken = pygame.Rect(batman.x, batman.y, SHURIKEN_SIRINA, SHURIKEN_VISINA)
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    postojanje_shurikena = 1



        kretanje(batman)
        draw_window(batman,postojanje_shurikena,shuriken)
        if postojanje_shurikena == 1:
            shuriken.x += 5
            if shuriken.x > WIDTH:
                postojanje_shurikena = 0
    pygame.quit()

main()