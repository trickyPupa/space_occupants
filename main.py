from ships import *
from random import choice


def main():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    player = SpaceShip()
    border = Border(100, 250, 500)
    for i in range(4):
        for j in range(10):
            a = Enemy(choice([0, 1]))
            a.rect = a.rect.move(50 + 70 * j, 100 + 70 * i)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.fire()
        all_sprites.update()

        screen.fill((100, 100, 100))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(100)
    pygame.quit()


if __name__ == '__main__':
    main()
