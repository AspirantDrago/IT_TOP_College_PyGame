import time

import pygame as pg

from config import Config

pg.init()
screen = pg.display.set_mode(Config.SIZE)

from src.player import Player
from src.suhareke import Suhareke
from src.scene import SceneManager, SkipException



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
