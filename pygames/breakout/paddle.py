from dataclasses import dataclass
from pygame.locals import Rect
from .input import Input
from .colors import PADDLE_COLOR, PADDLE_OUTLINE
import pygame


@dataclass
class Paddle:
    height: int
    screen_width: int
    screen_height: int
    columns: int
    speed: int

    def __post_init__(self):
        self.width = int(self.screen_width / self.columns)
        self.x = int((self.screen_width / 2) - (self.width / 2))
        self.y = self.screen_height - (self.height * 2)
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0

    def move(self, controller: Input):
        # reset direction
        self.direction = 0
        movement = controller.directions
        if movement.left and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if movement.right and self.rect.right < self.screen_width:
            self.rect.x += self.speed
            self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, PADDLE_COLOR.rgb, self.rect)
        pygame.draw.rect(screen, PADDLE_OUTLINE.rgb, self.rect, 3)
