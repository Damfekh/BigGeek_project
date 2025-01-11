import pygame
from data.image_func import load_image


# класс шарика
class Balloon(pygame.sprite.Sprite):
    image = load_image('img_balloon.png')

    def __init__(self, *group):
        super().__init__(group)
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 260

    def update_pos(self):
        if pygame.mouse.get_focused():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x, self.rect.y = mouse_x - 35, mouse_y - 40