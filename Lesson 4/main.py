import pygame as pg

from config import Config

pg.init()
pg.mixer.init()
screen = pg.display.set_mode(Config.SIZE)

import src.utils as utils
from src.player import Player
from src.camera import Camera
from scenes.start_scene import start_scene


def main(screen: pg.Surface) -> None:
    clock = pg.time.Clock()
    camera = Camera()
    background = 'black'

    level = utils.load_map('map.txt')
    groups = utils.read_map(level)
    group_people = pg.sprite.Group()
    player = Player(size=(Config.TILE_SIZE * 3, Config.TILE_SIZE * 3))
    player.rect.move_ip(Config.TILE_SIZE * 33, Config.TILE_SIZE * 43)
    group_people.add(player)
    camera\
        .add(group_people)\
        .add(groups.all_tile)\
        .set_target(player)\
        .set_position(Config.WIDTH // 2, Config.HEIGHT // 2)

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        screen.fill(background)
        groups.all_tile.draw(screen)
        group_people.update(events=events, groups=groups)
        camera.update()
        group_people.draw(screen)

        pg.display.flip()
        clock.tick(Config.FPS)
        print(clock.get_fps())



if __name__ == '__main__':
    # start_scene(screen)
    main(screen)
    pg.quit()
