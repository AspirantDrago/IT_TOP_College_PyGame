import time

import pygame as pg

from config import Config


class SkipException(Exception):
    ...


class SceneManager:
    def __init__(self, surface: pg.Surface, duration: float, background: pg.Color):
        self.surface = surface
        self.duration = duration
        self.background = background
        self.clock = pg.time.Clock()
        self.group = pg.sprite.Group()

    def add(self, sprite: pg.sprite.Sprite, position: tuple[int, int] = (0, 0)) -> None:
        self.group.add(sprite)
        sprite.rect.move_ip(position)

    def __enter__(self):
        self.time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        while time.time() - self.time < self.duration:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    raise SkipException()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        raise SkipException()
                    elif event.key == pg.K_SPACE:
                        return
            self.surface.fill(self.background)
            self.group.update()
            self.group.draw(self.surface)
            pg.display.flip()
            self.clock.tick(Config.FPS)
