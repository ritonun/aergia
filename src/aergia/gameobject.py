import pygame


class GameObject:
    """Basic class that represent all entity

    Attributes:
        image (Surface): Defaut is None, can be an image
        rect (Rect): Rect of image/entity size
        velocity (list): Reprensent the movement of the object
    """

    def __init__(self, pos, image=None, rect_size=None):
        """Initialize the GameObject class

        Args:
            pos (tuple): Coordinate of entity
            image (Surface, optional): Represent the entity
            rect_size (Rect, optional): If no image is passed, enter the rect size by hand (width, height)

        Raises:
            TypeError: Image & rect_size can not be both None
        """
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
        """Detect collision with other object

        Args:
            list_object (list): list of other object
        """
        for obj in list_object:
            if self.rect.colliderect(obj.rect):
                pass

    def handle_input(self, event):
        """Handle player input

        Args:
            event (events): List of pygame event
        """
        pass

    def update(self, dt):
        """Update object

        Args:
            dt (float): delta time between two frames
        """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def render(self, display):
        """Render object

        Args:
            display (surface): Surface to render the object on
        """
        if self.image is not None:
            display.blit(self.image, (self.rect.x, self.rect.y))


class AnimatedSprite(pygame.sprite.Sprite):
    """Summary

    Attributes:
        image (Surface): Current image in the animation
        images (list): List of image part of the animation
        index (int): Current index of the list of images
        loop (bool): If true, the animation loop over until it is over. Else it only play once.
        rect (Rect): Rect of the size of the image
        speed (int): Speed of the animation
    """

    def __init__(self, x: int, y: int, image_list, speed=3, loop=False):
        """Initialize the AnimatedSprite class

        Args:
            x (int): x coordinate
            y (int): y coordinate
            image_list (TYPE): list of image part of the animation
            speed (int, optional): Speed of the animation
            loop (bool, optional): If true, the animation loop over until it is over. Else it only play once.
        """
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
        """Reset all var of the animation
        """
        self.index = 0
        self.image = self.images[self.index]
        self.counter = 0
        old_center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def update(self):
        """Update the animation
        """
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
        """Resize all the images part of the animations

        Args:
            size (float): resize ratio
        """
        new_image_list = []
        for i in range(len(self.images)):
            img = self.images[i].copy()
            resize_img = pygame.transform.scale(img, (img.get_width() * size, img.get_height() * size))
            new_image_list.append(resize_img)
        self.images = new_image_list
        self.reset()


class AnimatedSpriteHandler:
    """Class to handle a bunch of animation associated to an entity.

    Attributes:
        animations (dict): Dictionnary containing all the animations
        current_anim (str): Current animation key
        sprite_group (sprite.Group): pygame.sprite.Group() that handle the draw & update of the animations
    """

    def __init__(self, animations, sprite_group):
        """Initialize AnimatedSpriteHandler

        Args:
            animations (dict): Dictionnary containing all the animations
            sprite_group (sprite.Group): pygame.sprite.Group() that handle the draw & update of the animations
        """
        self.animations = animations
        self.sprite_group = sprite_group
        self.current_anim = ""

    def resize_anim(self, size, anim_key="all"):
        """Resize all animation handled by this class

        Args:
            size (float): resize ratio
            anim_key (str, optional): anim key to resize. default="all", resize all anim
        """
        if anim_key == "all":
            for anim in self.animations:
                self.animations[anim].resize(size)
        else:
            self.animations[anim_key].resize(size)

    def set_animation(self, new_animation_key):
        """Set the current animation

        Args:
            new_animation_key (str): animation key to set
        """
        for anim in self.animations:
            if anim != new_animation_key:
                self.sprite_group.remove(self.animations[anim])
                self.sprite_group.add(self.animations[new_animation_key])
        self.current_anim = new_animation_key

    def update(self, new_pos):
        """Update all anim with new coordinate on screen

        Args:
            new_pos (tuple): New coordinate
        """
        for anim in self.animations:
            self.animations[anim].rect.x = new_pos[0]
            self.animations[anim].rect.y = new_pos[1]
