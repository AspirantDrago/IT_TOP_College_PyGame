from __future__ import annotations

from pygame.sprite import Sprite, Group

from config import Config


class Camera:

    def __init__(self):
        self._group = Group()
        self._target: Sprite | None = None
        self._position = 0, 0
        self._inertion: float = 0.99 ** Config.FPS

    def update(self) -> None:
        if self._target is not None:
            dx = self._target.rect.centerx - self._position[0]
            dy = self._target.rect.centery - self._position[1]
            dx *= self._inertion
            dy *= self._inertion
            for sprite in self._group:
                sprite.rect.move_ip(-dx, -dy)

    def set_position(self, x: int, y: int) -> Camera:
        self._position = x, y
        return self

    def set_target(self, target: Sprite | None) -> Camera:
        self._target = target
        return self

    @property
    def group(self) -> Group:
        return self._group

    def add(self, obj: Sprite | Group) -> Camera:
        if isinstance(obj, Sprite):
            self._group.add(obj)
        elif isinstance(obj, Group):
            for sprite in obj:
                self._group.add(sprite)
        return self

