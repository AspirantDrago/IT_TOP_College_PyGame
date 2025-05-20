import time
import types
from typing import Callable

import pygame as pg

from config import Config

type Coords = tuple[int, int]


class SkipException(Exception):
    ...


class SceneManager:
    def __init__(self, surface: pg.Surface, duration: float, background: pg.Color):
        self.surface = surface
        self.duration = duration
        self.background = background
        self.clock = pg.time.Clock()
        self.group = pg.sprite.Group()

    def add(self, sprite: pg.sprite.Sprite, position: Coords = (0, 0)) -> None:
        self.group.add(sprite)
        sprite.rect.move_ip(position)

    def __enter__(self):
        self.time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.time
        while t < self.duration:
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
            self.group.update(time=t)
            self.group.draw(self.surface)
            pg.display.flip()
            self.clock.tick(Config.FPS)
            t = time.time() - self.time

    @staticmethod
    def set_update(sprite: pg.sprite.Sprite, callback: Callable):
        sprite.update = types.MethodType(callback, sprite)

    @staticmethod
    def set_animation(
            sprite: pg.sprite.Sprite,
            start_pos: Coords,
            end_pos: Coords,
            start_time: float | int,
            end_time: float | int,
    ) -> None:
        def _update(self: pg.sprite.Sprite, time: float | int) -> None:
            if start_time <= time <= end_time:
                x1, y1 = start_pos
                x2, y2 = end_pos
                x = x1 + (time - start_time) * (x2 - x1) / (end_time - start_time)
                y = y1 + (time - start_time) * (y2 - y1) / (end_time - start_time)
                self.rect.x = x
                self.rect.y = y

        SceneManager.set_update(sprite, _update)
