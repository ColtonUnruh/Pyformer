from pymphony.level_objects import Wall
from pymphony.colors import *
from .room_base import *


class Room99(Room):
    """ the base for an empty 1x1 room with no doors or walls, used to test new mechanics """
    room_id = 99

    width = 400
    height = 300

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 20, 300, GRAY],

                 # right wall
                 [380, 0, 20, 300, GRAY],

                 # ceiling
                 [20, 0, 360, 20, GRAY],

                 # floor
                 [20, 280, 360, 20, GRAY]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)
