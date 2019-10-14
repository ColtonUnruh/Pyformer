class PlayGame:
    """ The game state of playing the game itself and controlling the character """
    def __init__(self, gs, screen, player):
        self.screen = screen
        self.screct = self.screen.get_rect()

        self.gs = gs
        self.gs.gameplay = self

        # the player character for the game
        self.player = player

        # whatever room the player is in
        self.room = None

    def update(self):
        # update the level's moving platforms
        self.gs.room.plat_move.update(0, 0, self.player)

        self.player.update()

    def check_event(self, event):
        self.player.check_event(event)

    def draw(self):
        self.player.draw()
