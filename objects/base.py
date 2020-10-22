def main():
    pass


if __name__ == '__main__':
    main()


class DrawableObject:
    def __init__(self, game):
        self.game = game

    def process_event(self, event):
        pass

    def process_logic(self):
        pass

    def process_draw(self):
        pass  # use self.game.screen, padawan