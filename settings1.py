
class Settings():
    """A class to store all settings for alien invasion"""

    def __init__(self):
        """ initialize game's settings"""

        # screen settings
        self.bg_color = (30, 30, 30)
        self.screen_width = 1200
        self.screen_height = 600

        # bullet settings
        self.bullet_speed = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)

        self.max_bullet = 5
        self.min_bullet = 1

        # player settings
        self.lives = 3
        self.score = 0

        # score
        self.points = 0

        # play game
        self.game_active = False

        # alien settings
        self.alien_speed = 10
