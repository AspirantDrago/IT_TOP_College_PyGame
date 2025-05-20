import pygame as pg

from .utils import load_image


class Suhareke(pg.sprite.Sprite):
    IMAGE = load_image('suhareke.png', None)

    def __init__(self, *args):
        super().__init__(*args)
        self.image = self.IMAGE
        self.rect = self.image.get_rect()
