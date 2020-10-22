from constants import RED
from objects.button import ButtonObject
from scenes.base import BaseScene


def main():
    pass


if __name__ == '__main__':
    main()


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