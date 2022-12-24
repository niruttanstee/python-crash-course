# Settings class.
# Setting object for the challenges in chapter 12 in creating Pygame windows.

class Settings:
    """A class to store all settings for Alien Invasions"""

    def __init__(self):
        """Initialize the Pygame window settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (6, 193, 227) # Blue.
        self.q2_bg_color = (0, 0, 0)

        # Rocket settings.
        self.rocket_speed = 4.0