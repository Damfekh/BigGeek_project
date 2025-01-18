import pygame
from data.image_func import load_image


# класс шарика
class Balloon(pygame.sprite.Sprite):
    """
    The class includes information about the balloon object
    """
    image = load_image('img_balloon.png')

    def __init__(self, *group):
        """Creating a balloon object and its hitbox

            Args:
                group (Sprite group): object's sprite group 
        """
        super().__init__(group)
        self.image = pygame.transform.scale(self.image, (70, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 360
        self.rect.y = 260

    def update_pos(self):
        """Changes the position of the balloon

            Returns:
                None
        """
        if pygame.mouse.get_focused():
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.x, self.rect.y = mouse_x - 35, mouse_y - 40