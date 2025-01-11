from dataclasses import dataclass
from .physics import Point2, Circle
from pygame.locals import Rect
from .colors import PADDLE_COLOR, PADDLE_OUTLINE
import pygame
from .paddle import Paddle
from .wall import Wall, Block


@dataclass
class Ball:
    radius: float
    x: float
    y: float
    screen_width: int
    screen_height: int
    collison_threshold: int
    speed_max: int

    def __post_init__(self):
        self.coordinate = Point2(self.x - self.radius, self.y)
        self.circle: Circle = Circle(self.coordinate, self.radius)
        self.rect = Rect(
            self.coordinate.x, self.coordinate.y, self.radius * 2, self.radius * 2
        )
        self.speed_x = 4
        self.speed_y = -4
        self.out_of_bounds = False

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            screen,
            PADDLE_COLOR.rgb,
            (self.rect.x + self.radius, self.rect.y + self.radius),
            self.radius,
        )
        pygame.draw.circle(
            screen,
            PADDLE_OUTLINE.rgb,
            (self.rect.x + self.radius, self.rect.y + self.radius),
            self.radius,
            3,
        )

    def _update_speed_from_block(self, block: Block):
        if (
            abs(self.rect.bottom - block.rect.top) < self.collison_threshold
            and self.speed_y > 0
        ):
            self.speed_y *= -1

        if (
            abs(self.rect.top - block.rect.bottom) < self.collison_threshold
            and self.speed_y < 0
        ):
            self.speed_y *= -1

        if (
            abs(self.rect.right - block.rect.left) < self.collison_threshold
            and self.speed_x > 0
        ):
            self.speed_x *= -1

        if (
            abs(self.rect.left - block.rect.right) < self.collison_threshold
            and self.speed_x < 0
        ):
            self.speed_x *= -1

    def move(self, paddle: Paddle, wall: Wall):

        # block collision check
        for row in wall.blocks:
            for block in row:
                if self.rect.colliderect(block.rect):
                    if block.strength > 0:
                        self._update_speed_from_block(block)
                    block.strength -= 1
                    break

        # wall collision check
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed_x *= -1
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > self.screen_height:
            self.out_of_bounds = True

        # padlle collision check
        if self.rect.colliderect(paddle.rect):
            if (
                abs(self.rect.bottom - paddle.rect.top) < self.collison_threshold
                and self.speed_x > 0
            ):
                self.speed_y *= -1
                self.speed_x += min(self.speed_x, self.speed_max) * paddle.direction

        # block collision check

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
