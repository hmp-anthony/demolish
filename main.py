import pygame as pg
import sys
from particle import *
from settings import *


class Demolish:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill('black')
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    sim = Demolish()
    sim.run()
