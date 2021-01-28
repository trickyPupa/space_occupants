import pygame
from ships import *


def main():
    size = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    player = SpaceShip()
    enem = Enemy(1)
    # enem.rect.move(200, 200)
    # border = Border(0, 200, 700, 200)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                player.update(event.pos[0])
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.fire()
        bullets.update()
        enemies.update()

        screen.fill((100, 100, 100))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()
