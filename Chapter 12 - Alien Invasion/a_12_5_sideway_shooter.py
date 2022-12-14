# Write a game that places a ship on the left side of the screen and allows
# the player to move the ship up and down. Make the ship fire a bullet that
# travels right scross the screen when the player presses the spacebar.
# Make sure bullets are deleted once they disappear off the screen.

import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class SidewayShooter():
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Sideway Shooter")

        self.ship = Ship(self)
        # Create group for bullets.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop of the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _check_events(self):
        """Respond to the keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Responding to a [up or down] keypress.
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
         
        # Check for [Q] key press to quit.
        elif event.key == pygame.K_q:
            sys.exit()

        # Respond to bullet fire.
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet nad add it to the bullets group."""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
                print(f"Active bullet: {len(self.bullets)}")

    
    def _update_screen(self):
        """Update images on the screen, and flip the new screen."""
        self.screen.fill(self.settings.q2_bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()


        pygame.display.flip()

if __name__ == '__main__':
    sh = SidewayShooter()
    sh.run_game()

            



