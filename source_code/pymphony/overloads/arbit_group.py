import pygame


class ArbitGroup(pygame.sprite.OrderedUpdates):
    """ a class of group that support arbitrary function calls on sprites
    Example: Let's say we have a sprite class with the function 'foo.'
    We can use ArbitGroup.foo(*args, **kwargs) to execute sprite.foo on all
    sprites in the group, even though ArbitGroup doesn't have a .foo method.
    Does NOT work if the method you wish to call already exists in the Group
    class. This still applies to the update method, but that doesn't matter.
    Methods in the Group class, for reference:
        -Group.sprites()
        -Group.copy()
        -Group.add()
        -Group.remove()
        -Group.has()
        -Group.update()  # Note: This doesn't matter
        -Group.draw()
        -Group.clear()
        -Group.empty()
    """

    def __getattr__(self, value):
        """ Get whatever value is on all sprites """
        return self._gen_executioner(value)

    def _gen_executioner(self, meth):
        """ Generate a function that calls whatever 'meth' is on all sprites in this group """

        def execute_method(*args, **kwargs):
            for sprite in self:
                # get the method from the sprites and call it
                getattr(sprite, meth)(*args, **kwargs)

        return execute_method


def demo():
    class Boi(pygame.sprite.Sprite):
        def __init__(self, *groups):
            super().__init__(*groups)

            self.rect = pygame.Rect(0, 0, 30, 30)

        def move(self, x, y=0):
            self.rect.x += x
            self.rect.y += y

    boi1 = Boi()
    thicc = ArbitGroup(boi1)
    boi2 = Boi(thicc)
    thicc.add(Boi())

    for boi in thicc:
        print(boi.rect)

    print("Calling .move on all sprites in thicc.")
    thicc.move(5, y=25)

    for boi in thicc:
        print(boi.rect)


demo()
