# Some collision and gravity logic borrowed from:
# http://programarcadegames.com/python_examples/show_file.php?file=maze_runner.py
# PROGRAM NAME: platformer.py
# UP-TO-DATE AS OF: 10/14/2019
# VERSION NUMBER: 0.1
# PROGRAMMER: Colton Unruh

import pygame


from pymphony import GameState
from pymphony import FPSdisplay
from pymphony import MainMenu, PauseMenu
from pymphony.colors import *

import pymphony.game_functions as gf


def main():
    """ The main program for the game """

    # pygame needs this to be initialized
    pygame.init()

    # Create the screen and the surface drawn on it
    DISPLAYSURF = pygame.display.set_mode([800, 600])
    screen = pygame.Surface([800, 600])

    # set the game title
    pygame.display.set_caption("Platformer")

    # the object that controls the game's state and the current room
    gsobj = GameState(DISPLAYSURF, screen)

    # create the main and pause menus
    PauseMenu(gsobj, screen)
    MainMenu(gsobj, screen)

    # start the game in the menu
    gsobj.state = 0

    # class to display the framerate in the corner
    fps_debug = FPSdisplay(screen, gsobj)

    # class to manage the frame rate
    clock = pygame.time.Clock()

    # the main game loop
    while True:
        " Main game loop "
        # processes events
        gf.check_events(gsobj.central, fps_debug)

        # update the player or the menu or whatever
        gsobj.central.update()
        fps_debug.update(clock.get_fps())

        " v DRAW BELOW THIS COMMENT v "
        screen.fill(PURPLE)
        gsobj.draw_all()

        # double the screen and draw it on the DISPLAYSURF
        DISPLAYSURF.blit(screen, (0, 0))

        " ^ DRAW ABOVE THIS COMMENT ^ "

        # update the screen
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
