from datetime import datetime

from objects.text import TextObject
from scenes.base import BaseScene


class GameOverScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.text = 'Game over ({})'
        self.objects.append(TextObject(self.game, 100, 100, "Game over", (255, 255, 255)))
        self.update_start_time()
        self.seconds_to_end = 3
        self.last_seconds_passed = 0

    def update_start_time(self):
        self.time_start = datetime.now()

    def process_logic(self):
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.objects[0].update_text(self.text.format(self.seconds_to_end - seconds_passed))
        if seconds_passed >= self.seconds_to_end:
            self.game.current_scene_index = 0