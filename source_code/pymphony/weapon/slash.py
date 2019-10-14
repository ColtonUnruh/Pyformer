import pygame
from .weapon import Weapon
from ..colors import H_PINK


class SwordSlash(pygame.sprite.Sprite):
    """ a good old fashion sword slash """

    def __init__(self, player, *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.Surface([30, 10])
        self.rect = self.image.fill(H_PINK)

        self.rect.center = self.player.rect.center

        self.time_on = 20  # how many frames should we be on screen?
        self.been_on = 0  # how many frames have we been on screen?

    def update(self):
        self.rect.center = self.player.rect.center

        if self.been_on < self.time_on:
            if self.player.direction.facing < 0:
                self.rect.right = self.player.rect.left
            elif self.player.direction.facing > 0:
                self.rect.left = self.player.rect.right

            self.been_on += 1
        else:
            self.kill()


class Thrust(pygame.sprite.Sprite):
    """ a good old fashion sword thrust """

    def __init__(self, player, *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.Surface([40, 20])
        self.rect = self.image.fill(H_PINK)

        self.rect.center = self.player.rect.center

        self.speed = 3  # how fast we thrust out
        self.hold = self.speed
        self.offset = 0

        self.linger = 20  # how long should we linger on screen
        self.time_out = 0  # how long have we been lingering

    def update(self):
        self.rect.center = self.player.rect.center
        self.rect.centerx += self.offset * self.player.direction.facing

        if self.player.direction.facing < 0:
            if self.rect.right <= self.player.rect.left:
                self.speed = 0

            elif self.rect.centerx > self.player.rect.centerx:
                self.kill()

        elif self.player.direction.facing > 0:
            if self.rect.left >= self.player.rect.right:
                self.speed = 0

            elif self.rect.centerx < self.player.rect.centerx:
                self.kill()

        if self.speed == 0:
            if self.time_out >= self.linger:
                self.speed = -self.hold
            self.time_out += 1
        self.offset += self.speed


class Sword(Weapon):
    """ a sword attack """

    def __init__(self, player):
        super().__init__(player)

        self.attacks = pygame.sprite.GroupSingle()

        self.firing = False

        self.icon.fill(H_PINK, [7, 10, 16, 10])

    def attack(self):
        self.firing = not self.firing
        if self.attacks.sprite is None:
            Thrust(self.player, self.attacks)
