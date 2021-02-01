from ships import *


def main():
    screen = pygame.display.set_mode((0, 0))
    SIZE = pygame.display.get_window_size()
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    player = SpaceShip(SIZE)
    border = [Border(SIZE, 100, 250, SIZE[1] - 300, 1),
              Border(SIZE, SIZE[0] - 250, SIZE[0] - 100, SIZE[1] - 300, -1)]
    a = Enemy(SIZE, choice((0, 1)))
    a.rect = a.rect.move(choice(range(50, SIZE[0] - 50)), 0)

    running = True
    tick = True
    counter = 1
    k = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pass
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.fire()
        if not counter % int(200 * k):
            counter = 0
            k = max(k - 0.01, 0.3)
            n = choice((1, 2, 3))
            place = my_choices(range(30, SIZE[0] - 30), n)
            for i in range(n):
                if choice((0, 1, 2)):
                    a = Enemy(SIZE, choice([0, 1]))
                    a.rect = a.rect.move(place[i], 0)
                else:
                    Bullet(SIZE, place[i], 0, choice(range(2, 5)), bulletsb)
        all_sprites.update()
        screen.fill((100, 100, 100))
        all_sprites.draw(screen)
        pygame.display.flip()
        if tick:
            clock.tick(100)
        counter += 1
    pygame.quit()


if __name__ == '__main__':
    main()
