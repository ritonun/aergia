import pygame
from .graphics import resize_surface_to_surface, resize_surface_to_display_keep_ratio
from .var import *
from .debug import show_fps


class App:
    """Class to handle the app itself.

    Attributes:
        caption (str): Caption of the app, displayed at the top of the window
        clock (Clock): clock that handle fps in the game
        dev (bool): debug mode for special options
        display (surface): app display configured with pygame.set_mode()
        display_filler_color (tuple): RGB color
        FPS (int): number of frame per second
        icon (surface): default is None, else is a image (max 32x32) that serve as an icon
        keep_ratio_when_resizing (bool): If true, in case of a resize of the display,
                                         the draw surface is scaled to keep its ratio and avoid deformation.
        ressource_manager (object): An instance of the RessourceManager() class
        running (bool): If set to false, the app quit.
        scene_manager (object): An instance of the SceneManager() class
        screen (surface): Surface on which everything is drawed on, before being scaled to display size
        screen_filler_color (tuple): Background color of the screen surface
        screen_pos (list): Screen pos (should be [0, 0] unless for special effect like a screen shake)
        screen_ratio (int): Ratio between the screen size and the dimesion of the app
        size (tuple): Size of the display (width, height)
    """

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

        self.display_filler_color = BLACK
        self.screen_filler_color = BLACK

        self.dev = False

    def init_app(self):
        """Initialize all the variable necessary to run the application
        """
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
        """Handle pygame events

        Args:
            events (events): list of pygame events
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

            if self.dev:
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

    def update_app(self, dt):
        """Update the app

        Args:
            dt (float): delta time between two frame
        """
        pass

    def render_app(self):
        """Render the app
        """
        self.display.fill(self.display_filler_color)
        self.screen.fill(self.screen_filler_color)

    def cleanup(self):
        """Action to perform when the app quit
        """
        pygame.quit()

    def mainloop(self):
        """Mainloop of the app. Run forever until quit event.
        """
        if self.init_app() is False:
            self.running = False

        while(self.running):
            dt = self.clock.tick(self.FPS) / 1000
            events = pygame.event.get()

            if self.dev:
                show_fps(self.clock, self.caption)

            self.events_handling(events)

            if self.scene_manager is not None:
                self.display.fill(self.display_filler_color)
                self.screen.fill(self.screen_filler_color)
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
