import pygame
import os
import sys
import random
import time


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# класс сердец жизней
class Heart(pygame.sprite.Sprite):
    image = load_image('heart.png')
    image2 = pygame.transform.scale(image, (60, 60))
    x,y = 20,20

    def __init__(self, *group):
        super().__init__(group)
        self.image = Heart.image
        self.rect = self.image.get_rect()
        self.rect.x = Heart.x
        self.rect.y = Heart.y

        Heart.x += 20


# отрисовка облаков
class Cloud(pygame.sprite.Sprite):
    image = load_image('cloud.png')

    def __init__(self, *group):
        super().__init__(group)
        self.group = group
        self.w, self.h = random.randint(80, 150), random.randint(70, 80)
        self.image = pygame.transform.scale(Cloud.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width - self.w)
        self.rect.y = -70

    def update(self):
        self.rect.y += 1

# класс шарика
class Balloon(pygame.sprite.Sprite):
    image = load_image('balloon.png')

    def __init__(self, *group):
        super().__init__(group)
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 260

    def update_pos(self, pos):
        self.rect = self.rect.move(pos[0], pos[1])


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
    FPS = 300
    
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
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_focused():
                screen.blit(balloon.image, event.pos)
                pygame.mouse.set_visible(False)
                balloon.update_pos(event.pos)

        all_sprites.update()
        all_sprites.draw(screen)
        screen.blit(text, (600, 20))

        clock.tick(FPS)

        pygame.display.flip()
    pygame.quit()