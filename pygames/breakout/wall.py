from dataclasses import dataclass
from .colors import RED_WINE, GRASS_GREEN, SKY_BLUE, Rgba
import pygame


@dataclass
class Block:
    rect: pygame.Rect
    strength: int


@dataclass
class Wall:
    rows: int
    columns: int
    screen_width: int
    height: int = 50

    def __post_init__(self):
        self.block_colors: dict = {
            "red": RED_WINE.rgb,
            "green": GRASS_GREEN.rgb,
            "blue": SKY_BLUE.rgb,
        }
        self.width = self.screen_width // self.columns
        self.blocks = []

        for row in range(self.rows):
            block_row = []
            for col in range(self.columns):
                # generate x,y positions for each block
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)

                # assign brick 'strength'
                if row < 2:
                    strength = 3
                elif row < 4:
                    strength = 2
                elif row < 6:
                    strength = 1

                block_row.append(Block(rect=rect, strength=strength))
            self.blocks.append(block_row)

    def draw_wall(self, screen: pygame.Surface, bg_color: Rgba):
        for row in self.blocks:
            for block in row:
                if block.strength == 3:
                    block_color = self.block_colors["blue"]
                elif block.strength == 2:
                    block_color = self.block_colors["green"]
                else:
                    block_color = self.block_colors["red"]
                pygame.draw.rect(screen, block_color, block.rect)
                # draw 'border' using background color
                pygame.draw.rect(screen, bg_color.rgb, (block.rect), 2)
