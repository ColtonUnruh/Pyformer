import pygame

import pymphony.game_functions as gf
from .selection import Select


class PauseMenu:
    """ holds and works with the menu's data """

    def __init__(self, game_state, screen):
        myfont = pygame.font.SysFont("Arial", 60)
        self.text_height = myfont.get_height()

        self.screen = screen
        self.screct = self.screen.get_rect()

        self.size = [self.screct.width - 40, self.screct.height - 40]
        self.image = pygame.Surface(self.size)
        self.image.fill(pygame.Color('green'))

        self.rect = self.image.get_rect()
        self.rect.center = self.screct.center

        self.gs = game_state
        self.gs.pause_menu = self

        self.select = 0
        self.get_imgs()
        self.start = (495, 160)

        self._init_options(myfont)

    def _get_decor(self):
        pass

    def _init_options(self, font):
        text = ["Continue", "Exit to title"]
        self.options = []

        for pos, txt in enumerate(text):
            option = Select(self, pos, txt, font, backcolor=(0, 255, 0), solid=False)
            option.rect.centerx = self.rect.centerx
            option.rect.y += 5*pos
            self.options.append(option)

        self.total = len(self.options) - 1

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.move(event)
            # forward keydown events to the player
            self.gs.forward_keydown(event.key)
        elif event.type == pygame.KEYUP:
            # forward keyup events to the player
            self.gs.forward_keyup(event.key)

    def move(self, event):
        """ for keyup events, stops the player """
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
        self.image.fill(pygame.Color('green'))

        self.update_curse(self.options[self.select].rect.width + 5)
        self.curect.center = self.options[self.select].rect.center

        self.image.blit(self.curse, self.curect)

        self.image.blit(self.title, self.tit_rect)

        for option in self.options:
            self.image.blit(option.text, option.rect)

    def get_imgs(self):
        # Make the cursor that moves around the menu
        self.update_curse(10)

        # Get the title image
        title_fnt = pygame.font.SysFont("Arial", 100)
        self.title = gf.get_text("Options", title_fnt)
        self.tit_rect = self.title.get_rect()
        self.tit_rect.top = 20
        self.tit_rect.centerx = self.rect.centerx

    def update_curse(self, w):
        self.curse = pygame.Surface([w, self.text_height+5])
        self.curect = self.curse.get_rect()

        self.curse.fill(pygame.Color('orange'))

    def choose(self):
        """ Called when the player presses enter,
        executes the selected command """
        if self.select == 0:
            # Continue
            self.gs.state = 1
        elif self.select == 1:
            # exit to title
            self.gs.state = 0

    def draw(self):
        """ draw stuff on the main display """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.image, self.rect)