import pygame
from data.image_func import load_image


# класс сердец жизней
class Heart(pygame.sprite.Sprite):
    """
    The class includes information about the heart object
    """
    image = load_image('img_heart.png')
    image2 = pygame.transform.scale(image, (60, 60))
    x,y = 20,20

    def __init__(self, *group):
        """Creating a heart object

        Args:
            group (Sprite group): object's sprite group 
        """
        super().__init__(group)
        self.image = Heart.image
        self.rect = self.image.get_rect()
        self.rect.x = Heart.x
        self.rect.y = Heart.y

        Heart.x += 20