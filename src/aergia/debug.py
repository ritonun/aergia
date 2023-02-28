import pygame


def show_fps(clock, caption=""):
    """
    Show fps directly in window name
    """
    fps = clock.get_fps()
    str_fps = "{} - {:.2f} FPS".format(caption, fps)
    pygame.display.set_caption(str_fps)
