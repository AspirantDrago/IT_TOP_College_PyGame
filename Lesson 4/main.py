import pygame as pg

from config import Config
import src.utils as utils

pg.init()
screen = pg.display.set_mode(Config.SIZE)


def main(screen: pg.Surface):
    clock = pg.time.Clock()
    background = 'blue'

    player_images = utils.load_many_images('player.png', 2, 2, None, (100, 100))
    mega_boss_images = utils.load_many_images('mega_boss.png', 2, 2, None, (100, 100))
    boss_1_images = utils.load_many_images('boss_1.png', 2, 2, None, (100, 100))
    boss_2_images = utils.load_many_images('boss_2.png', 2, 2, None, (100, 100))
    boss_3_images = utils.load_many_images('boss_3.png', 2, 2, None, (100, 100))
    boss_4_images = utils.load_many_images('boss_4.png', 2, 2, None, (100, 100))
    i = 0

    running = True
    while running:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        screen.fill(background)

        i += 1
        screen.blit(player_images[i // 10 % 4], (0, 0))
        screen.blit(mega_boss_images[i // 10 % 4], (100, 0))
        screen.blit(boss_1_images[i // 10 % 4], (200, 0))
        screen.blit(boss_2_images[i // 10 % 4], (300, 0))
        screen.blit(boss_3_images[i // 10 % 4], (400, 0))
        screen.blit(boss_4_images[i // 10 % 4], (500, 0))

        pg.display.flip()
        clock.tick(Config.FPS)


if __name__ == '__main__':
    main(screen)
    pg.quit()
