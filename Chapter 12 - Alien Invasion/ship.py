# Creating a Ship class.

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('sideway-ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the center-left side of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value of the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's y value, not the rect.
        # Limit the ship vertical range depending on screen size.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update rect object.
        self.rect.y = self.y
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)