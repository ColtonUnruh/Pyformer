import pygame
from itertools import cycle

import pymphony.game_functions as gf
from pymphony.colors import *
from pymphony.weapons.bullet import Gun
from pymphony.weapons.slash import Sword
from pymphony.weapons.rotating_shield import RotatingShield


class Player(pygame.sprite.Sprite):
    """ Class to hold everything related to the player """

    # the value that affects vertical movement
    change_y = 0

    # the speed at which the player moves
    # TODO for greater control of the speed, have player's x value
    # stored as a float, not an int, maybe make a sub class
    # of rect that stores the values as floats (subpixels).
    speed = 5

    # jumping vars
    # TODO don't tie these values to the FPS
    jump_height = -12
    gravity = 0.50
    term_vel = 20  # the 'terminal velocity,' or our max falling
    air_jump = True  # for the double jump
    max_jumps = 5  # the amount of double jumps allowed(not used)

    # the starting room and starting position
    spawn = (40, 520)
    start_room = 5

    # check if the player is on the ground or not
    grounded = True

    # frames since the ground was touched
    in_air_for = 0
    leni = 5  # leniency for jumping

    def __init__(self, screen, gsobj):
        """ Player's initialization """

        # call parent init first
        super().__init__()

        # create the player's image
        self.image = pygame.Surface([40, 40])
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        self.hitbox = pygame.Rect(0, 0, 23, 46)

        # set the screen of the game
        self.screen = screen
        self.screct = self.screen.get_rect()

        # The object that hold the games state and current room
        self.gsobj = gsobj

        # the object that controls movement
        self.direction = MovementDir(self)

        # the player's possible weapons and current weapon
        self.arsonal = cycle([Gun(self), Sword(self), RotatingShield(self)])
        self.weapon = next(self.arsonal)

    def draw(self):
        """ draw everything on the screen """
        self.weapon.draw(self.screen)

        self.screen.blit(self.image, self.rect)

        self.screen.fill(BLACK, [10, 550, 40, 40])
        self.screen.blit(self.weapon.icon, [15, 555])

    def check_event(self, event):
        """ move the player based of the given event """
        if event.type == pygame.KEYDOWN:
            self._check_keydown(event.key)
        elif event.type == pygame.KEYUP:
            self._check_keyup(event.key)

    def _check_keydown(self, keystroke):
        """ Change speed when a key is pressed """
        # see if we're moving left or right
        self.direction.check_keydown(keystroke)

        if keystroke == pygame.K_SPACE:
            self.jump()
        elif keystroke == pygame.K_ESCAPE:
            # switch to the pause menu
            self.gsobj.state = 2

    def _check_keyup(self, keystroke):
        """ Stop speed when a key is released """
        # see if we've stopped moving left or right
        self.direction.check_keyup(keystroke)

        if keystroke == pygame.K_SPACE:
            self.stop_jump()
        elif keystroke == pygame.K_x:
            self._swap_weapon()

    def jump(self):
        """ called when the player jumps """

        # move down for smoother jumping
        self.rect.y += 2
        platforms_hit = pygame.sprite.spritecollide(self, self.gsobj.get_walls(), False)
        self.rect.y -= 2

        # if we have collided with anything, it's ok to jump
        # because that means we are touching the ground
        if len(platforms_hit) > 0:
            self.change_y = self.jump_height
            self.in_air_for = self.leni + 1

        # if the player was only in air for a bit, let them jump
        elif self.in_air_for <= self.leni:
            self.change_y = self.jump_height
            self.in_air_for = self.leni + 1

        elif self.air_jump:
            self.change_y = self.jump_height

            # disable the double jump if it has already been used
            self.air_jump = False

            #self.air_jump -= 1

    def stop_jump(self):
        """ called when the player stops jumping """

        if self.change_y < 0:
            self.change_y *= self.gravity/2

    def duck(self):
        """ make the player duck down """
        pass

    def stand(self):
        """ make the player stand back up """
        pass

    def interact(self):
        """ when the player interacts with an object """
        pass

    def attack(self):
        """ attack with whatever weapon we are using """
        self.weapon.attack()

    def _swap_weapon(self):
        """ change the player's weapon """
        if not self.weapon.firing:
            self.weapon = next(self.arsonal)
            self.weapon.attacks.empty()

    def _calc_gravity(self):
        """ accelerate the player down with gravity """
        " partly borrow from source code "
        # move us down so we don't bounce on the moving platforms
        if self.change_y == 0:
            self.change_y = 2
        elif self.change_y < self.term_vel:
        #else:
            # as long as our speed is less than the maximum, increase the speed
            self.change_y += self.gravity

    def update(self):
        """ Update the player's position on the screen """

        # move the player down with gravity
        self._calc_gravity()

        # Move the rect horizontally and then vertically
        self.move_rect_x()
        self.move_rect_y()

        # check if the player is on the ground
        self.check_move_grounded()

        # If needed, scroll the screen
        gf.set_around(self, self.gsobj.room)

        # check if we got any coins in the room
        self.gsobj.check_coins()

        # check if we entered any doors
        self.gsobj.check_doors()

        # update our weapon
        self.weapon.update()

    def move_rect_x(self):
        """ Move the player horizontally and check for collisions """
        self.update_x()

        # check if movement caused collision with any walls
        hit_blocks = gf.sprite_collide_rect(self, self.gsobj.get_walls())
        for block in hit_blocks:
            block.set_player_x(self)

    def move_rect_y(self):
        """ Move the player vertically and check for collisions """
        self.rect.y += self.change_y

        # check if movement caused collision with any walls
        hit_blocks = gf.sprite_collide_rect(self, self.gsobj.get_walls())

        for block in hit_blocks:
            block.set_player_y(self)

        if not hit_blocks:
            self.grounded = False

    def update_x(self):
        """ update our x coordinate """
        if self.direction.left:
            self.rect.x -= self.speed
            self.direction.facing = -1
        if self.direction.right:
            self.rect.x += self.speed
            self.direction.facing = 1

    def check_move_grounded(self):

        for block in self.gsobj.get_move_walls():
            if self.rect.bottom == block.rect.top:
                if self.rect.left <= block.rect.right and self.rect.right >= block.rect.left:
                    self.grounded = True

        if self.grounded:
            self.in_air_for = 0
        else:
            self.in_air_for += 1

    def reset(self):
        self.rect.topleft = self.spawn
        self.gsobj.set_room(self.start_room)

    def update_img(self):
        """ update the player's image based off the change_x and change_y values """
        # change_x < 0: moving left
        # change_x > 0: moving right
        # change_y > 0: falling
        # change_y < 0: jumping
        pass

    def __str__(self):
        return "Player<{}, {}, {}, {}>".format(*self.rect.topleft, *self.rect.size)


class MovementDir:
    """ a class to hold what direction the player is moving """
    # TODO get rid of this and use 'state_handle.keys_held' instead

    def __init__(self, player):
        self.left = False  # is the player moving left?
        self.right = False  # is the player moving right?

        self.facing = 1  # what direction is the player facing

        self.player = player  # the player in question

    def check_keydown(self, keystroke):
        if keystroke == pygame.K_LEFT:
            self.left = True
        elif keystroke == pygame.K_RIGHT:
            self.right = True
        elif keystroke == pygame.K_z:
            self.player.attack()

    def check_keyup(self, keystroke):
        if keystroke == pygame.K_LEFT:
            self.left = False
        elif keystroke == pygame.K_RIGHT:
            self.right = False
        elif keystroke == pygame.K_z:
            self.player.attack()