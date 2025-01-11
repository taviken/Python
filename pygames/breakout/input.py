import pygame
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN, K_a, K_s, K_d, K_w
from collections import namedtuple

directions = namedtuple("directions", ["up", "down", "left", "right"])


class Input:
    @property
    def directions(self) -> directions:
        key = pygame.key.get_pressed()
        left = any((key[K_LEFT], key[K_a]))
        right = any((key[K_RIGHT], key[K_d]))
        up = any((key[K_UP], key[K_w]))
        down = any((key[K_DOWN], key[K_d]))
        return directions(up, down, left, right)
