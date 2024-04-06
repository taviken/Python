import pygame as pg

import engine


class App:
    """
        Calls high level control functions (handle input, draw scene etc)
    """

    def __init__(self, screen_width=800, screen_height=600):
        pg.init()
        self.screenWidth = screen_width
        self.screenHeight = screen_height
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)

        pg.display.set_mode((self.screenWidth, self.screenHeight), pg.OPENGL | pg.DOUBLEBUF)
        pg.display.set_caption(f"Python OpenGl")

        self.engine = engine.Engine(screen_width=screen_width,
                                    screen_height=screen_height)

    def main_loop(self):
        running = True
        while running:
            # events
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        running = False
            self.engine.render()
            pg.display.flip()

        self.quit()

    @staticmethod
    def quit():
        pg.quit()
