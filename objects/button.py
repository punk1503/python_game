from third_party.button import Button
from constants import BLUE, GREEN, BLACK, ORANGE
from objects.base import DrawableObject


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