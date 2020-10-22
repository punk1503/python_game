import pygame

from constants import BLACK
from scenes.game import GameScene
from scenes.menu import MenuScene


def main():
    pass


if __name__ == '__main__':
    main()


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