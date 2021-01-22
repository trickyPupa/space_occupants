import pygame
from ships import *


def main():
    size = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    player = SpaceShip()
    border = Border(0, 200, 700, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.update(event.pos[0])
            if event.type == pygame.KEYDOWN:
                player.fire()
        bullets.update()
        # enemies.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()
