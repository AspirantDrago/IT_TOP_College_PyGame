import pygame as pg

from .utils import load_image


class Suhareke(pg.sprite.Sprite):
    IMAGE = load_image('suhareke.png', None)

    def __init__(self, *args, size: tuple[int, int] | None = None):
        super().__init__(*args)
        self.image = self.IMAGE
        if size:
            self.image = pg.transform.scale(self.image, size).convert_alpha()
        self.rect = self.image.get_rect()
