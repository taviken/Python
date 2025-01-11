from dataclasses import dataclass
import Box2D
from Box2D.b2 import world, polygonShape, staticBody, dynamicBody


class World:
    def __init__(self):
        self.world = world(gravity=(0, 0), doSleep=True)
        self.world.CreateStaticBody(position=(0, 1))


@dataclass
class Point2:
    x: float
    y: float


@dataclass
class Circle:
    coord: Point2
    radius: float
