

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
