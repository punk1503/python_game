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
game_start = False

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



def start_game():
    print('Trying to start the game')


def main():
    pygame.init()

    pygame.mixer.init()

    BUTTON_STYLE = {
        "hover_color": BLUE,
        "clicked_color": GREEN,
        "clicked_font_color": BLACK,
        "hover_font_color": ORANGE,
    }

    screen = pygame.display.set_mode(size)


    balls = [Ball() for i in range(5)]

    game_over = False
    button1 = Button((width // 2 - 100, height // 2 - 20 - 25, 200, 50),
                     RED, start_game, text='Запуск игры', **BUTTON_STYLE)
    button2 = Button((width // 2 - 100, height // 2 + 25, 200, 50),
                     RED, exit, text='Выход', **BUTTON_STYLE)


    while not game_over:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if not game_start:
                pass
            else:
                button1.check_event(event)
                button2.check_event(event)

        if not game_start:
            pass
        else:
            for ball in balls:
                ball.process_logic()
            for i in range(len(balls) - 1):
                for j in range(i + 1, len(balls)):
                    if balls[i].collides_with(balls[j]):
                        balls[i].bounce(balls[j])

        # Отрисовка
        screen.fill(BLACK)
        if not game_start:
            button1.update(screen)
            button2.update(screen)
        else:
            for ball in balls:
                ball.process_draw(screen)
        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit()


if __name__ == '__main__':
    main()
