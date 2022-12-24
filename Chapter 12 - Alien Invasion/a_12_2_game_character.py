# Find a bitmap image of a game character you like or convert an image to
# a bitmap (Pygame naturally supports bitmap).

# Make a class that draws the character at the center of the screen and match
# the background color of the image to the background color of the screen, or
# vice versa.
import sys

import pygame

from settings import Settings
from character import Character

class GameCharacter:
    """Overall class to manage the game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Game Character")

        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Display characters and events
            self._check_events()
            self._update_screen()
    
    def _check_events(self):
        """Respond to the keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Close the game.
                sys.exit()
    
    def _update_screen(self):
        """Update images on the screen, and flip the new screen."""
        self.screen.fill(self.settings.q2_bg_color) # Background colour.
        self.character.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    gc = GameCharacter()
    gc.run_game()