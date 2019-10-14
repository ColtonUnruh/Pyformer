import pygame


class Decor(pygame.sprite.Sprite):
    """ A simple decoration that can be used for anything."""

    def __init__(self, image):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()

    def update(self):
        pass
