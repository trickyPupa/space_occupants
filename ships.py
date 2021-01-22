import pygame
import os

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()


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
    def __init__(self):
        super().__init__(all_sprites, player_group)
        self.image = pygame.transform.scale(load_image('main_character.png', -1), (100, 100))
        self.rect = self.image.get_rect().move(self.image.get_rect().x, 500)

    def update(self, x):
        self.rect = self.rect.move(x - self.rect.x - 0.5 * self.rect.width, 0)

    def fire(self):
        b = Bullet(self.rect.x + self.rect.width // 2, self.rect.y)
        return b


class Enemies(pygame.sprite.Sprite):
    def __init__(self, image_name):
        super().__init__(all_sprites, enemies)
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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, bullets)
        self.image = load_image('bullet.jpg', -1)
        self.rect = self.image.get_rect().move(x - 3, y - 25)
        self.mask = pygame.mask.from_surface(self.image)
        self.k = 0

    def update(self):
        if self.k:
            self.kill()
        emen = pygame.sprite.spritecollideany(self, enemies)

        if self.rect.y <= -46:
            self.k = 1
        elif not emen:
            self.rect = self.rect.move(0, -5)
            return None
        else:
            self.k = 1
            return emen


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites, enemies)
        self.image = pygame.Surface([x2 - x1, 1])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x1, y1, x2 - x1, 1)