import pygame

from objects.base import DrawableObject


class ImageObject(DrawableObject):
    filename = 'images/basketball.png'

    def __init__(self, game, filename=None, x=None, y=None):
        super().__init__(game)
        if filename:
            self.filename = filename
        self.image = pygame.image.load(self.filename)
        self.rect = self.image.get_rect()
        self.rect.x = x if x else 0
        self.rect.y = y if y else 0

    def process_draw(self):
        self.game.screen.blit(self.image, self.rect)