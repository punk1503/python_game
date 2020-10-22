import pygame
import sys

from random import randint

from button import Button

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

size = width, height = 800, 600
current_scene_index = 0


class Ball:
    image = pygame.image.load('basketball.png')

    def __init__(self):
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, width - self.rect.width - 10)
        self.rect.y = randint(10, height - self.rect.height - 10)
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


def start_game():
    global current_scene_index
    current_scene_index = 1


class MenuScene:

    def __init__(self):
        BUTTON_STYLE = {
            "hover_color": BLUE,
            "clicked_color": GREEN,
            "clicked_font_color": BLACK,
            "hover_font_color": ORANGE,
        }
        self.button1 = Button((width // 2 - 100, height // 2 - 20 - 25, 200, 50),
                         RED, start_game, text='Запуск игры', **BUTTON_STYLE)
        self.button2 = Button((width // 2 - 100, height // 2 + 25, 200, 50),
                         RED, exit, text='Выход', **BUTTON_STYLE)

    def process_events(self, event):
        self.button1.check_event(event)
        self.button2.check_event(event)

    def process_logic(self):
        pass

    def process_draw(self, screen):
        self.button1.update(screen)
        self.button2.update(screen)


class GameScene:

    def __init__(self):
        self.balls = [Ball() for i in range(5)]

    def process_events(self, event):
        pass

    def process_logic(self):
        for ball in self.balls:
            ball.process_logic()
        for i in range(len(self.balls) - 1):
            for j in range(i + 1, len(self.balls)):
                if self.balls[i].collides_with(self.balls[j]):
                    self.balls[i].bounce(self.balls[j])

    def process_draw(self, screen):
        for ball in self.balls:
            ball.process_draw(screen)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)

    scenes = [
        MenuScene(),
        GameScene()
    ]

    game_over = False
    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            scenes[current_scene_index].process_events(event)

        # Логика игры
        scenes[current_scene_index].process_logic()

        # Отрисовка
        screen.fill(BLACK)
        scenes[current_scene_index].process_draw(screen)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit()


if __name__ == '__main__':
    main()
