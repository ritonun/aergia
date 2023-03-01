import pygame
from .graphics import resize_surface_to_surface, resize_surface_to_display_keep_ratio
from .var import *
from .debug import show_fps


class App:
    def __init__(self, size=(1000, 600)):
        self.running = False
        self.display = None
        self.scene_manager = None
        self.ressource_manager = None
        self.size = self.width, self.height = size
        self.caption = "Aergia Engine Sandbox"
        self.icon = None
        self.keep_ratio_when_resizing = False
        self.FPS = 60
        self.screen_ratio = 1

        self.dev = False

    def init_app(self):
        pygame.init()

        self.display = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
        screen_size = [round(self.display.get_width() / self.screen_ratio),
                       round(self.display.get_height() / self.screen_ratio)]
        self.screen = pygame.Surface(screen_size, pygame.SRCALPHA)
        self.screen_pos = [0, 0]
        pygame.display.set_caption(self.caption)
        if self.icon is not None:
            pygame.display.set_icon(self.icon.convert_alpha())

        self.clock = pygame.time.Clock()

        self.running = True

    def events_handling(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            if self.dev:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
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
            events = pygame.event.get()

            if self.dev:
                show_fps(self.clock, self.caption)

            self.events_handling(events)

            if self.scene_manager is not None:
                self.display.fill(BLACK)
                self.screen.fill(BLACK)
                self.scene_manager.run_scene(events, self.screen, dt)
            else:
                self.update_app(dt)
                self.render_app()

            # handle screen resize
            if self.keep_ratio_when_resizing:
                offset_screen = resize_surface_to_display_keep_ratio(self.display, self.screen, return_surf=True)
                self.display.blit(offset_screen[0], offset_screen[1])
            else:
                self.display.blit(resize_surface_to_surface(self.display, self.screen), self.screen_pos)

            pygame.display.update()
        self.cleanup()
