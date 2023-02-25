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


class NeonRect():
    def __init__(self, color, rect, n=10, size=1, outline=0):
        self.color = self.init_color(color)
        self.rect = rect
        self.n = n
        self.size = size
        self.outline = outline

        self.pos = None
        self.surface = self.get_neon_surface()

    def init_color(self, color):
        color = list(color)
        if len(color) < 4:
            color.append(0)
        color[3] = 100
        return color

    def get_neon_surface(self):
        pos = [self.rect.x, self.rect.y]
        rect = pygame.Rect(self.rect)
        rect.x = 0 + self.size * self.n
        rect.y = 0 + self.size * self.n

        color = list(self.color)
        w = (self.size * self.n * 2) + rect.w
        h = (self.size * self.n * 2) + rect.h
        surface = pygame.Surface((w, h), pygame.SRCALPHA)

        alpha_incr = 100 / self.n
        for i in range(self.n):
            pos[0] -= self.size
            pos[1] -= self.size
            rect.x -= self.size
            rect.y -= self.size
            rect.w += 2 * self.size
            rect.h += 2 * self.size

            pygame.draw.rect(surface, color, rect, self.size)
            color[3] -= alpha_incr

        if self.outline != 0:
            color[3] = 100
            rect = pygame.Rect(self.rect)
            rect.x = 0 + self.size * self.n
            rect.y = 0 + self.size * self.n
            for i in range(self.n):
                rect.x += self.size
                rect.y += self.size
                rect.w -= 2 * self.size
                rect.h -= 2 * self.size

                pygame.draw.rect(surface, color, rect, self.size)
                color[3] -= alpha_incr

        rect = pygame.Rect(self.rect)
        rect.x = 0 + self.size * self.n
        rect.y = 0 + self.size * self.n
        # pygame.draw.rect(surface, self.color, rect, self.outline)
        self.pos = list(pos)
        return surface

    def draw(self, display, offset=[0, 0]):
        pos = [self.pos[0] + offset[0], self.pos[1] + offset[1]]
        display.blit(self.surface, pos)

        x = pos[0] + self.size * self.n
        y = pos[1] + self.size * self.n
        rect = pygame.Rect(x, y, self.rect.w, self.rect.h)
        pygame.draw.rect(display, self.color, rect, self.outline)


class NeonLine():
    def __init__(self, color, start, end, display_size, n=10, size=1, pos=[0, 0]):
        self.color = self.init_color(color)
        self.start, self.end = self.init_coord(start, end)
        self.vect = pygame.Vector2(self.end[0] - self.start[0], end[1] - start[1])
        self.display_size = display_size
        self.n = n
        self.size = size

        self.surface = self.get_neon_surface()
        self.pos = pos

    def init_coord(self, start, end):
        if start[0] > end[0]:
            temp = list(start)
            start = list(end)
            end = list(temp)
        return start, end

    def init_color(self, color):
        color = list(color)
        if len(color) < 4:
            color.append(0)
        color[3] = 100
        return color

    def get_neon_surface(self):
        alpha_incr = 100 / self.n
        surface = pygame.Surface(self.display_size, pygame.SRCALPHA)
        color = list(self.color)

        for i in range(self.n):
            x, y = list(self.start)
            x += i
            y -= i
            pygame.draw.line(surface, color, (x, y), (x + self.vect.x, y + self.vect.y))

            x, y = list(self.start)
            x -= i
            y += i
            pygame.draw.line(surface, color, (x, y), (x + self.vect.x, y + self.vect.y))
            color[3] -= alpha_incr
        return surface

    def draw(self, display, offset=[0, 0]):
        pos = [self.pos[0] + offset[0], self.pos[1] + offset[1]]
        display.blit(self.surface, pos)
        pygame.draw.line(display, self.color, self.start, self.end)