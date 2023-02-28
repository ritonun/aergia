import pygame
from .graphics import resize_surface_to_surface, resize_surface_to_display_keep_ratio
from .var import *


class App:
    def __init__(self, size=(1000, 600)):
        self.running = False
        self.display = None
        self.size = self.width, self.height = size
        self.caption = "Aergia Engine Sandbox"
        self.icon = None
        self.keep_ratio_when_resizing = False
        self.FPS = 60

    def init_app(self):
        pygame.init()

        if self.icon is not None:
            pygame.display.set_icon(self.icon)

        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.screen = pygame.Surface(self.display.get_size(), pygame.SRCALPHA)
        self.screen_pos = [0, 0]
        pygame.display.set_caption(self.caption)

        self.clock = pygame.time.Clock()

        self.running = True

    def events_handling(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def update_app(self, dt):
        pass

    def render_app(self):
        self.display.fill(BLACK)
        self.screen.fill(WHITE)

    def cleanup(self):
        pygame.quit()

    def mainloop(self):
        if self.init_app() is False:
            self.running = False

        while(self.running):
            dt = self.clock.tick(self.FPS) / 1000
            for event in pygame.event.get():
                self.events_handling(event)
            self.update_app(dt)
            self.render_app()

            if self.keep_ratio_when_resizing:
                offset_screen = resize_surface_to_display_keep_ratio(self.display, self.screen, return_surf=True)
                self.display.blit(offset_screen[0], offset_screen[1])
            else:
                self.display.blit(resize_surface_to_surface(self.display, self.screen), self.screen_pos)

            pygame.display.update()
        self.cleanup()
