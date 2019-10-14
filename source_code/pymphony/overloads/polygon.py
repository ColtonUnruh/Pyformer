import pygame


class Poly(pygame.Rect):
    """ a subclass of Rect that works with any polygon """

    def __init__(self, x, y, width, height, *vertices):
        super().__init__(x, y, width, height)
        self.vertices = vertices


class Quad(pygame.Rect):
    """ a subclass of Rect that works with any quadrilateral, faster than Poly """

    def __init__(self, x, y, width, height, *vertices):
        super().__init__(x, y, width, height)
        self.vertices = vertices