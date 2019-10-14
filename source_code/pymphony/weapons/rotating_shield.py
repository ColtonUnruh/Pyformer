from pymphony.weapons.weapon import Weapon
import pymphony.game_functions as gf
from pymphony.colors import *


class RotatingShield(Weapon):
    def __init__(self, player, num=5):
        super().__init__(player)

        self.orbits = gf.get_orbitals(self.player, num)
        self.attacks = self.orbits.copy()

        self.firing = False

        self.icon.fill(NAVY, [8, 8, 14, 14])

    def attack(self):
        self.firing = not self.firing

    def update(self):
        # a bit clunky, but it works for now
        if not self.attacks:
            self.attacks = self.orbits.copy()

        if self.firing:
            self.attacks.update()

    def draw(self, surf):
        if self.firing:
            super().draw(surf)
