from datetime import datetime

from objects.text import TextObject
from scenes.base import BaseScene

from constants import GREEN
from constants import YELLOW
from constants import ORANGE


class GameOverScene(BaseScene):
    text_format = 'Game over ({})'
    seconds_to_end = 3

    def __init__(self, game):
        super().__init__(game)
        self.last_seconds_passed = 0
        self.three_hs = [0, 0, 0]
        
        self.text = TextObject(self.game, self.game.width // 2, 50, self.get_gameover_text_formatted(), (255, 255, 255))
        self.first_record_text = TextObject(self.game, self.game.width//2, self.game.height * 0.25, '1) ' + str(self.three_hs[0]), GREEN)
        self.second_record_text = TextObject(self.game, self.game.width//2, self.game.height * 0.50, '2) ' + str(self.three_hs[1]), YELLOW)
        self.third_record_text = TextObject(self.game, self.game.width//2, self.game.height * 0.75, '3) ' + str(self.three_hs[2]), ORANGE)

        self.objects.append(self.text)
        self.objects.append(self.first_record_text)
        self.objects.append(self.second_record_text)
        self.objects.append(self.third_record_text)
        
        
        self.update_start_time()

    def get_gameover_text_formatted(self):
        return self.text_format.format(self.seconds_to_end - self.last_seconds_passed)

    def on_activate(self):
        self.update_start_time()
        self.update_highscores()
        self.update_highscores_text()

    def update_start_time(self):
        self.time_start = datetime.now()

    def update_highscores(self):
        with open('highscores.txt', 'r') as hs_file:
            hs_arr = sorted([round(float(i), 2) for i in hs_file.readlines()], reverse=True)
            self.three_hs = hs_arr[0:3]
        
    def update_highscores_text(self):
        self.first_record_text.update_text('1) ' + str(self.three_hs[0]))
        self.second_record_text.update_text('2) ' + str(self.three_hs[1]))
        self.third_record_text.update_text('3) ' + str(self.three_hs[2]))

    def process_logic(self):
        time_current = datetime.now()
        seconds_passed = (time_current - self.time_start).seconds
        if self.last_seconds_passed != seconds_passed:
            self.last_seconds_passed = seconds_passed
            self.objects[0].update_text(self.get_gameover_text_formatted())
        if seconds_passed >= self.seconds_to_end:
            self.game.set_scene(self.game.SCENE_MENU)
