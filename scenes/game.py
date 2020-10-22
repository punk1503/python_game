from objects.ball import BallObject
from scenes.base import BaseScene


def main():
    pass


if __name__ == '__main__':
    main()


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