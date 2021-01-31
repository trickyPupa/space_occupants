import pygame
import os

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

SIZE = (800, 700)


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


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites, player_group)
        self.image = pygame.transform.scale(load_image('main_character.png', -1), (84, 65))
        self.rect = self.image.get_rect().move(self.image.get_rect().x, 600)

    def update(self):
        x = pygame.mouse.get_pos()[0]
        x2 = x - self.rect.x - 0.5 * self.rect.width
        if 0 <= self.rect.x + x2 and self.rect.x + x2 + self.rect.width <= SIZE[0]:
            self.rect = self.rect.move(x2, 0)

    def fire(self):
        b = Bullet(self.rect.x + self.rect.width // 2, self.rect.y)
        return b


class Enemy(pygame.sprite.Sprite):
    def __init__(self, im):
        super().__init__(all_sprites, enemies)
        self.image = pygame.transform.scale(load_image('enemy1.jpg', -1), (50, 50)) if im == 1 \
            else pygame.transform.scale(load_image('enemy2.jpg', -1), (50, 50))
        self.rect = self.image.get_rect()
        self.counter = 1
        self.k = 5

    def moving(self):
        if not self.counter % 900:
            self.counter = 1
            self.rect = self.rect.move(0, 5)
            self.k = -self.k
        elif not self.counter % 500:
            self.k = -self.k
            self.rect = self.rect.move(self.k, 0)
        elif not self.counter % 100:
            self.rect = self.rect.move(self.k, 0)
        self.counter += 1

    def update(self):
        if pygame.sprite.spritecollide(self, bullets, True):
            self.kill()
        self.moving()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites, bullets)
        self.image = load_image('bullet.jpg', -1)
        self.rect = self.image.get_rect().move(x - 3, y - 25)

    def update(self):
        if self.rect.y <= -46:
            self.kill()
        else:
            self.rect = self.rect.move(0, -3)


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, x2, y):
        super().__init__(all_sprites, enemies)
        self.image = pygame.Surface([x2 - x1, 10])
        self.image.fill((255, 255, 255))
        self.rect = pygame.Rect(x1, y, x2 - x1, 10)
        self.v = 1

    def update(self):
        pygame.sprite.spritecollide(self, bullets, True)
        self.rect = self.rect.move(self.v, 0)
        if self.rect.x == 0 or self.rect.x + self.rect.width == SIZE[0]:
            self.v = -self.v
