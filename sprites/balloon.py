import pygame
from data.image_func import load_image


# класс шарика
class Balloon(pygame.sprite.Sprite):
    """
    The class includes information about the balloon object
    """
    img_index = 0
    ball_images = [
        load_image("img_balloon.png"),
        load_image("balloon2.png"),
        load_image("balloon3.png"),
        load_image("balloon4.png"),
        load_image("balloon5.png"),
        load_image("balloon6.png"),
        load_image("balloon7.png"),
        load_image("balloon8.png")]

    def __init__(self, *group):
        """Creating a balloon object and its hitbox

            Args:
                group (Sprite group): object's sprite group 
        """
        super().__init__(group)
        self.image = self.ball_images[self.img_index]
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

    def tick(self):
        if self.img_index == 0:
            self.img_index = 1

        elif self.img_index == 1:
            self.img_index = 2

        elif self.img_index == 2:
            self.img_index = 3

        elif self.img_index == 3:
            self.img_index = 4

        elif self.img_index == 4:
            self.img_index = 5

        elif self.img_index == 5:
            self.img_index = 6

        elif self.img_index == 6:
            self.img_index = 7

        elif self.img_index == 7:
            self.img_index = 0

        self.image = self.ball_images[self.img_index]
        self.image = pygame.transform.scale(self.image, (70, 80))

        self.rect = self.image.get_rect()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.rect.x, self.rect.y = mouse_x - 35, mouse_y - 40


