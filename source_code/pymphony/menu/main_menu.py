import pygame

import pymphony.game_functions as gf

from .selection import Select


class MainMenu:
    """ holds and works with the menu's data """

    def __init__(self, game_state, screen):
        myfont = pygame.font.SysFont("Arial", 60)

        # the screen and its rectangle
        self.screen = screen
        self.screct = self.screen.get_rect()

        # the image of the menu
        self.image = pygame.Surface(self.screct.size)
        self.image.fill(pygame.Color('blue'))

        self.rect = self.image.get_rect()
        self.rect.center = self.screct.center

        # an object that controls the state of the game
        self.gs = game_state
        self.gs.main_menu = self

        # what the player has selected in the menu
        self.select = 0
        self.get_imgs(myfont)
        self.start = (495, 360)

        # initialize all possible option for this menu
        self._init_options(myfont)

        # the decoration sprites for the menu
        self.decorations = pygame.sprite.Group()

        # get the decorations for the menu and add them to the group
        self._get_decor()

    def _get_decor(self):
        """ initialize the decorations on the menu"""
        pass

    def _init_options(self, font):
        """ Initialize the options for the menu """
        text = ["New Game", "Quit"]
        self.options = []

        for pos, txt in enumerate(text):
            self.options.append(Select(self, pos, txt, font, color=(255, 255, 255)))

        self.total = len(self.options) - 1  # set the opinions used

    def check_event(self, event):
        """ check a event from the keyboard """
        if event.type == pygame.KEYDOWN:
            self.move(event)
            # forward keydown events to the player
            self.gs.forward_keydown(event.key)
        elif event.type == pygame.KEYUP:
            # forward keyup events to the player
            self.gs.forward_keyup(event.key)

    def move(self, event):
        """ for keydown events, """
        if event.key == pygame.K_UP:
            if self.select > 0:
                self.select -= 1
        if event.key == pygame.K_DOWN:
            if self.select < self.total:
                self.select += 1

        if event.key == pygame.K_RETURN:
            self.choose()

        if event.key == pygame.K_ESCAPE:
            self.gs.state = 1

    def update(self):
        """ Redraw the menu """
        self.image.fill(pygame.Color("blue"))

        self.decorations.draw(self.image)

        self.curect.centery = self.options[self.select].rect.centery
        self.curect.right = self.options[self.select].rect.left

        self.image.blit(self.curse, self.curect)

        self.image.blit(self.title, self.tit_rect)

        for option in self.options:
            self.image.blit(option.text, option.rect)

        self.image.blit(self.verimg, self.verect)

    def get_imgs(self, font):
        # Make the cursor that moves around the menu
        self.curse = pygame.Surface([40, 40])
        self.curect = self.curse.get_rect()

        self.curse.fill((0, 255, 160))
        pygame.draw.polygon(self.curse, pygame.Color('orange'), [
            self.curect.topleft,
            [self.curect.left, self.curect.bottom-1],
            # self.curect.bottomleft,
            self.curect.midright
        ])

        self.curse.set_colorkey((0, 255, 160))

        # Get the title image
        title_fnt = pygame.font.SysFont("Arial", 120)
        self.title = gf.get_text("Platformer\nGame", title_fnt, chroma=(255, 255, 255))
        self.tit_rect = self.title.get_rect()
        self.tit_rect.topleft = (20, 0)

        # Get the version display and display it in the bottom left corner of the menu
        self.verimg = gf.get_text(self.gs.version, font, chroma=(255, 255, 255))
        self.verect = self.verimg.get_rect()
        self.verect.bottomleft = self.rect.bottomleft

    def update_curse(self, w):
        pass

    def choose(self):
        """ Called when the player presses enter,
        executes the selected command """
        if self.select == 0:
            # Continue
            self.gs.state = 1
        elif self.select == 1:
            # Quit
            gf.end_game()

    def draw(self):
        """ draw stuff on the main display """
        self.screen.blit(self.image, self.rect)
