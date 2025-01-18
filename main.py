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
    cloud_sprite_group = pygame.sprite.Group()

    # отрисовка шарика
    balloon = Balloon(all_sprites)

    # отрисовка очков 
    points = 0
    font = pygame.font.Font(None, 26)  # выбор шрифт
    text = font.render(f'points:  {points}', True, (0, 0, 0))

    # счётчик усложнения
    fps_points = 0

    # счётчик жизней
    heart_count = 7
        
    # время между появлением облаков
    CLOUDEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUDEVENT, 100)

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
                    cloud = Cloud(cloud_sprite_group)

        if heart_count == 0:
            with open('data/points_record.txt', 'w', encoding='utf8') as file:
                file.write(points)
            points = 0
            running = False

        # отрисовка сердец жизни
        for i in range(heart_count):
            Heart(all_sprites)

        text = font.render(f'points:  {points}', True, (0, 0, 0))

        # управление шариком
        balloon.update_pos()

        # обработка столкновения шарика с облаками
        if cloud.collide_update(balloon.get_rect):
            heart_count -= 1

        cloud_sprite_group.update()
        cloud_sprite_group.draw(screen)

        all_sprites.update()
        all_sprites.draw(screen)
        screen.blit(text, (600, 20))

        clock.tick(FPS)
        # начисление очков
        points += 1
        fps_points += 1

        # усложнение игры
        if fps_points == 1000:
            fps_points = 0
            FPS += 10

        pygame.display.flip()
    pygame.quit()