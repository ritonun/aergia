import pygame


def show_fps(clock, caption=""):
    """
    Show fps directly in window name
    """
    fps = clock.get_fps()
    str_fps = "{} - {:.2f} FPS".format(caption, fps)
    pygame.display.set_caption(str_fps)


def show_fps_label(clock, display, pos, font_path, size=12):
    font = pygame.font.Font(font_path, size)
    text = str(round(clock.get_fps(), 2))
    text_surf = font.render(text, False, (255, 0, 0))
    display.blit(text_surf, pos)
