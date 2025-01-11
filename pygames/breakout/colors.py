from dataclasses import dataclass


@dataclass
class Rgba:
    red: int
    green: int
    blue: int
    alpha: int = 0

    @property
    def rgb(self):
        return self.red, self.green, self.blue

    @property
    def rgba(self):
        return self.red, self.green, self.blue, self.alpha


BLACK = Rgba(0, 0, 0, 1)
RED = Rgba(255, 0, 0, 1)
GREEN = Rgba(0, 255, 0, 1)
BLUE = Rgba(0, 0, 255, 1)

RED_WINE = Rgba(242, 85, 96)
GRASS_GREEN = Rgba(86, 174, 87)
SKY_BLUE = Rgba(69, 177, 232)

PADDLE_COLOR = Rgba(142, 135, 123)
PADDLE_OUTLINE = Rgba(100, 100, 100)
