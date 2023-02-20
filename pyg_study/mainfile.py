import pygame
from pygame.locals import *

class App:

    def __init__(self):
        pygame.init()
        self.flags = RESIZABLE
        self.rect = Rect(0, 0, 840, 640)

        App.screen = pygame.display.set_mode(self.rect.size, self.flags)
        App.t = Text('Pygame App', pos=(0, 0))
        App.f = Text('Something', pos=(200, 200))
        App.running = True

    def run(self):
        while App.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    App.running = False
            App.screen.fill(Color('gray'))
            App.t.draw()
            App.f.draw()
            pygame.display.update()
        pygame.quit()

class Text:

    def __init__(self, text, pos, **options):
        self.text = text
        self.pos = pos

        self.fontname = None
        self.fontsize = 72
        self.fontcolor = Color('black')
        self.set_font()
        self.render()

    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)

    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos

    def draw(self):
        App.screen.blit(self.img, self.rect)

if __name__ == '__main__':
    App().run()