import pygame

class Rocket:
    """A class to manage rockets."""

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings

        self.screen_rect = game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value of the rocket's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        # Update the rocket's x value, not the rect
        # Limit ship horizontal range
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update the rocket's y value, not the rect
        # Limit ship vertical range
        print(self.screen_rect)
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object from self.x or self.y
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)