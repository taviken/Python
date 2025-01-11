import pygame
from pygame.locals import *
from .colors import Rgba
from .wall import Wall
from .paddle import Paddle
from .input import Input


class Main:
    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        rows: int,
        columns: int,
        caption: str = "Breakout",
    ):
        pygame.init()
        self.running = False
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(caption)
        self.background_color = Rgba(234, 218, 184)

        self.rows = rows
        self.columns = columns
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.wall = Wall(rows, columns, screen_width)
        self.paddle = Paddle(20, screen_width, screen_height, columns, 10)
        self.input = Input()

    def run(self):
        self.running = True
        while self.running:

            self.clock.tick(self.fps)

            self.screen.fill(self.background_color.rgb)
            self.wall.draw_wall(self.screen, self.background_color)
            self.paddle.draw(self.screen)
            self.paddle.move(self.input)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()
