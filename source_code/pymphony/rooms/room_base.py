from pygame.sprite import Group, OrderedUpdates
from pygame import Rect

import pymphony.game_functions as gf
from pymphony.colors import *


class Room:
    """ base class for all rooms """

    # these variables are set in the subclass
    width = None
    height = None

    def __init__(self, screen):
        """ Initialization of our lists """
        self.wall_list = Group()
        self.coin_list = Group()
        self.plat_move = Group()
        self.door_list = OrderedUpdates()

        # the screen and its rect
        self.screen = screen
        self.screct = self.screen.get_rect()

        # the room's size and image
        self.rect = Rect(0, 0, self.width, self.height)
        self.bckimg = gf.get_checkboard(20, 20, self.width, self.height,
                                        [WHITE, GREY])
        #self.bckimg.fill(WHITE)

    def draw(self):
        """ Draw the room on the screen"""
        self.screen.blit(self.bckimg, self.rect)
        self.wall_list.draw(self.screen)
        self.door_list.draw(self.screen)
        self.coin_list.draw(self.screen)

    def move_room(self, move_x, move_y):
        """ Move all walls in the room """
        self.move_obj(move_x, move_y)
        self.rect.x += move_x
        self.rect.y += move_y

    def move_obj(self, move_x, move_y):
        """ Move all objects in the room, but not the room itself """
        self.wall_list.update(move_x, move_y)
        self.door_list.update(move_x, move_y)
        self.coin_list.update(move_x, move_y)

    def reset(self, player=None):
        """ reset the room rect's topleft to the topleft of the screen and
        move everything accordingly. """

        displace_x = self.screct.x - self.rect.x
        displace_y = self.screct.y - self.rect.y

        self.move_room(displace_x, displace_y)

        if player:
            player.rect.x += displace_x
            player.rect.y += displace_y

    def old_set_around(self, player):
        """ Move the room so that the room and the player are in the right place"""
        plax = player.rect.x
        play = player.rect.y
        roox = self.rect.x
        rooy = self.rect.y

        # check horizontal position
        if player.rect.centerx < self.rect.left + self.screct.centerx:
            self.rect.left = self.screct.left
            dis_x = self.rect.x - roox
            self.move_obj(dis_x, 0)
            player.rect.x += dis_x
        elif player.rect.centerx > self.rect.right - self.screct.centerx:
            self.rect.right = self.screct.right
            dis_x = self.rect.x - roox
            self.move_obj(dis_x, 0)
            player.rect.x += dis_x
        else:
            player.rect.centerx = self.screct.centerx
            dis_x = player.rect.x - plax
            self.move_room(dis_x, 0)

        # check vertical position
        if player.rect.centery < self.rect.top + self.screct.centery:
            self.rect.top = self.screct.top
            dis_y = self.rect.y - rooy
            self.move_obj(0, dis_y)
            player.rect.y += dis_y
        elif player.rect.centery > self.rect.bottom - self.screct.centery:
            self.rect.bottom = self.screct.bottom
            dis_y = self.rect.y - rooy
            self.move_obj(0, dis_y)
            player.rect.y += dis_y
        else:
            player.rect.centery = self.screct.centery
            dis_y = player.rect.y - play
            self.move_room(0, dis_y)

    def reset_coins(self):
        """ reset all coins """

        # improve this so it doesn't have to keep removing sprites already in the group
        self.coin_list.empty()

        self.get_coins()

    def get_coins(self):
        """ get the coins for the room, overloaded in subclasses """
        pass