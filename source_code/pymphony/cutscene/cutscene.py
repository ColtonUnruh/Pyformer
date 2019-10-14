import pygame
from pymphony.colors import BLACK


class Cutscene:
    """ the base class for future cutscenes. """
    def __init__(self):
        pass


class FadeIn:
    """ a fade to black and back """

    # speed we fade in/out
    speed = 20

    # how many frames we linger on
    linger = 0
    hold_cou = 0

    def __init__(self, screen, gsobj):
        self.screen = screen
        self.screct = self.screen.get_rect()

        self.gsobj = gsobj

        self.image = pygame.Surface(self.screct.size)
        self.image.fill(BLACK)

        self.image.set_alpha(0)

        # are we fading in or out?
        self.fade_in = True

        # is this transition done or not?
        self.done = False

    def update(self):
        """ update our image's alpha value """
        if self.fade_in:
            self.image.set_alpha(self.image.get_alpha() + self.speed)
        elif self.image.get_alpha() > 0:
            if self.hold_cou >= self.linger:
                self.image.set_alpha(self.image.get_alpha() - self.speed)
            else:
                self.hold_cou += 1
        else:
            self.finish()

        if self.image.get_alpha() >= 255:
            self.fade_in = False

    def finish(self):
        """ called when the transition is finished """
        self.done = True

    def draw(self):
        """ draw the image on the screen """
        self.screen.blit(self.image, (0, 0))

    def reset(self):
        """ reset the transition """
        self.done = False
        self.fade_in = True


class CutTo:
    """ cut to black for a few seconds """
    # how many frames we linger on
    linger = 5
    hold_cou = 0

    def __init__(self, screen, gsobj):
        self.screen = screen
        self.screct = self.screen.get_rect()

        self.gsobj = gsobj

        self.image = pygame.Surface(self.screct.size)
        self.image.fill(BLACK)

        # is this transition done or not?
        self.done = False

    def update(self):
        """ update our image's alpha value """
        if self.hold_cou < self.linger:
            self.hold_cou += 1
        else:
            self.finish()

    def finish(self):
        """ called when the transition is finished """
        # set the state back to the player
        self.gsobj.state = 1

        # reset the transition for the future
        self.reset()

        self.done = True

    def draw(self):
        """ draw the image on the screen """
        self.screen.blit(self.image, (0, 0))

    def check_event(self, event):
        """ forward all events to the player  """
        if event.type == pygame.KEYDOWN:
            self.gsobj.forward_keydown(event.key)
        elif event.type == pygame.KEYUP:
            self.gsobj.forward_keyup(event.key)

    def draw_main(self):
        """ needed to become a valid game state """
        pass

    def reset(self):
        """ reset the transition """
        self.done = False

        self.hold_cou = 0

