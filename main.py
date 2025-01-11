import pygame
import random
from data.class_balloon import Balloon
from data.class_heart import Heart
from data.class_cloud import Cloud


if __name__ == '__main__':
    pygame.init()
    size = width,height = 800,600
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()

    # отрисовка шарика
    balloon = Balloon(all_sprites)

    # отрисовка очков 
    points = 0
    font = pygame.font.Font(None, 26) # выбор шрифт 
    text = font.render(f'points:  {points}', True, (0, 0, 0))
    
    # отрисовка сердец жизни
    for i in range(7):
        Heart(all_sprites)
        
    # время между появлением облаков
    CLOUDEVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(CLOUDEVENT, 100)

    clock = pygame.time.Clock()
    FPS = 420
    
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
                    Cloud(all_sprites)

        # управление шариком
        balloon.update_pos()    

        all_sprites.update()
        all_sprites.draw(screen)
        screen.blit(text, (600, 20))

        clock.tick(FPS)

        pygame.display.flip()
    pygame.quit()