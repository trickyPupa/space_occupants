import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, image_name, *groups):
        super().__init__(*groups)
        self.image = load_image(image_name, -1)
        self.rect = self.image.get_rect()

    def update(self, x):
        self.rect.move(x, self.rect.y)


class Enemies(pygame.sprite.Sprite):
    def __init__(self, image_name, *groups):
        super().__init__(*groups)
        self.image = load_image(image_name, -1)
        self.rect = self.image.get_rect()
        self.counter = 1
        self.k = 1

    def update(self):
        x, y = self.rect.x + self.k, self.rect.y
        if not self.counter % 5:
            y += 1
            self.k = -self.k
            self.counter = 1
        self.rect.move(x, y)
        self.counter += 1
