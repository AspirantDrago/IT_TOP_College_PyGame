import pygame as pg

from config import Config

pg.init()
pg.mixer.init()
screen = pg.display.set_mode(Config.SIZE)

from scenes.start_scene import start_scene


if __name__ == '__main__':
    start_scene(screen)
    pg.quit()
