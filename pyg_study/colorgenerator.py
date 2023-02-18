import pygame

pygame.init()

DIMENZIJE = (600, 400)
screen = pygame.display.set_mode(DIMENZIJE)

BOJA = [100, 100, 100]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                BOJA[0] += 20
            if event.key == pygame.K_a:
                BOJA[1] += 20
            if event.key == pygame.K_w:
                BOJA[2] += 20
            if event.key == pygame.K_l:
                BOJA[0] -= 20
            if event.key == pygame.K_k:
                BOJA[1] -= 20
            if event.key == pygame.K_s:
                BOJA[2] -= 20

    for i in range(3):
        if BOJA[i] > 255:
            BOJA[i] = 255
        if BOJA[i] < 0:
            BOJA[i] = 0
            
            
    screen.fill(BOJA)
    pygame.display.flip()

pygame.quit()