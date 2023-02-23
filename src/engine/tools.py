import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y, image_list, speed=3, loop=False):
        pygame.sprite.Sprite.__init__(self)

        self.images = image_list

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        self.counter = 0

        self.speed = speed
        self.loop = loop

    def update(self):
        # update anim
        self.counter += 1

        if self.counter >= self.speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if animation complete
        if self.index >= len(self.images) - 1 and self.counter >= self.speed:
            if not self.loop:
                self.kill()
            else:
                self.counter = 0
                self.index = 0
                self.image = self.images[self.index]


def wait_user_input():
    wait = True
    if pygame.mouse.get_pressed()[0]:
        wait = False
    return wait


def check_border(pos, rect, display_size):
    display_width, display_height = display_size

    if pos[0] < 0:
        pos[0] = 0
    elif pos[0] + rect.w > display_width:
        pos[0] = display_width - rect.w
    if pos[1] + rect.h > display_height:
        pos[1] = display_height - rect.h
    return pos


def rect_in_collision(rect, collisions_rects):
    lists = []
    for hitbox_rect in collisions_rects:
        if rect.colliderect(hitbox_rect):
            lists.append(hitbox_rect)
    return lists


def collision(rect, movement_vect, collisions_rects):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}

    rect.x += movement_vect[0]
    collide_list = rect_in_collision(rect, collisions_rects)
    for hitbox in collide_list:
        if movement_vect[0] > 0:
            rect.x = hitbox.x - rect.w
            collision_types["right"] = True
        elif movement_vect[0] < 0:
            rect.x = hitbox.x + hitbox.w
            # rect.left = hitbox.right
            collision_types["left"] = True

    rect.y += movement_vect[1]
    collide_list = rect_in_collision(rect, collisions_rects)
    for hitbox in collide_list:
        if movement_vect[1] > 0:
            rect.y = hitbox.y - rect.h
            collision_types["bottom"] = True
        elif movement_vect[1] < 1:
            rect.y = hitbox.y + hitbox.h
            collision_types["top"] = True
    return rect, collision_types


def get_offset(screen, player, offset):
    w, h = screen.get_size()
    x_offset, y_offset = 0, 0
    x = player.pos[0] + player.rect.w / 2
    y = player.pos[1] + player.rect.h / 2

    if x > w * (1 / 2) - offset[0] + player.rect.w / 2:
        x_offset = w * (1 / 2) - offset[0] + player.rect.w / 2 - x
    elif x < w * (1 / 2) - offset[0] - player.rect.w / 2:
        x_offset = w * (1 / 2) - offset[0] - player.rect.w / 2 - x

    if y > h * (1 / 2) - offset[1] + player.rect.h / 2:
        y_offset = h * (1 / 2) - offset[1] + player.rect.h / 2 - y
    elif y < h * (1 / 2) - offset[1] - player.rect.h / 2:
        y_offset = h * (1 / 2) - offset[1] - player.rect.h / 2 - y

    offset[0] += x_offset
    offset[1] += y_offset
    return offset
