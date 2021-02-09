import pygame
import os
from random import choice

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bulletsa = pygame.sprite.Group()
bulletsb = pygame.sprite.Group()
borders = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def my_choices(seq, k):
    s = list(seq)
    res = []
    for i in range(k):
        a = choice(s)
        del s[s.index(a) - 55: s.index(a) + 55]
        res.append(a)
    return res


def delete(*groups):
    for group in groups:
        for i in group.sprites():
            i.kill()


class MySprite(pygame.sprite.Sprite):
    def __init__(self, size, *groups):
        super().__init__(all_sprites, *groups)
        self.size = size


class SpaceShip(MySprite):
    def __init__(self, size):
        super().__init__(size, player_group)
        self.image = pygame.transform.scale(load_image('main_character.png', -1), (84, 65))
        self.rect = self.image.get_rect().move(self.image.get_rect().x, self.size[1] - 150)
        self.lives = 3

    def update(self):
        x = pygame.mouse.get_pos()[0]
        x2 = x - self.rect.x - 0.5 * self.rect.width
        if 0 <= self.rect.x + x2 and self.rect.x + x2 + self.rect.width <= self.size[0]:
            self.rect = self.rect.move(x2, 0)
        if pygame.sprite.spritecollide(self, pygame.sprite.Group(*bulletsb.sprites(),
                                                                 *enemies.sprites()), True):
            self.lives -= 1

    def fire(self):
        Bullet(self.size, self.rect.x + self.rect.width // 2, self.rect.y, -3, bulletsa)


class Enemy(MySprite):
    def __init__(self, size, i, player):
        super().__init__(size, enemies)
        img = 'enemy1.jpg' if i else 'enemy2.jpg'
        self.image = pygame.transform.scale(load_image(img, -1), (50, 50))
        self.rect = self.image.get_rect()
        self.counter = 1
        self.k = 5
        self.player = player

    def moving(self):
        if not pygame.sprite.spritecollideany(self, borders):
            self.rect = self.rect.move(0, 1)

    def update(self):
        if self.rect.y == self.size[1]:
            self.player.lives -= 1
            self.kill()
        if pygame.sprite.spritecollide(self, bulletsa, True):
            self.kill()
        if choice(range(0, 10000)) < 5:
            Bullet(self.size, self.rect.x + self.rect.width // 2, self.rect.y, 3, bulletsb)
        self.moving()


class Bullet(MySprite):
    def __init__(self, size, x, y, v, b):
        super().__init__(size, b)
        self.image = load_image('bullet2.png', -1)
        self.v = v
        self.rect = self.image.get_rect().move(x - 3, y + self.v * 10)

    def update(self):
        if self.rect.y <= -46 or self.rect.y >= self.size[1]:
            self.kill()
        else:
            self.rect = self.rect.move(0, self.v)


class Border(MySprite):
    def __init__(self, size, x1, x2, y, v):
        super().__init__(size, borders)
        self.image = pygame.Surface([x2 - x1, 10])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x1, y, x2 - x1, 10)
        self.v = v

    def update(self):
        pygame.sprite.spritecollide(self, pygame.sprite.Group(*bulletsa.sprites(),
                                                              *bulletsb.sprites()), True)
        self.rect = self.rect.move(self.v, 0)
        if self.rect.x == 0 or self.rect.x + self.rect.width == self.size[0]:
            self.v = -self.v
