import pygame


def show_fps(clock, caption=""):
    """
    Show fps directly in window name

    Args:
        clock (Clock): Clock
        caption (str, optional): Caption of the app, to add fps to the name
    """
    fps = clock.get_fps()
    str_fps = "{} - {:.2f} FPS".format(caption, fps)
    pygame.display.set_caption(str_fps)
