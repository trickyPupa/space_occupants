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
        self.image = pygame.transform.scale(load_image(image_name, -1), (100, 100))
        self.rect = self.image.get_rect().move(self.image.get_rect().x, 500)

    def update(self, x):
        self.rect = self.rect.move(x - self.rect.x - 0.5 * self.rect.width, 0)


class Enemies(pygame.sprite.Sprite):
    def __init__(self, image_name, *groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(load_image(image_name, -1), (100, 100))
        self.rect = self.image.get_rect()
        self.counter = 1
        self.k = 1

    def update(self):
        y = 0
        if not self.counter % 5:
            y = 1
            self.k = -self.k
            self.counter = 1
        self.rect.move(self.k, y)
        self.counter += 1
