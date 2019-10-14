import pygame

from pymphony.cutscene.cutscene import CutTo
from pymphony.player import Player
from pymphony.player.inventory import Inventory
from pymphony.rooms.demo_rooms import *
from .play_game import PlayGame
import pymphony.game_functions as gf


class GameState:
    """ This class holds the current game state. Game state controls if the
    game is in a cutscene, a menu, or gameplay. It also holds the room the
    player is in and manages room relate logic. """

    def __init__(self, displaysurf, screen):
        self.screen = screen
        self.screct = self.screen.get_rect()

        self.DISPLAYSURF = displaysurf

        # controls the game state
        self._state = None
        self.central = None

        self.rooms = [Room5(self.screen),
                      Room6(self.screen),
                      Room7(self.screen),
                      Room9(self.screen),
                      RoomA(self.screen)]

        # the object to hold the player character
        self.player = Player(self.screen, self)

        # these will be set when they initialize
        self.room = None
        self.debug = None
        self.main_menu = None
        self.pause_menu = None

        # this state for controlling the player and whatnot
        self.gameplay = PlayGame(self, self.screen, self.player)

        self.cuto_black = CutTo(self.screen, self)

        # the player's inventory
        self.inv = Inventory()

        self.player.reset()

        # the current version of the game
        self.version = "0.1"

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        if new_state == 0:
            # the main menu
            # because this is the title screen, reset pymphony
            self.reset_all()
            self.central = self.main_menu
            self._state = new_state
        elif new_state == 1:
            # the player
            self.central = self.gameplay
            self._state = new_state
        elif new_state == 2:
            # the pause menu
            self.central = self.pause_menu
            self._state = new_state

        elif new_state == 3:
            # a screen transition
            self.central = self.cuto_black
            self._state = new_state

    def get_walls(self):
        """ Return the walls of the current room """
        return self.room.wall_list

    def get_move_walls(self):
        """ Return the walls of the current room """
        return self.room.plat_move

    def get_doors(self):
        """ Return the doors of the current room """
        return self.room.door_list

    def get_a_door(self, index):
        """ Return the door in the current room's door_list at the index"""
        return self.room.door_list.sprites()[index]

    def draw_all(self):
        """ draw everything on the screen """
        # doesn't need to be draw if in a menu, so improve that
        self.room.draw()
        self.inv.draw(self.screen)
        self.debug.draw()

        self.central.draw()

    def set_room(self, room_id):
        """ Change the room based off the id """
        self.room = self.get_room_by_id(room_id)
        gf.set_around(self.player, self.room)

    def get_room_by_id(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                return room

    def check_doors(self):
        """ check if the player is in any door """
        for door in self.get_doors():
            if door.is_containing(self.player):
                self.enter_door(door)

    def enter_door(self, door):
        """ make the player 'enter' the door by changing the room and position """
        old_x = door.rect.centerx - self.player.rect.centerx
        old_y = door.rect.centery - self.player.rect.centery

        self.room = self.get_room_by_id(door.room_id)
        self.room.reset()

        # the rect of the output door
        ndoor = self.get_a_door(door.door_out)

        # move the player to the 'door' they just 'came out of'
        if ndoor.rect.width < ndoor.rect.height:
            # the door is vertical
            self.player.rect.centery = ndoor.rect.centery
            self.player.rect.centery -= old_y

            if ndoor.rect.left < 0:
                # the door is on the left side
                self.player.rect.left = ndoor.rect.right
            else:
                # the door is on the right side
                self.player.rect.right = ndoor.rect.left
        else:
            # the door is horizontal
            self.player.rect.centerx = ndoor.rect.centerx
            self.player.rect.centerx -= old_x

            if ndoor.rect.top < 0:
                # the door is on the top
                self.player.rect.top = ndoor.rect.bottom
            else:
                # the door is on the bottom
                self.player.rect.bottom = ndoor.rect.top

        gf.set_around(self.player, self.room)

        # set the state to a room transition
        self.state = 3

        # empty the player's attack group
        self.player.weapon.attacks.empty()

    def check_coins(self):
        """ see if the player got any coins in the room """
        coin_got = pygame.sprite.spritecollide(self.player, self.room.coin_list, True)
        for coin in coin_got:
            coin.add_myself(self.inv)

    def reset_all(self):
        for room in self.rooms:
            room.reset_coins()
            room.reset()

        self.player.reset()
        self.inv.reset()

        self.pause_menu.select = 0

    def forward_keydown(self, keystroke):
        """ forward any keydown events to the player """
        self.player.direction.check_keydown(keystroke)

    def forward_keyup(self, keystroke):
        """ forward any keyup events to the player """
        # maybe forward jump in menus as well?
        self.player.direction.check_keyup(keystroke)