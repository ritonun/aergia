import pygame


class GameObject:
    def __init__(self, pos, image=None, rect_size=None):
        if rect_size is None and image is None:
            raise TypeError("image & rect can not be None at the same time")

        if image is not None:
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.x = pos[0]
            self.rect.y = pos[1]
        else:
            w, h = rect_size
            self.rect = pygame.Rect(pos[0], pos[1], w, h)

        self.velocity = [0.0, 0.0]

    def collision_detection(self, list_object):
        for obj in list_object:
            if self.rect.colliderect(obj.rect):
                pass

    def handle_input(self, event):
        pass

    def update(self, dt):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def render(self, display):
        if self.image is not None:
            display.blit(self.image, (self.rect.x, self.rect.y))


class AnimatedSprite(pygame.sprite.Sprite):
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

    def reset(self):
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

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

    def resize(self, size):
        new_image_list = []
        for i in range(len(self.images)):
            img = self.images[i].copy()
            resize_img = pygame.transform.scale(img, (img.get_width() * size, img.get_height() * size))
            new_image_list.append(resize_img)
        self.images = new_image_list
        self.reset()


class AnimatedSpriteHandler:
    def __init__(self, animations, sprite_group):
        self.animations = animations
        self.sprite_group = sprite_group
        self.current_anim = ""

    def resize_anim(self, size, anim_key="all"):
        if anim_key == "all":
            for anim in self.animations:
                self.animations[anim].resize(size)

    def set_animation(self, new_animation_key):
        for anim in self.animations:
            if anim != new_animation_key:
                self.sprite_group.remove(self.animations[anim])
                self.sprite_group.add(self.animations[new_animation_key])
        self.current_anim = new_animation_key

    def update(self, new_pos):
        for anim in self.animations:
            self.animations[anim].rect.x = new_pos[0]
            self.animations[anim].rect.y = new_pos[1]
