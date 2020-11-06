import pygame
from objects.image import ImageObject
from constants import RED

class Platform(ImageObject):
    filename = 'images/brick.png'

    def __init__(self, game, filename=None, x=0, y=0, speed=4):
        super().__init__(game, filename, x, y)
        self.rect
        self.shift = 0
        self.speed = speed
    
    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.shift = -1
            elif event.key == pygame.K_d:
                self.shift = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                self.shift = 0

    def move(self):
        self.rect.x += self.shift * self.speed
        self.rect.x = max(min(self.rect.x, self.rect.w + self.game.width), 0)