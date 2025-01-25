import pygame
from data.image_func import load_image
import random


# класс облаков
class Cloud(pygame.sprite.Sprite):
    """
    The class includes information about the cloud object
    """
    image = load_image('img_cloud.png')

    def __init__(self, *group):
        """Creating a cloud object and its hitbox

        Args:
            group (Sprite group): object's sprite group 
        """
        super().__init__(group)
        self.group = group
        self.w, self.h = random.randint(80, 150), random.randint(70, 80)
        self.image = pygame.transform.scale(Cloud.image, (self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(900 - self.w)
        self.rect.y = -70

    def update(self, more=False):
        """Changes the position of the cloud

            Returns:
                None
        """

        if self.rect.y == 700:
            self.kill()

        self.rect.y += 1

        
        