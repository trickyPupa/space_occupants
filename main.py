import pygame
from ships import SpaceShip, Enemies


def main():
    size = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = SpaceShip('main_character.png', all_sprites, player_group)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.update(event.pos[0])
        enemies.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()
