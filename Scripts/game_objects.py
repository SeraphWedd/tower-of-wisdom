'''
File contraining all inherent game class objects.
'''

import pygame as pg
import numpy as np

class GameObject(object):
    '''
    The base GameObject class.
    Position x and y are held in a global numpy array within
    the main game engine.

    Each GameObject instance will hold a unique index identifier
    indicating their position on the numpy array.
    '''
    def __init__(self, GE, identity=0, floor=0):
        self.i = identity
        self.floor = floor
        self.game = GE
        self.image = pg.surface.Surface((64, 64)).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self, dt):
        self.rect.center = (self.game.x[self.floor, self.i],
                            self.game.y[self.floor, self.i])

    def draw(self, screen):
        screen.blit(self.image, self.rect)
