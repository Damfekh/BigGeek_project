import pygame
from data.image_func import load_image
import random


# класс облаков
class Cloud(pygame.sprite.Sprite):
    image = load_image('img_cloud.png')

    def __init__(self, *group):
        super().__init__(group)
        self.group = group
        self.w, self.h = random.randint(80, 150), random.randint(70, 80)
        self.image = pygame.transform.scale(Cloud.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.w)
        self.rect.y = -70

    def update(self):
        self.rect.y += 1