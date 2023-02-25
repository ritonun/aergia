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
