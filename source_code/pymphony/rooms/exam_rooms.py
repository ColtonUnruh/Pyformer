""" older test rooms from when the game was a 'top-down'.
Not used, but kept as bases for future rooms """
from .room_base import Room
from ..level_objects.walls import Wall, MovingBlock
from ..level_objects.doors import Door
from ..level_objects.consumable import Coin
from pymphony.colors import *


class Room0(Room):
    """This creates all the walls in room 1"""
    room_id = 0

    width = 800
    height = 600

    def __init__(self, screen):

        super().__init__(screen)
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 275, BLUE],
                 [0, 325, 20, 275, BLUE],
                 [780, 0, 20, 275, BLUE],
                 [780, 325, 20, 275, BLUE],
                 [20, 0, 760, 20, BLUE],
                 [20, 580, 760, 20, BLUE]]

        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[-20, 275, 1, 1, "a"],
                 [790, 275, 3, 0, "b"]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)


class Room1(Room):
    """ This room is a test for a 2x1 level """
    room_id = 1

    width = 400
    height = 600

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [[0, 0, 20, 275, CYAN],
                 [0, 325, 20, 275, CYAN],
                 [380, 0, 20, 275, CYAN],
                 [380, 325, 20, 275, CYAN],
                 [20, 0, 360, 20, CYAN],
                 [20, 580, 360, 20, CYAN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[-20, 275, 2, 1, "c"],
                 [390, 275, 0, 0, "d"]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)


class Room2(Room):
    """ This room is a test for a 1x1 level """
    room_id = 2

    width = 400
    height = 300

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [[0, 0, 20, 125, PINK],
                 [0, 175, 20, 125, PINK],
                 [380, 0, 20, 125, PINK],
                 [380, 175, 20, 125, PINK],
                 [20, 0, 360, 20, PINK],
                 [20, 280, 155, 20, PINK],
                 [225, 280, 155, 20, PINK]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[-20, 125, 3, 1, "e"],
                 [390, 125, 1, 0, "f"],
                 [175, 290, 4, 0, "j", True]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)


class Room3(Room):
    """ This room is a test for a 1x2 level """
    room_id = 3

    width = 800
    height = 300

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 20, 125, NAVY],
                 [0, 175, 20, 125, NAVY],

                 # right wall
                 [780, 0, 20, 125, NAVY],
                 [780, 175, 20, 125, NAVY],

                 # ceiling and floor
                 [20, 0, 760, 20, NAVY],
                 [20, 280, 760, 20, NAVY]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)


class Room4(Room):
    """ This room is a test horizontal exits"""
    room_id = 4

    width = 400
    height = 300

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 20, 300, GREEN],

                 # right wall
                 [380, 0, 20, 300, GREEN],

                 # ceiling
                 [20, 0, 155, 20, GREEN],
                 [225, 0, 155, 20, GREEN],

                 # floor
                 [20, 280, 360, 20, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[175, -20, 2, 2, "i", True]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

class Room8(Room):
    """ A room to test coins and pickups """
    room_id = 8

    width = 400
    height = 300

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 20, 300, GREEN],

                 # right wall
                 [380, 0, 20, 300, GREEN],

                 # ceiling
                 [20, 0, 360, 20, GREEN],

                 # floor
                 [20, 280, 360, 20, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        self.get_coins()

        plat = MovingBlock(40, 40, 40, 20, D_GREEN)
        plat.boundary_bottom = 260
        plat.boundary_top = 40
        plat.boundary_left = 40
        plat.boundary_right = 360
        plat.change_y = -1
        plat.change_x = -1
        plat.level_rect = self.rect
        self.wall_list.add(plat)

    def get_coins(self):
        # fill the room with coins!
        for x in range(30, 380, 20):
            for y in range(30, 280, 20):
                coin = Coin(x-5, y-5)
                coin.update(self.rect.x, self.rect.y)
                self.coin_list.add(coin)
