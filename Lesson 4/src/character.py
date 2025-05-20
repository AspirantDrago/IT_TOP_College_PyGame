from enum import IntEnum

import pygame as pg

from .utils import load_many_images


class CharacterEmotion(IntEnum):
    NORMAL = 0
    SMILE = 1
    ANGER = 2
    ASTONISHMENT = 3


class Character(pg.sprite.Sprite):
    IMAGE_PATH: str | None = None
    IMAGES: list[pg.Surface] = []

    def __init__(self, *args):
        super().__init__(*args)
        self.class_init()
        self.emotion = CharacterEmotion.NORMAL
        self.image: pg.Surface = self.IMAGES[self.emotion]
        self.rect = self.image.get_rect()

    @classmethod
    def class_init(cls):
        if not cls.IMAGES:
            cls.IMAGES = load_many_images(cls.IMAGE_PATH, 2, 2, None, (600, 600))
