import pygame


class Coin(pygame.sprite.Sprite):
    """ A collectible coin """

    color = pygame.Color("orange")
    chroma = (0, 255, 160)

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([40, 40])
        self.image.fill(self.chroma)
        self.image.set_colorkey(self.chroma)

        self.rect = self.image.get_rect()

        pygame.draw.circle(self.image, self.color, self.rect.center, 10)

        self.rect.topleft = (x, y)

    def update(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y

    def add_myself(self, inv):
        """ add coin self to pass-in inventory object. """
        inv.coins += 1

    def __repr__(self):
        return "Coin at <{}, {}>".format(*self.rect.topleft)


class BlueCoin(Coin):
    """ Identical to the coin, but blue and increments a different counter """
    color = pygame.Color("Blue")

    def add_myself(self, inv):
        """ increase the inventory object's blue coin counter """
        inv.boins += 1

    def __repr__(self):
        return "Blue" + super().__repr__()
