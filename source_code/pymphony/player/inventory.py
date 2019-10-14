import pygame


class Inventory:
    """ A class that contain pymphony the player is holding """

    def __init__(self):
        # initialize the font if it hasn't been already
        if not pygame.font.get_init():
            pygame.font.init()

        # the font for displaying the coins
        self.arial = pygame.font.SysFont("Arial", 36)

        # the player's coin counter
        self._coins = 0
        self._boins = 0
        self.max_num = 999
        self.blue_max = 9

        self.color = pygame.Color("orange")
        self.colorkey = (0, 255, 160)

        self.alt_color = pygame.Color("blue")

        self.image = pygame.Surface([210, 84])
        self.image.set_colorkey(self.colorkey)
        self.rect = self.image.get_rect()

        self.update()

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, value):
        """ only increase the coins if the value isn't larger than the maximum. """
        if value <= self.max_num and value != self._coins:
            self._coins = value
            self.update()

    @property
    def boins(self):
        return self._boins

    @boins.setter
    def boins(self, value):
        """ only increase the coins if the value isn't larger than the maximum. """
        if value <= self.blue_max and value != self._boins:
            self._boins = value
            self.update()

    def update(self):
        img1 = self.arial.render("Coins: {}".format(self._coins), False, self.color, self.colorkey)
        img2 = self.arial.render("Blue Coins: {}".format(self._boins), False, self.alt_color, self.colorkey)
        self.image.fill(self.colorkey)

        self.image.blit(img1, (0, 0))
        self.image.blit(img2, (0, self.arial.get_height()))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.coins = 0
        self.boins = 0
