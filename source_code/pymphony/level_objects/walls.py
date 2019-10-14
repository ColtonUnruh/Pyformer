import pygame


class Wall(pygame.sprite.Sprite):
    """ the walls and platforms the player can bump into """

    def __init__(self, x, y, width, height, color):
        """ Initialization """

        # init parent class
        super().__init__()

        # make image and rect for the wall
        self.image = pygame.Surface([width, height])
        self.rect = self.image.fill(color)

        # set the rect to the needed position
        self.rect.x = x
        self.rect.y = y

    def update(self, move_x, move_y, player=None):
        """ moves the platform with the player """
        self.rect.x += move_x
        self.rect.y += move_y

    def set_player_y(self, player):
        """ moves the player vertically if they have collided with this wall """
        " partly borrow from source code "
        if player.change_y > 0:
            # the player hit the ground
            player.rect.bottom = self.rect.top

            # the player has hit the ground, so enable their double jump
            player.air_jump = True
            player.grounded = True
            # alternative
            # self.air_jump = self.max_jumps

        elif player.change_y < 0:
            # the player hit a ceiling
            player.rect.top = self.rect.bottom
            player.grounded = False

        # stop falling
        player.change_y = 0

    def set_player_x(self, player):
        """ moves the player horizontally if they have collided with this wall """
        if player.direction.right:
            player.rect.right = self.rect.left

        elif player.direction.left:
            player.rect.left = self.rect.right


class MovingBlock(Wall):
    """ a platform that can move around """
    change_x = 0
    change_y = 0

    level_rect = None

    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)
        self.boundary = pygame.Rect(0, 0, 0, 0)

    def update(self, move_x, move_y, player=None):
        """ Scroll the screen or update the platform """
        if player:
            if self.rect.bottom >= self.boundary.bottom or self.rect.top <= self.boundary.top:
                self.change_y *= -1

            if self.rect.right >= self.boundary.right or self.rect.left <= self.boundary.left:
                self.change_x *= -1

            self.rect.x += self.change_x

            if pygame.sprite.collide_rect(self, player):
                # we hit the player
                if self.change_x < 0:
                    player.rect.right = self.rect.left
                else:
                    player.rect.left = self.rect.right

            # move up/ down
            self.rect.y += self.change_y

            if pygame.sprite.collide_rect(self, player):
                if self.change_y < 0:
                    player.rect.bottom = self.rect.top
                    #player.on_ground = True

                else:
                    player.rect.top = self.rect.bottom

        else:
            self.rect.x += move_x
            self.rect.y += move_y

            self.boundary.x += move_x
            self.boundary.y += move_y

    def set_player_y(self, player):
        super().set_player_y(player)
        if self.boundary.right >= self.rect.right and self.boundary.left <= self.rect.left:
            player.rect.x += self.change_x


class Phaseform(Wall):
    """ A platform that can be jumped thought from the bottom, but is solid on top """


class PushingBlock(Wall):
    """ a block that can be pushed by the player """


class Button(Wall):
    """ a block that is pressed by the player and activates something """
