import pygame
import os
import sys


def load_image(name, colorkey=None):
    """Loads images

        Args:
            name (str): name of the file

        Returns:
            pygame.image: image
    """
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image