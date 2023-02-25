import pygame


def resize_surface_to_display_keep_ratio(display, surface):
    """
    Scale a surface to display with black strip to keep the ratio
    """
    offset = [0, 0]
    w, h = display.get_size()
    screen_w, screen_h = surface.get_size()
    screen_ratio = screen_w / screen_h

    size = (w, w / screen_ratio)
    if size[0] <= w and size[1] <= h:
        if size[0] == w:
            offset_h = (h - size[1]) / 2
            offset[1] = int(offset_h)
    else:
        size = (h * screen_ratio, h)
        if size[1] == h:
            offset_w = (w - size[0]) / 2
            offset[0] = int(offset_w)

    return size, offset


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
