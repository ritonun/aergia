import pygame


class GameObject:
    def __init__(self, pos, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

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


class AnimatedSpriteHandler:
    def __init__(self, animations, sprite_group):
        self.animations = animations
        self.sprite_group = sprite_group

    def set_animation(self, new_animation_key):
        for animation_key in self.animations:
            if self.sprite_group.has(self.animations[animation_key]):
                self.sprite_group.remove(self.animations[animation_key])
        self.sprite_group.add(self.animations[new_animation_key])

    def update(self):
        pass
