from datetime import datetime

import pygame, sys

size = width, height = 800, 600
black = 0, 0, 0


def main():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(size)
    gameover = False

    time_start = datetime.now()

    seconds_to_end = 3
    last_seconds_passed = 0

    font = pygame.font.SysFont('Comic Sans MS', 30, True)
    text = 'Game over ({})'

    text_surface = font.render(text.format(seconds_to_end), True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = width // 2
    text_rect.centery = height // 2

    while not gameover:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

        # Логика работы
        time_current = datetime.now()
        seconds_passed = (time_current - time_start).seconds
        if last_seconds_passed != seconds_passed:
            text_surface = font.render(text.format(seconds_to_end - seconds_passed), True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            text_rect.centerx = width // 2
            text_rect.centery = height // 2

        if seconds_passed >= seconds_to_end:
            gameover = True

        # Отрисовка
        screen.fill(black)
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit()


if __name__ == '__main__':
    main()
