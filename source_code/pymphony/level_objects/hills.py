import pygame

from pymphony.colors import CHROMA
from pymphony.overloads.triangle import Tri


class Hill(pygame.sprite.Sprite):
    """ a right triangle block"""

    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill(CHROMA)
        self.image.set_colorkey(CHROMA)

    def update(self, move_x, move_y, player=None):
        """ moves the platform with the player """
        self.rect.x += move_x
        self.rect.y += move_y

    def set_player_x(self, player):
        pass

    def set_player_y(self, player):
        pass


class HillBL(Hill):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

        self.rect = Tri(0, 0, w, h, 'bl')
        self.c = 'bl'

        pygame.draw.polygon(self.image, color, self.rect.get_points())

        self.rect.x = x
        self.rect.y = y

    def set_player_x(self, player):
        # for bottom left
        #if player.change_x < 0:
        if player.direction.left:
            if player.rect.bottom > self.rect.bottom:
                player.rect.left = self.rect.right
            else:
                player.rect.bottom = self.rect.equation(player.rect.left)

                player.air_jump = True
                player.grounded = True
                player.change_y = 0

        #elif player.change_x > 0:
        elif player.direction.right:
            player.rect.right = self.rect.left

    def set_player_y(self, player):
        # for bottom left
        if player.change_y >= 0:
            b = self.rect.equation(player.rect.left)
            if b < self.rect.top:
                b = self.rect.top
            player.rect.bottom = b

            # the player has hit the ground, so enable their double jump
            player.air_jump = True
            player.grounded = True

            # stop falling
            player.change_y = 0

        elif player.change_y < 0:
            player.rect.top = self.rect.bottom
            player.grounded = False


class HillBR(Hill):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

        self.rect = Tri(0, 0, w, h, 'br')
        self.c = 'br'

        pygame.draw.polygon(self.image, color, self.rect.get_points())

        self.rect.x = x
        self.rect.y = y

    def set_player_x(self, player):
        # for bottom right
        #if player.change_x > 0:
        if player.direction.right:
            if player.rect.bottom > self.rect.bottom:
                player.rect.right = self.rect.left
            else:
                player.rect.bottom = self.rect.equation(player.rect.right)

                player.air_jump = True
                player.grounded = True

                player.change_y = 0

        #elif player.change_x < 0:
        elif player.direction.left:
            player.rect.left = self.rect.right

    def set_player_y(self, player):
        # for bottom right
        if player.change_y >= 0:
            b = self.rect.equation(player.rect.right)
            if b < self.rect.top:
                b = self.rect.top
            player.rect.bottom = b

            # the player has hit the ground, so enable their double jump
            player.air_jump = True
            player.grounded = True

            # stop falling
            player.change_y = 0

        elif player.change_y < 0:
            player.rect.top = self.rect.bottom
            player.grounded = False


class HillTL(Hill):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

        self.rect = Tri(0, 0, w, h, 'tl')
        self.c = 'tl'

        pygame.draw.polygon(self.image, color, self.rect.get_points())

        self.rect.x = x
        self.rect.y = y

    def set_player_x(self, player):
        # for top left
        if player.change_x < 0:
            if player.rect.top < self.rect.top:
                player.rect.left = self.rect.right
            else:
                player.rect.top = self.rect.equation(player.rect.left)

        elif player.change_x > 0:
            player.rect.right = self.rect.left

    def set_player_y(self, player):
        # for top left

        if player.change_y > 0:
            b = self.rect.equation(player.rect.left)
            if b > self.rect.bottom:
                b = self.rect.bottom
            player.rect.top = b
        elif player.change_y < 0:
            player.rect.bottom = self.rect.top


class HillTR(Hill):
    def __init__(self, x, y, w, h, color):
        super().__init__(x, y, w, h, color)

        self.rect = Tri(0, 0, w, h, 'tr')
        self.c = 'tr'

        pygame.draw.polygon(self.image, color, self.rect.get_points())

        self.rect.x = x
        self.rect.y = y

    def set_player_x(self, player):
        # for top right
        if player.change_x > 0:
            if player.rect.top < self.rect.top:
                player.rect.right = self.rect.left
            else:
                player.rect.top = self.rect.equation(player.rect.right)

        elif player.change_x < 0:
            player.rect.left = self.rect.right

    def set_player_y(self, player):
        # for top right

        if player.change_y <= 0:
            b = self.rect.equation(player.rect.right)
            if b > self.rect.bottom:
                b = self.rect.bottom
            player.rect.top = b
        elif player.change_y > 0:
            player.rect.bottom = self.rect.top