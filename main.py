import pygame
import random
from sprites.balloon import Balloon
from sprites.heart import Heart
from sprites.cloud import Cloud


if __name__ == '__main__':
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    cloud_sprites = pygame.sprite.Group()
    heart_sprites = pygame.sprite.Group()

    # отрисовка шарика
    balloon = Balloon(all_sprites)

    # отрисовка очков 
    points = 0
    font = pygame.font.Font(None, 26)  # выбор шрифт
    text = font.render(f'points:  {points}', True, (0, 0, 0))

    # отрисовка сердец жизней и счётчик жизней
    heart_count = 7
    for i in range(heart_count):
        Heart(heart_count, heart_sprites)

    # счётчик усложнения
    POINTEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(POINTEVENT, 10 ** 9)

    # время между появлением облаков
    CLOUDEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUDEVENT, 100)

    # фпс
    clock = pygame.time.Clock()
    FPS = 200

    pygame.mouse.set_visible(False)
    running = True
    while running:
        screen.fill('lightblue')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # отрисовка облаков
            if event.type == CLOUDEVENT:
                for i in range(random.randrange(2)):
                    Cloud(cloud_sprites)

            # начисление очков
            if event.type == POINTEVENT:
                points += 1

        # усложнение игры
        if points == 200:
            FPS += 1

        if heart_count == 0:
            with open('data/points_record.txt', 'w', encoding='utf8') as file:
                file.write(str(points))
            points = 0
            running = False

        # отрисовка очков
        text = font.render(f'points:  {points}', True, (0, 0, 0))

        # управление шариком
        balloon.update_pos()

        # обработка столкновения шарика с облаками
        if pygame.sprite.spritecollide(balloon, cloud_sprites, True):
            heart_count -= 1
            
            # отрисовка сердец жизни
            for sprite in heart_sprites:
                sprite.kill()
            
            for i in range(heart_count):
                Heart(heart_count, heart_sprites)

        cloud_sprites.update()
        cloud_sprites.draw(screen)

        all_sprites.update()
        all_sprites.draw(screen)

        heart_sprites.draw(screen)

        screen.blit(text, (600, 20))

        clock.tick(FPS)

        pygame.display.flip()
    pygame.quit()