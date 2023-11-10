import pygame as pg
import sys
from particle import *
from settings import *


class Demolish:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

