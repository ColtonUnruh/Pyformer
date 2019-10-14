import pygame
import math

from pymphony.colors import *


class Orbital(pygame.sprite.Sprite):
    """ an object that orbits around the player """

    def __init__(self, player, angle=0.0, radius=60):
        super().__init__()

        # our image
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.image.fill(NAVY)

        # the player we orbit around
        self.player = player

        # the angle us compared to the center of the player
        self._angle = angle

        # the distance from the player
        self.radius = radius

        # the speed we orbit around the player
        self.speed = 0.05

    @property
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        if value >= 6.28:
            self._angle = value % 6.28
        else:
            self._angle = value

    @property
    def degrees(self):
        """ the angle, but in degrees instead of radians """
        return math.degrees(self._angle)

    @degrees.setter
    def degrees(self, value):
        self.angle = math.radians(value)

    def update(self):
        # move our position to the player's position
        self.rect.center = self.player.rect.center

        # update our angle
        self.angle += self.speed

        # update our position
        self.rect.centerx += self.radius * math.cos(self.angle)
        self.rect.centery += self.radius * math.sin(self.angle)

    def __str__(self):
        return "Orbit<center:{}, angle:{}, around:{}>".format(self.rect.center, self.degrees, self.player.rect.center)
