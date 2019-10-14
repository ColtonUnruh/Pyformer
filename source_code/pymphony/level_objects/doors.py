import pygame


class Door(pygame.sprite.Sprite):
    """ A class that make the player teleport to a new room when they
    are engulfed in it """

    def __init__(self, x, y, room_id, door_out, door_name, h=False):
        super().__init__()
        if h:
            self.width = 100
            self.height = 60
        else:
            self.width = 60
            self.height = 100

        # create the rect and move it to it's spot in the room
        self.rect = pygame.Rect(x, y, self.width, self.height)

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(pygame.Color("yellow"))

        # set the room to be transported to
        self.room_id = room_id

        # the index of the door in the room that this door leads you to
        self.door_out = door_out

        self.door_name = door_name

    def is_containing(self, player):
        """ check to see if the player is engulfed in the rectangle """
        return self.rect.contains(player.rect)

    def update(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y

    def __repr__(self):
        return "Door {}: <{}, {}, {}, {}>".format(self.door_name, *self.rect)


class Entrance(pygame.sprite.Sprite):
    def __init__(self, x, y, room_id, door_out, door_id, *groups):
        super().__init__(*groups)

        self.image = pygame.Surface([800, 600])
        self.image.fill((255, 255, 0))

        # create the rect and move it to it's spot in the room
        self.rect = pygame.Rect(x, y, 800, 600)
        self.room_id = room_id
        self.door_out = door_out
        self.door_id = door_id

    def move(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y


class DoorLeft(Entrance):
    def __init__(self, x, y, room_id, door_out, door_id, *groups):
        super().__init__(x, y, room_id, door_out, door_id, *groups)

    def is_containing(self, player):
        if player.rect.right <= self.rect.right:
            if player.rect.top >= self.rect.top and player.rect.bottom <= self.rect.bottom:
                return True
        return False


class DoorRight(Entrance):
    def __init__(self, x, y, room_id, door_out, door_id, *groups):
        super().__init__(x, y, room_id, door_out, door_id, *groups)

    def is_containing(self, player):
        if player.rect.left >= self.rect.left:
            if player.rect.top >= self.rect.top and player.rect.bottom <= self.rect.bottom:
                return True
        return False


class DoorTop(Entrance):
    def __init__(self, x, y, room_id, door_out, door_id, *groups):
        super().__init__(x, y, room_id, door_out, door_id, *groups)

    def is_containing(self, player):
        if player.rect.bottom <= self.rect.bottom:
            if player.rect.left >= self.rect.left and player.rect.right <= self.rect.right:
                return True
        return False


class DoorBottom(Entrance):
    def __init__(self, x, y, room_id, door_out, door_id, *groups):
        super().__init__(x, y, room_id, door_out, door_id, *groups)

    def is_containing(self, player):
        if player.rect.top >= self.rect.top:
            if player.rect.left >= self.rect.left and player.rect.right <= self.rect.right:
                return True
        return False