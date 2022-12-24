# This class will manage the game character.
import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, a_game):
        """Initialize the character and set its starting position."""
        # Get the screen rectangle (size) surface.
        self.screen = a_game.screen
        self.screen_rect = a_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('karadoc_character.bmp')
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center
    
    # Blit means block transfer. 
    # Gets the newly displayed surface on screen.
    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)