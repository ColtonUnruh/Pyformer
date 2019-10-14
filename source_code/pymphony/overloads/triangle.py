import pygame


class Tri(pygame.Rect):
    """ A child class of Rect for right triangle collision """
    def __init__(self, x, y, width, height, c):
        # 'c' is the point that is opposite the hypotenuse.
        # like this (x,y), (x+w,y), (x+w,y+h), (x, y+h)
        # Example:  #tl  , #tr  ,   #br   ,    #bl
        super().__init__(x, y, width, height)
        self._c = c
        self.slope = (self.height / self.width)

        if c == 'tr' or c == 'bl':
            self.y_int = self.y - (self.slope * self.x)
        else:
            self.slope *= -1
            self.y_int = self.y - (self.slope * self.right)

        # Create a function to check what side a Rect object is on
        self._get_sid_parm()

    def __setattr__(self, key, value):
        """ Overload, used reset the vars 'slope' and 'y_int' if needed """
        if '_attrExample__initialised' not in self.__dict__:
            # this test allows attributes to be set in the __init__ method
            pygame.Rect.__setattr__(self, key, value)
            if key not in self.__dict__:
                self.reset_equation()
        elif key in self.__dict__:
            # any normal attributes are handles normally
            pygame.Rect.__setattr__(self, key, value)
        else:
            self.__setitem__(key, value)

    def _get_sid_parm(self):
        """ Creates a function to test if a rectangle object
        is on the same side as  the 'c' point. """
        if self._c == 'tl':
            def same_side(rect):
                return rect.y <= self.equation(rect.x)
        elif self._c == 'tr':
            def same_side(rect):
                return rect.y <= self.equation(rect.right)
        elif self._c == 'bl':
            def same_side(rect):
                return rect.bottom >= self.equation(rect.x)
        else:
            def same_side(rect):
                return rect.bottom >= self.equation(rect.right)

        self.same_side = same_side

    def equation(self, x):
        """ Return the 'y' value for 'x' on the triangle's hypotenuse """
        return (x * self.slope) + self.y_int

    def inverse(self, y):
        """ Opposite of self.equation, return the 'x' value for 'y' on the triangle's hypotenuse """
        return (y - self.y_int) / self.slope

    def reset_equation(self):
        """ Reset the equation if the triangle has been changed """
        self.slope = self.height / self.width
        if self._c in ('tl', 'br'):
            self.slope *= -1
            self.y_int = self.y - (self.slope * self.right)
        else:
            self.y_int = self.y - (self.slope * self.x)

    def get_points(self):
        """ Returns a list of the three points the make up the triangle """
        if self._c == 'tl':
            return [self.topleft, self.topright, self.bottomleft]
        elif self._c == 'tr':
            return [self.topright, self.topleft, self.bottomright]
        elif self._c == 'bl':
            return [self.bottomleft, self.topleft, self.bottomright]
        else:
            return [self.bottomright, self.topright, self.bottomleft]

    def colliderect(self, rect):
        """ Overload, test if a rect is colliding with the triangle"""
        if ((self.x < rect.right) and
            (self.right > rect.x) and
            (self.y < rect.bottom) and
            (self.bottom > rect.y)):
            return self.same_side(rect)
        else:
            return False

    def contains(self, Rect):
        """ Check if a rectangle is fully engulfed in the triangle"""
        pass

    def collidepoint(self, x, y):
        """ Check if point (x, y) is in this triangle """
        pass

    def collidelist(self, p_list):
        pass

    def collidelistall(self, p_list):
        pass

    def collidedict(self, dict):
        pass

    def collidedictall(self, dict):
        pass
