import pygame


def main():
    size = 0, 0
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()