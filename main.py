import pygame, sys

size = width, height = 800, 600
black = 0, 0, 0


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False

    while not gameover:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

        # Логика работы

        # Отрисовка
        screen.fill(black)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit()


if __name__ == '__main__':
    main()
