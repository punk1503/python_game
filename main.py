import pygame, sys

from button import Button

size = width, height = 800, 600
black = 0, 0, 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)


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

    button1 = Button((width // 2 - 100, height // 2 - 20 - 25, 200, 50),
                     RED, start_game, text='Запуск игры', **BUTTON_STYLE)
    button2 = Button((width // 2 - 100, height // 2 + 25, 200, 50),
                     RED, exit, text='Выход', **BUTTON_STYLE)

    gameover = False
    while not gameover:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            button1.check_event(event)
            button2.check_event(event)

        # Логика работы

        # Отрисовка
        screen.fill(black)
        button1.update(screen)
        button2.update(screen)
        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit()


if __name__ == '__main__':
    main()
