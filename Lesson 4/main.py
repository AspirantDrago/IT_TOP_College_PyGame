import pygame as pg

from config import Config

pg.init()
screen = pg.display.set_mode(Config.SIZE)

from src.player import Player
from src.suhareke import Suhareke
from src.scene import SceneManager, SkipException



def main(screen: pg.Surface):
    background = 'blue'
    try:
        with SceneManager(screen, 2, background) as scene:
            scene.add(Player(size=(200, 100)))
        with SceneManager(screen, 2, background) as scene:
            scene.add(Suhareke(), (200, 200))

    except SkipException:
        return


if __name__ == '__main__':
    main(screen)
    pg.quit()
