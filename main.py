import csv

import pygame
import random
from sprites.balloon import Balloon
from sprites.heart import Heart
from sprites.cloud import Cloud


if __name__ == '__main__':
    pygame.init()
    size = width,height = 900,700
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    cloud_sprites = pygame.sprite.Group()
    heart_sprites = pygame.sprite.Group()

    # отрисовка шарика
    balloon = Balloon(all_sprites)

    # счетчик очков 
    points = 0

    # лучший счёт
    with open('data/points_score.txt', 'r', encoding='utf8') as file:
        best_score = max([int(i.strip('\n')) for i in file.readlines()])
    
    # шрифты для текстов
    points_font = pygame.font.Font(None, 26)  # выбор шрифт
    menu_font = pygame.font.Font(None, 35)

    # отрисовка сердец жизней и счётчик жизней
    heart_count = 10
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

    # залипание клавиш
    pygame.key.set_repeat()

    # пауза
    pause = True

    running = True
    while running:
        screen.fill('lightblue')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if heart_count == 0:
                    running = False
                else:
                    pause = not pause
            
            if not pause and heart_count != 0:    
                # отрисовка облаков
                if event.type == CLOUDEVENT:
                    if FPS >= 220:
                        for i in range(random.randint(2, 4)):
                            Cloud(cloud_sprites)
                    else:
                        for i in range(random.randrange(2)):
                            Cloud(cloud_sprites)

                # начисление очков
                if event.type == POINTEVENT:
                    points += 1

        if pause:
            pygame.mouse.set_visible(True)

            pygame.draw.rect(screen, (250, 250, 250), (300, 200, 300, 300), border_radius=40)

            name_text = menu_font.render('Balloon flight', True, (0, 0, 0))
            play_text = menu_font.render('Press SPACE to play', True, (0, 0, 0))

            screen.blit(name_text, (370, 250))
            screen.blit(play_text, (330, 320))

        elif not pause or heart_count == 0:
            # конец игры
            if heart_count == 0:
                pygame.mouse.set_visible(True)

                pygame.draw.rect(screen, (250, 250, 250), (300, 200, 300, 300), border_radius=40)

                if points > best_score:
                    best_score = points

                end_text = menu_font.render('Game over', True, (0, 0, 0))
                points_end_text = menu_font.render(f'Your score:  {points}', True, (0, 0, 0))
                best_points_text = menu_font.render(f'Your best score:  {best_score}', True, (0, 0, 0))
                exit_text = menu_font.render('Press SPACE to exit', True, (0, 0, 0))

                screen.blit(end_text, (380, 230))
                screen.blit(points_end_text, (360, 300))
                screen.blit(best_points_text, (330, 370))
                screen.blit(exit_text, (330, 440))

            else:
                pygame.mouse.set_visible(False)

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
                
                # отрисовка очков
                points_text = points_font.render(f'points:  {points}', True, (0, 0, 0))
                screen.blit(points_text, (700, 20))
                
                # усложнение игры
                if points % 500 == 0:
                    FPS += 5

                cloud_sprites.update()
                cloud_sprites.draw(screen)

                all_sprites.update()
                all_sprites.draw(screen)

                heart_sprites.draw(screen)

        clock.tick(FPS)

        pygame.display.flip()
    pygame.quit()

    if best_score == points:
        with open('data/points_score.txt', 'w', encoding='utf8') as file:
            file.write(str(points))