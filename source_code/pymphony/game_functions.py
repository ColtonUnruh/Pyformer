import pygame
import sys
from math import tau
from itertools import cycle

from pymphony.weapons.orbital import Orbital

# return true if odd, false if even
isOdd = lambda x: x - ((x >> 1) << 1)


def inverse_color(color):
    """ inverse a rgb color"""
    return [abs(d - 255) for d in color]


def get_checkboard(square_w, square_h, width, height, colors):
    """ Create a checker board pattern with the given specs """
    back_img = pygame.Surface([width, height])
    color = cycle(colors)
    # improve this check algorithm to work with all values
    check = not isOdd(height // square_h)

    for x in range(0, width, square_w):
        for y in range(0, height, square_h):
            pygame.draw.rect(back_img, next(color), pygame.Rect(x, y, square_w, square_h))
        if check:
            next(color)

    return back_img


def check_events(central, debug):
    """ Check for keystrokes """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()

        central.check_event(event)

        if event.type == pygame.KEYDOWN:
            keydown_events(event)
        if event.type == pygame.KEYUP:
            keyup_events(event, debug)


def keydown_events(event):
    """ Check events for when a key is held down """
    pass


def keyup_events(event, debug,):
    """ Check events for when a key is released """
    debug.check_strokes(event.key)


def end_game():
    """ exit the game """
    pygame.quit()
    sys.exit()


def get_text(text, font, chroma=(0, 0, 0), background=(0, 255, 160), solid=True):
    """ render the text as an image """
    lines = text.split("\n")
    vec = font.render(max(lines, key=len), False, chroma)
    chars = pygame.Surface((vec.get_width(), vec.get_height() * len(lines)))
    chars.fill(background)

    for index, line in enumerate(lines):
        char = font.render(line, False, chroma, background)
        chars.blit(char, (0, vec.get_height() * index))

    if solid:
        chars.set_colorkey(background)
    return chars


def sprite_collide_rect(sprite, sprite_group):
    """ Get all sprites in group blocks and return a list of the ones who's
    rect overlaps the passed in sprite's """

    for ghost in sprite_group:
        if ghost.rect.colliderect(sprite.rect):

            yield ghost


def bullet_murder(bullets, walls):
    """ check the bullet class to see if any of them have hit any walls. If they have, kill them. """

    for bullet in bullets.copy():
        for wall in walls:
            if wall.rect.colliderect(bullet.rect):
                bullets.remove(bullet)


def check_offscreen(bullets, room):
    """ check if a bullet is off-screen, then kill it if it is."""

    for bullet in bullets.copy():
        if not room.rect.colliderect(bullet.rect):
            bullet.kill()


def get_orbitals(player, number, radius=60):
    """ return a number of orbitals that are an equal distance apart """
    orbitals = pygame.sprite.Group()

    try:
        angle = tau / number

    except ZeroDivisionError:
        return orbitals

    else:
        while len(orbitals) < number:
            orbit = Orbital(player, angle=angle, radius=radius)
            angle += tau / number

            orbitals.add(orbit)

        return orbitals


def shift_group(group, move_x, move_y):
    for sprite in group:
        sprite.rect.x += move_x
        sprite.rect.y += move_y


def set_around(player, room):
    """ Move the room so that the room and the player are in the right place. """

    plax = player.rect.x
    play = player.rect.y
    roox = room.rect.x
    rooy = room.rect.y

    # check horizontal position
    if player.rect.centerx < room.rect.left + room.screct.centerx:
        # the player needs to move
        room.rect.left = room.screct.left
        dis_x = room.rect.x - roox
        room.move_obj(dis_x, 0)

        # move the player
        player.rect.x += dis_x
    elif player.rect.centerx > room.rect.right - room.screct.centerx:
        # the player needs to move
        room.rect.right = room.screct.right
        dis_x = room.rect.x - roox
        room.move_obj(dis_x, 0)

        # move the player
        player.rect.x += dis_x
    else:
        # the room need to move
        player.rect.centerx = room.screct.centerx
        dis_x = player.rect.x - plax
        room.move_room(dis_x, 0)

        shift_group(player.weapon.attacks, dis_x, 0)

    # check vertical position
    if player.rect.centery < room.rect.top + room.screct.centery:
        room.rect.top = room.screct.top
        dis_y = room.rect.y - rooy
        room.move_obj(0, dis_y)

        # move the player
        player.rect.y += dis_y
    elif player.rect.centery > room.rect.bottom - room.screct.centery:
        room.rect.bottom = room.screct.bottom
        dis_y = room.rect.y - rooy
        room.move_obj(0, dis_y)

        # move the player
        player.rect.y += dis_y
    else:
        player.rect.centery = room.screct.centery
        dis_y = player.rect.y - play
        room.move_room(0, dis_y)

        shift_group(player.weapon.attacks, 0, dis_y)
