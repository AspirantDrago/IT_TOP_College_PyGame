import pygame as pg

from .character import Character
from .utils import GroupTile


class Player(Character):
    IMAGE_PATH = 'player.png'
    SPEED = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mask = pg.mask.from_surface(self.image)

    def update(
            self,
            *args,
            groups: GroupTile | None = None,
            **kwargs):
        dx = dy = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            dx -= self.SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            dx += self.SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            dy -= self.SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            dy += self.SPEED
        self.rect.move_ip(dx, 0)
        if groups and pg.sprite.spritecollideany(self, groups.obstacle, pg.sprite.collide_mask):
            self.rect.move_ip(-dx, -0)
        self.rect.move_ip(0, dy)
        if groups and pg.sprite.spritecollideany(self, groups.obstacle, pg.sprite.collide_mask):
            self.rect.move_ip(0, -dy)



class Boss(Character):
    ...


class BossRegina(Boss):
    IMAGE_PATH = 'boss_1.png'


class BossRamzes(Boss):
    IMAGE_PATH = 'boss_2.png'


class BossMarina(Boss):
    IMAGE_PATH = 'boss_3.png'


class BossBerto(Boss):
    IMAGE_PATH = 'boss_4.png'


class BossRosa(Boss):
    IMAGE_PATH = 'boss_5.png'


class BossMegaMaga(Boss):
    IMAGE_PATH = 'mega_boss.png'
