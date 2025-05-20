from .character import Character


class Player(Character):
    IMAGE_PATH = 'player.png'


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
