'''
File contraining all inherent game class objects.
'''

import pygame as pg

class GameObject(object):
    '''
    The base GameObject class.
    Position x and y are held in a global numpy array within
    the main game engine.

    Each GameObject instance will hold a unique index identifier
    indicating their position on the numpy array.
    '''
    def __init__(self, GE, identity=0):
        self.i = ident
        self.game = GE
        self.image = None
        self.rect = None

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
