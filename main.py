from random import randint

import pygame
import sys

BLACK = 0, 0, 0
size = width, height = 800, 600


class Ball:
    image = pygame.image.load('basketball.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, width-self.rect.width - 10)
        self.rect.y = randint(10, height-self.rect.height - 10)
        self.speed = [randint(-2, 2), randint(-2, 2)]
        self.radius = self.rect.width // 2

    def collides_with(self, other):
        return pygame.sprite.collide_circle(self, other)

    def bounce(self, other):
        self.speed, other.speed = other.speed, self.speed

    def process_logic(self):
        if self.rect.right >= width or self.rect.left <= 0:
            self.speed[0] *= -1
        if self.rect.bottom >= height or self.rect.top <= 0:
            self.speed[1] *= -1

        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    game_over = False

    balls = [Ball() for i in range(5)]

    while not game_over:
        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Логика работы
        for ball in balls:
            ball.process_logic()

        for i in range(len(balls)-1):
            for j in range(i+1, len(balls)):
                if balls[i].collides_with(balls[j]):
                    balls[i].bounce(balls[j])

        # Отрисовка кадра
        screen.fill(BLACK)  # чёрный фон, рисуется первым!
        for ball in balls:
            ball.process_draw(screen)

        # Подтверждение отрисовки и ожидание
        pygame.display.flip()
        pygame.time.wait(10)
    sys.exit()


if __name__ == '__main__':
    main()
