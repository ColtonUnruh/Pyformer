import pygame
from pymphony.colors import *


class Weapon:
    """ a generic weapon class that can be overloaded """

    def __init__(self, player):
        self.player = player

        # to be overloaded in the child classes, the sprite group that holds the weapons
        self.attacks = None

        # the icon for the weapon, overloaded in the subclass
        self.icon = pygame.Surface([30, 30])
        self.icon.fill(YELLOW)

    def check_event(self, event):
        pass

    def update(self):
        self.attacks.update()

    def draw(self, surf):
        """ blit the sprite group on the screen """
        self.attacks.draw(surf)

    def attack(self):
        """ called when the player attacks with the weapon """
        pass

    def reset(self):
        """ overloaded in the main function """
        pass


class MultiWeapon(Weapon):
    """ a generic weapon class that can hold a bunch of weapons """