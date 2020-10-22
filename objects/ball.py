from random import randint

import pygame

from objects.base import DrawableObject


class BallObject(DrawableObject):
    image = pygame.image.load('images/basketball.png')

    def __init__(self, game):
        super().__init__(game)
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, game.width - self.rect.width - 10)
        self.rect.y = randint(10, game.height - self.rect.height - 10)
        self.speed = [randint(-2, 2), randint(-2, 2)]
        self.radius = self.rect.width // 2

    def collides_with(self, other):
        return pygame.sprite.collide_circle(self, other)

    def bounce(self, other):
        self.speed, other.speed = other.speed, self.speed

    def process_logic(self):
        if self.rect.right >= self.game.width or self.rect.left <= 0:
            self.speed[0] *= -1
        if self.rect.bottom >= self.game.height or self.rect.top <= 0:
            self.speed[1] *= -1

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def process_draw(self):
        self.game.screen.blit(self.image, self.rect)
