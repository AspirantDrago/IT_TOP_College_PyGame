import time

import pygame as pg

from config import Config

pg.init()
screen = pg.display.set_mode(Config.SIZE)

from src.player import Player
from src.suhareke import Suhareke


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
                elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    raise SkipException()
            self.surface.fill(self.background)
            self.group.update()
            self.group.draw(self.surface)
            pg.display.flip()
            self.clock.tick(Config.FPS)


def main(screen: pg.Surface):
    clock = pg.time.Clock()
    background = 'blue'
    all_sprites = pg.sprite.Group()
    player = Player(all_sprites)
    suhareke = Suhareke(all_sprites)
    with SceneManager(screen, 2, background) as scene:
        scene.add(player)
    with SceneManager(screen, 2, background) as scene:
        scene.add(suhareke, (200, 200))

    # running = True
    # while running:
    #     events = pg.event.get()
    #     for event in events:
    #         if event.type == pg.QUIT:
    #             running = False
    #     screen.fill(background)
    #
    #     all_sprites.draw(screen)
    #     pg.display.flip()
    #     clock.tick(Config.FPS)


if __name__ == '__main__':
    main(screen)
    pg.quit()
