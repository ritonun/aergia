import random
import pygame
from .tools import Animation


class ScreenShake:
    def __init__(self, tick_limit=30, random_range=5):
        self.offset = [0.0, 0.0]
        self.counting = False
        self.tick = 0
        self.tick_limit = tick_limit
        self.random_range = random_range

    def reset(self):
        self.offset = [0.0, 0.0]
        self.counting = False
        self.count_up = True

    def start(self):
        if self.counting is False:
            self.count_up = True
            self.counting = True
            self.offset = [1.0, 1.0]

    def update(self):
        if self.counting:
            self.offset[0] = 0.0
            self.offset[1] = 0.0
            x = random.randint(0, self.random_range)
            y = random.randint(0, self.random_range)
            x -= self.random_range / 2
            y -= self.random_range / 2
            self.offset[0] = x
            self.offset[1] = y

            self.tick += 1
            if self.tick >= self.tick_limit:
                self.tick = 0
                self.counting = False
                self.reset()

    def get_offset(self):
        return [int(self.offset[0]), int(self.offset[1])]


class VFX:
    """
    vfxs_data: dict with info to create anim -> vfxs_data[key] = [list_img/tileset, speed, bool: loop]
    """

    def __init__(self, vfxs_data):
        self.vfxs_data = vfxs_data
        self.animation_group = pygame.sprite.Group()

    def add_anim(self, animation_key, x, y):
        vfx = self.vfxs_data[animation_key]
        animation = Animation(x, y, vfx[0], vfx[1], vfx[2])
        self.animation_group.add(animation)

    def update(self):
        self.animation_group.update()

    def draw(self, display):
        self.animation_group.draw(display)
