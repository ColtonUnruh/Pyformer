import pygame


class KeysHeld:
    """ which keys are being held down? """
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False

        self.space = False
        self.zed = False

    def check_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.check_keydown(event)
        elif event.type == pygame.KEYUP:
            self.check_keyup(event)

    def check_keydown(self, event):
        if event.key == pygame.K_LEFT:
            self.left = True
        elif event.key == pygame.K_RIGHT:
            self.right = True
        elif event.key == pygame.K_UP:
            self.up = True
        elif event.key == pygame.K_DOWN:
            self.down = True

        elif event.key == pygame.K_SPACE:
            self.space = True
        elif event.key == pygame.K_z:
            self.zed = True

    def check_keyup(self, event):
        if event.key == pygame.K_LEFT:
            self.left = False
        elif event.key == pygame.K_RIGHT:
            self.right = False
        elif event.key == pygame.K_UP:
            self.up = False
        elif event.key == pygame.K_DOWN:
            self.down = False

        elif event.key == pygame.K_SPACE:
            self.space = False
        elif event.key == pygame.K_z:
            self.zed = False