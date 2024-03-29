from random import randint

import pygame

from objects.ball import BallObject
from objects.text import TextObject
from scenes.base import BaseScene
from objects.platform import Platform


class GameScene(BaseScene):
    max_collisions = 15
    balls_count = 3

    def __init__(self, game):
        super().__init__(game)
        self.balls = [BallObject(game) for _ in range(GameScene.balls_count)]
        self.platform = Platform(game, 'images/brick.png', game.width//2 + 50, game.height - 50, 4)
        self.collision_count = 0
        self.score = 0
        self.hs_arr = []
        self.update_highs_scores()
        self.status_text = TextObject(self.game, 0, 0, self.get_collisions_text(), (255, 255, 255))
        self.score_text = TextObject(self.game, 0, 0, self.get_score_text(), (255, 255, 255))
        self.status_text.move(10, 10)
        self.objects += self.balls
        self.objects.append(self.status_text)
        self.objects.append(self.score_text)
        self.objects.append(self.platform)

        self.reset_balls_position()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.set_scene(self.game.SCENE_MENU)
        self.platform.process_event(event)

    def get_random_position(self, radius):
        return randint(10, self.game.width - radius*2 - 10), randint(10, self.game.height - radius*2 - 10)

    def set_random_position(self, ball):
        pos = self.get_random_position(ball.radius)
        ball.move(*pos)

    def reset_balls_position(self):
        for ball in self.balls:
            ball.move(self.game.width, self.game.height)

    def set_random_unique_position(self):
        for index in range(len(self.balls)):
            other_rects = [self.balls[i].rect for i in range(len(self.balls)) if i != index]
            self.set_random_position(self.balls[index])
            while self.balls[index].rect.collidelist(other_rects) != -1:
                self.set_random_position(self.balls[index])

    def on_activate(self):
        self.collision_count = 0
        self.score = 0
        self.reset_balls_position()
        self.set_random_unique_position()
        self.status_text.update_text(self.get_collisions_text())
        self.status_text.move(10, 10)
        self.score_text.update_text(self.get_score_text())
        self.score_text.move(10, 40)

    def check_ball_intercollisions(self):
        for i in range(len(self.balls) - 1):
            for j in range(i + 1, len(self.balls)):
                if self.balls[i].collides_with(self.balls[j]):
                    self.balls[i].bounce(self.balls[j])

    def get_collisions_text(self):
        return 'Wall collisions: {}/{}'.format(self.collision_count, GameScene.max_collisions)
    
    def get_score_text(self):
        return 'Score: ' + str(int(self.score))

    def check_ball_edge_collision(self):
        for ball in self.balls:
            if ball.edge_collision():
                self.collision_count += 1
                self.status_text.update_text(self.get_collisions_text())
                self.status_text.move(10, 10)

    def increase_score(self):
        self.score += 0.01
        self.score_text.update_text(self.get_score_text())
        self.score_text.move(10, 40)

    def add_new_highscore(self):
        with open('highscores.txt', 'a') as hs_file:
            hs_file.writelines('\n' + str(round(self.score, 2)))
        print('Highscore has been written')

    def update_highs_scores(self):
        with open('highscores.txt', 'r') as hs_file:
            self.hs_arr = [round(float(i), 2) for i in hs_file.readlines()]
    
    def check_game_over(self):
        if self.collision_count >= GameScene.max_collisions:
            self.add_new_highscore()
            self.update_highs_scores()
            self.game.set_scene(self.game.SCENE_GAMEOVER)
    
    def check_ball_platform_collision(self):
        for ball_ndx in range(len(self.balls)):
            self.balls[ball_ndx].check_platform_collision(self.platform)
        
    def process_logic(self):
        super().process_logic()
        self.increase_score()
        self.check_ball_edge_collision()
        self.check_ball_intercollisions()
        self.check_ball_platform_collision()
        self.platform.move()
        self.check_game_over()
