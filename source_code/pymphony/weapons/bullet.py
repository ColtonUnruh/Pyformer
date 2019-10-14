import pygame

from pymphony.colors import *
import pymphony.game_functions as gf
from .weapon import Weapon


class Bullet(pygame.sprite.Sprite):
    """ a bullet shot by the player """

    def __init__(self, player, *groups):
        super().__init__(*groups)

        # the image for the bullet
        self.image = pygame.Surface([15, 10])
        self.rect = self.image.get_rect()
        self.image.fill(CHROMA)

        pygame.draw.ellipse(self.image, D_CYAN, self.rect)

        self.image.set_colorkey(CHROMA)

        # set the bullet's position
        self.rect.center = player.rect.center

        # the speed the shots travel at
        self.shot_speed = 7
        self.shot_speed *= player.direction.facing

    def update(self):
        # update the bullet's position
        self.rect.x += self.shot_speed


class Gun(Weapon):
    def __init__(self, player):
        super().__init__(player)

        self.attacks = pygame.sprite.Group()

        self.bullet_delay = 10
        self.fs_fired = self.bullet_delay

        self.firing = False

        pygame.draw.ellipse(self.icon, D_CYAN, [8, 10, 14, 10])

    def _fire_bullet(self):
        """ fire a bullet """
        if self.fs_fired == self.bullet_delay:
            Bullet(self.player, self.attacks)
            self.fs_fired = 0
        else:
            self.fs_fired += 1

    def attack(self):
        self.firing = not self.firing

    def update(self):
        """ update our bullets """
        gf.bullet_murder(self.attacks, self.player.gsobj.get_walls())
        super().update()

        gf.check_offscreen(self.attacks, self.player.gsobj.room)

        if self.firing:
            self._fire_bullet()
