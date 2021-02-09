from ships import *


def main():
    screen = pygame.display.set_mode((0, 0))
    SIZE = pygame.display.get_window_size()
    pygame.display.set_caption('Space occupants')
    clock = pygame.time.Clock()

    back = pygame.transform.scale(load_image('back1.jpg'), (SIZE[0], SIZE[1]))
    back.set_alpha(40)

    pygame.font.init()
    esc = pygame.font.Font(None, 20).render("Чтобы выйти нажмите ESC", True, (0, 255, 255))
    end2 = pygame.font.Font(None, 30).render("Чтобы начать новую игру нажмите ENTER", True, (0, 255, 255))
    end1 = pygame.font.Font(None, 30).render("Игра окончена", True, (0, 255, 255))

    player = SpaceShip(SIZE)
    Border(SIZE, 100, 250, SIZE[1] - 300, 1)
    Border(SIZE, SIZE[0] - 250, SIZE[0] - 100, SIZE[1] - 300, -1)

    running = True
    counter = 1
    k = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif player.lives <= 0 and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                player.lives = 3
                delete(enemies, bulletsa, bulletsb)
                counter = 1
                k = 1
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                player.fire()
        if not counter % int(200 * k):
            counter = 0
            k = max(k - 0.01, 0.3)
            n = choice((1, 2, 3))
            place = my_choices(range(30, SIZE[0] - 30), n)
            for i in range(n):
                if choice((0, 1, 2)):
                    a = Enemy(SIZE, choice([0, 1]), player)
                    a.rect = a.rect.move(place[i], 0)
                else:
                    Bullet(SIZE, place[i], 0, choice(range(2, 5)), bulletsb)
        screen.fill((10, 10, 10))
        screen.blit(back, (0, 0))
        if player.lives:
            all_sprites.update()
            all_sprites.draw(screen)
            screen.blit(esc, (SIZE[0] // 2 - esc.get_width() // 2, SIZE[1] - 20))
            for i in range(1, player.lives + 1):
                pygame.draw.circle(screen, (255, 0, 0), (SIZE[0] - 25 * i, SIZE[1] - 20), 10)
            clock.tick(100)
            counter += 1
        else:
            screen.blit(esc, (SIZE[0] // 2 - esc.get_width() // 2, SIZE[1] // 2 + 10))
            screen.blit(end1, (SIZE[0] // 2 - end1.get_width() // 2, SIZE[1] // 2 - 80))
            screen.blit(end2, (SIZE[0] // 2 - end2.get_width() // 2, SIZE[1] // 2 - 40))
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
