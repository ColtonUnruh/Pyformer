import pygame


class FPSdisplay:
    """ display the framerate in the corner of the screen """

    def __init__(self, screen, gsobj):
        # initialize the font if it hasn't been already
        if not pygame.font.get_init():
            pygame.font.init()

        # should the frame rate be displayed?
        self.fps_on = True

        # should the player's position be displayed?
        self.player_pos = True

        # our reference to the screen.
        self.screen = screen
        self.screct = self.screen.get_rect()

        # our reference to the main gamestate object
        self.gsobj = gsobj
        self.gsobj.debug = self

        # the two font objects for the game
        self.arial = pygame.font.SysFont("Arial", 48)
        self.carial = pygame.font.SysFont("Arial", 24)

    def update(self, fps):
        """ change the image to the current fps and set it in the bottomright
        corner of the screen. """
        self.image = self.arial.render(str(round(fps)), False, pygame.Color("black"), (0, 255, 160))
        self.image.set_colorkey((0, 255, 160))
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.screct.bottomright

        self.posimg = self.carial.render("X: {} Y: {}".format(*self.gsobj.player.rect.topleft),
                                          False, (0, 0, 0), (0, 255, 160))

        self.posimg.set_colorkey((0, 255, 160))
        self.posrect = self.posimg.get_rect()

        self.posrect.topright = self.screct.topright

    def draw(self):
        # display the framerate if we need to
        if self.fps_on:
            self.screen.blit(self.image, self.rect)

        # display the player's position if we need to
        if self.player_pos:
            self.screen.blit(self.posimg, self.posrect)

    def check_strokes(self, keystroke):
        """ turn the tools on/off when the corresponding key is pressed """
        if keystroke == pygame.K_F1:
            self.fps_on = not self.fps_on
        if keystroke == pygame.K_F2:
            self.player_pos = not self.player_pos
