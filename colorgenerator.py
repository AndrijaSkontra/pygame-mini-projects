import pygame
pygame.init()

DIMENZIJE = (600, 400)
screen = pygame.display.set_mode(DIMENZIJE)


YELLOW = [100, 100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                YELLOW[0] += 20
            if event.key == pygame.K_a:
                YELLOW[1] += 20
            if event.key == pygame.K_w:
                YELLOW[2] += 20
            if event.key == pygame.K_l:
                YELLOW[0] -= 20
            if event.key == pygame.K_k:
                YELLOW[1] -= 20
            if event.key == pygame.K_s:
                YELLOW[2] -= 20

    for i in range(3):
        if YELLOW[i] > 255:
            YELLOW[i] = 255
        if YELLOW[i] < 0:
            YELLOW[i] = 0
    screen.fill(YELLOW)
    pygame.display.flip()

pygame.quit()