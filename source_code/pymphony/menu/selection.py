import pymphony.game_functions as gf


class Select:
    def __init__(self, menu, pos, text, font, color=(0, 0, 0), backcolor=(0, 255, 160), solid=True):
        self.menu = menu
        self.pos = pos

        self.text = gf.get_text(text, font, chroma=color, background=backcolor, solid=solid)

        self.rect = self.text.get_rect()

        self.rect.topleft = self.menu.start
        self.rect.y += self.rect.height * pos
