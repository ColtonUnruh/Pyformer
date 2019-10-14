""" these rooms are used in the game itself, generally to demonstrate some new mechanic """

# base for the room class
from .room_base import Room

# all objects that make up the levels
from ..level_objects.walls import Wall, MovingBlock
from ..level_objects.hills import HillBL, HillBR
from ..level_objects.doors import Door
from ..level_objects.consumable import Coin, BlueCoin

# the colors used
from pymphony.colors import *


class Room5(Room):
    """ For the platformer """
    room_id = 5

    width = 800
    height = 600

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 40, 600, GREEN],

                 # right wall
                 [760, 0, 40, 250, GREEN],
                 [760, 350, 40, 250, GREEN],

                 # ceiling
                 [40, 0, 310, 40, GREEN],
                 [450, 0, 310, 40, GREEN],

                 # floor
                 [40, 560, 720, 40, GREEN],

                 # others
                 [480, 440, 120, 40, GREEN],
                 [680, 350, 80, 40, GREEN],
                 [280, 320, 120, 40, GREEN],
                 [40, 200, 160, 40, GREEN],
                 [280, 120, 480, 40, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[780, 250, 7, 1, "k"],
                 [350, -40, 6, 1, "l", True]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

        self.get_coins()

    def get_coins(self):
        # this is a list of coins
        coins = [[560, 400], [480, 400], [320, 280], [80, 160], [160, 160]]

        boins = [[520, 400], [360, 280], [280, 280], [40, 160],  [120, 160]]

        for con in coins:
            coin = Coin(*con)
            coin.update(self.rect.x, self.rect.y)
            self.coin_list.add(coin)

        for bon in boins:
            boin = BlueCoin(*bon)

            boin.update(self.rect.x, self.rect.y)
            self.coin_list.add(boin)

        for x in range(280, 740, 40):
            coin = Coin(x, 80)
            coin.update(self.rect.x, self.rect.y)
            self.coin_list.add(coin)


class Room6(Room):
    """ For the platformer """
    room_id = 6

    width = 800
    height = 600

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 40, 600, GREEN],

                 # right wall
                 [760, 0, 40, 250, GREEN],
                 [760, 350, 40, 250, GREEN],

                 # ceiling
                 [40, 0, 310, 40, GREEN],
                 [450, 0, 310, 40, GREEN],

                 # floor
                 [40, 560, 310, 40, GREEN],
                 [450, 560, 310, 40, GREEN],

                 # others
                 [480, 440, 120, 40, GREEN],
                 [680, 350, 80, 40, GREEN],
                 [340, 160, 120, 40, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[780, 250, 7, 0, "m"],
                 [350, 580, 5, 1, "n", True],
                 [350, -40, 9, 1, "t", True]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

        self.get_coins()

        plat = MovingBlock(120, 280, 80, 40, D_GREEN)
        plat.boundary.top = 280
        plat.boundary.height = 200

        plat.change_y = -2
        plat.level_rect = self.rect
        self.wall_list.add(plat)
        self.plat_move.add(plat)

    def get_coins(self):
        # this is a list of coins
        coins = [[140, 240]]

        for con in coins:
            coin = Coin(*con)
            coin.update(self.rect.x, self.rect.y)
            self.coin_list.add(coin)


class Room7(Room):
    """ For the platformer """
    room_id = 7

    width = 800
    height = 1200

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [[0, 0, 40, 220, GREEN],
                 [0, 320, 40, 530, GREEN],
                 [0, 950, 40, 250, GREEN],
                 [760, 0, 40, 1200, GREEN],
                 [40, 0, 310, 40, GREEN],
                 [450, 0, 310, 40, GREEN],
                 [40, 1160, 720, 40, GREEN],
                 [40, 320, 80, 40, GREEN],
                 [40, 950, 80, 40, GREEN],
                 [200, 840, 120, 40, GREEN],
                 [200, 1040, 120, 40, GREEN],
                 [400, 720, 120, 40, GREEN],
                 [200, 600, 120, 40, GREEN],
                 [400, 480, 120, 40, GREEN],
                 [200, 360, 120, 40, GREEN],
                 [280, 120, 480, 40, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[-40, 220, 6, 0, "o"],
                 [-40, 850, 5, 0, "p"],
                 [350, -40, 9, 0, "s", True]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

        self.get_coins()

        plat = MovingBlock(600, 1040, 80, 40, D_GREEN)
        plat.boundary.top = 280
        plat.boundary.height = 800

        plat.change_y = 2
        plat.level_rect = self.rect
        self.wall_list.add(plat)
        self.plat_move.add(plat)

    def get_coins(self):
        s = True

        for x in range(40, 760, 40):
            if s:
                coin = Coin(x, 1120)
            else:
                coin = BlueCoin(x, 1120)

            coin.update(self.rect.x, self.rect.y)
            self.coin_list.add(coin)
            s = not s


class Room9(Room):
    """ For the platformer """
    room_id = 9

    width = 1600
    height = 600

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 40, 250, GREEN],
                 [0, 350, 40, 250, GREEN],

                 # right wall
                 [1560, 0, 40, 600, GREEN],

                 # ceiling
                 [40, 0, 1520, 40, GREEN],

                 # floor
                 [40, 560, 310, 40, GREEN],
                 [450, 560, 730, 40, GREEN],
                 [1280, 560, 280, 40, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[1180, 580, 7, 2, "q", True],
                 [350, 580, 6, 2, "r", True],
                 [-40, 250, 10, 0, "u"]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

        plat = MovingBlock(240, 300, 80, 40, D_GREEN)
        plat.boundary.left = 200
        plat.boundary.width = 1000

        plat.change_x = 2
        plat.level_rect = self.rect
        self.wall_list.add(plat)
        self.plat_move.add(plat)

        self.get_coins()

        hills = [HillBR(720, 480, 80, 80, GREEN),
                 HillBL(800, 480, 80, 80, GREEN)]

        for hill in hills:
            self.wall_list.add(hill)

    def get_coins(self):
        s = True

        for x in range(210, 1200, 40):
            if s:
                coin = BlueCoin(x, 260)
            else:
                coin = Coin(x, 260)
            coin.update(self.rect.x, self.rect.y)
            self.coin_list.add(coin)
            s = not s


class RoomA(Room):
    """ For the platformer """
    room_id = 10

    width = 800
    height = 600

    def __init__(self, screen):
        super().__init__(screen)

        # this is a list of walls
        walls = [
                 # left wall
                 [0, 0, 40, 170, GREEN],
                 [0, 190, 40, 410, GREEN],

                 # right wall
                 [760, 0, 40, 250, GREEN],
                 [760, 350, 40, 250, GREEN],

                 # ceiling
                 [40, 0, 720, 40, GREEN],

                 # floor
                 [40, 560, 720, 40, GREEN],

                 # others
                 [40, 440, 120, 120, GREEN],
                 [680, 350, 80, 40, GREEN],
                 [280, 320, 120, 40, GREEN],
                 [40, 200, 160, 40, GREEN]]

        for item in walls:
            wall = Wall(*item)
            self.wall_list.add(wall)

        doors = [[780, 250, 9, 2, "v"]]

        for thing in doors:
            door = Door(*thing)
            self.door_list.add(door)

        hills = [HillBL(160, 440, 120, 120, GREEN)]  # HillTR(340, 20, 40, 40, H_PINK)

        for hill in hills:
            self.wall_list.add(hill)
