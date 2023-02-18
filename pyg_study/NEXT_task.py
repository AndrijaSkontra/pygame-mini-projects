import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
running = True
drawing = False
points = []
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            points.append(event.pos)
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            points[-1] = event.pos

    screen.fill(WHITE)
    for tocka in range(0, len(points) - 1):
        pygame.draw.line(screen, BLACK, points[tocka], points[tocka + 1], 2)
    pygame.display.flip()

pygame.quit()
