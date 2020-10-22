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


class DrawableObject:
    def __init__(self, game):
        self.game = game

    def process_event(self, event):
        pass

    def process_logic(self):
        pass

    def process_draw(self):
        pass  # use self.game.screen, padawan


class ButtonObject(DrawableObject):
    BUTTON_STYLE = {
        "hover_color": BLUE,
        "clicked_color": GREEN,
        "clicked_font_color": BLACK,
        "hover_font_color": ORANGE,
    }

    def __init__(self, game, x, y, width, height, color, function, text):
        super().__init__(game)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.function = function
        self.text = text
        self.button = Button(
            (self.x, self.y, self.width, self.height),
            self.color, self.function, text=self.text, **self.BUTTON_STYLE)

    def process_event(self, event):
        self.button.check_event(event)

    def process_draw(self):
        self.button.update(self.game.screen)


class BallObject(DrawableObject):
    image = pygame.image.load('basketball.png')

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


class BaseScene:
    def __init__(self, game):
        self.game = game
        self.objects = []

    def process_event(self, event):
        for object in self.objects:
            object.process_event(event)

    def process_logic(self):
        for object in self.objects:
            object.process_logic()

    def process_draw(self):
        for object in self.objects:
            object.process_draw()


class MenuScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects.append(
            ButtonObject(
                self.game,
                self.game.width // 2 - 100,
                self.game.height // 2 - 20 - 25,
                200,
                50,
                RED,
                self.start_game,
                text='Запуск игры'
            )
        )
        self.objects.append(
            ButtonObject(
                self.game,
                self.game.width // 2 - 100,
                self.game.height // 2 + 25,
                200,
                50,
                RED,
                exit,
                text='Выход'
            )
        )

    def start_game(self):
        self.game.current_scene_index = 1


class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.objects = [BallObject(game) for i in range(5)]

    def process_logic(self):
        super().process_logic()

        for i in range(len(self.objects) - 1):
            for j in range(i + 1, len(self.objects)):
                if self.objects[i].collides_with(self.objects[j]):
                    self.objects[i].bounce(self.objects[j])


class Game:
    size = width, height = 800, 600
    current_scene_index = 0

    def __init__(self):
        self.screen = pygame.display.set_mode(self.size)
        self.scenes = [
            MenuScene(self),
            GameScene(self)
        ]
        self.game_over = False

    def process_all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            self.scenes[self.current_scene_index].process_event(event)

    def process_all_logic(self):
        self.scenes[self.current_scene_index].process_logic()

    def process_all_draw(self):
        self.screen.fill(BLACK)
        self.scenes[self.current_scene_index].process_draw()
        pygame.display.flip()

    def main_loop(self):
        while not self.game_over:
            self.process_all_events()
            self.process_all_logic()
            self.process_all_draw()
            pygame.time.wait(10)


def main():
    pygame.init()
    game = Game()
    game.main_loop()
    sys.exit()


if __name__ == '__main__':
    main()
