import random

import pygame as pg

from src.character import CharacterEmotion
from src.player import *
from src.suhareke import Suhareke
from src.scene import SceneManager, SkipException


def start_scene(screen: pg.Surface):
    def tryaska(self, *args, **kwargs):
        self.rect.move_ip(0, random.randint(-2, 2))


    background = 'black'
    try:
        pg.mixer.music.load('data/sounds/sound_1.mp3')
        pg.mixer.music.play()
        for x in (0, 200, 400):
            with SceneManager(screen, 1.1, background) as scene:
                scene.add(Player(size=(400 + 2 * x, 400 + 2 * x)), (100 - x, 100 - x))
            with SceneManager(screen, 1.1, background) as scene:
                scene.add(Suhareke(size=(400 + 2 * x, 400 + 2 * x)), (100 - x, 100 - x))
        pg.mixer.music.stop()
        with SceneManager(screen, 10, background) as scene:
            random.seed(8)
            p = Player(size=(400 , 400))
            p.set_emotion(CharacterEmotion.SMILE)
            scene.add(p, (0, 100))
            suh = Suhareke(size=(200, 200))
            scene.add(suh, (100, 330))
            scene.set_update(suh, tryaska)

            bosses = [
                BossRegina(size=(120, 120)),
                BossRamzes(size=(120, 120)),
                BossMarina(size=(120, 120)),
                BossBerto(size=(120, 120)),
                BossRosa(size=(120, 120)),
                BossMegaMaga(size=(120, 120)),
            ]
            for i in range(3):
                bosses[i].set_emotion(CharacterEmotion.ANGER)
                start = (600 + 100 * i, 100)
                scene.add(bosses[i], start)
                scene.set_animation(bosses[i], start, (300 + 100 * i, start[1]), 4 + i, 5 + i)
            for i in range(3):
                bosses[i + 3].set_emotion(CharacterEmotion.ANGER)
                start = (600 + 100 * i, 200)
                scene.add(bosses[i + 3], start)
                scene.set_animation(bosses[i + 3], start, (300 + 100 * i, start[1]), 7 + i, 9 + i)
        with SceneManager(screen, 15, background) as scene:
            scene.add(p)
            p.set_emotion(CharacterEmotion.ASTONISHMENT)
            scene.set_animation(p, p.rect.topleft, (p.rect.x - 420, p.rect.y), 1, 4)
            for i in range(6):
                scene.add(bosses[i])
                scene.set_animation(
                    bosses[i],
                    bosses[i].rect.topleft,
                    (bosses[i].rect.x - 1000, bosses[i].rect.y),
                    4 + i / 2, 5 + i / 2)

    except SkipException:
        return