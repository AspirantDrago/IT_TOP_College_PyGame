import pygame as pg

from config import Config

pg.init()
pg.mixer.init()
screen = pg.display.set_mode(Config.SIZE)

import src.utils as utils
from src.player import Player
from scenes.start_scene import start_scene


def main(screen: pg.Surface) -> None:
    clock = pg.time.Clock()
    background = 'black'

    level = utils.load_map('map.txt')
    groups = utils.read_map(level)
    group_people = pg.sprite.Group()
    player = Player(size=(Config.TILE_SIZE * 3, Config.TILE_SIZE * 3))
    player.rect.move_ip(Config.TILE_SIZE * 2, Config.TILE_SIZE * 2)
    group_people.add(player)

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        screen.fill(background)
        groups.all_tile.draw(screen)
        group_people.update(events=events, groups=groups)
        group_people.draw(screen)

        pg.display.flip()
        clock.tick(Config.FPS)



if __name__ == '__main__':
    start_scene(screen)
    main(screen)
    pg.quit()
