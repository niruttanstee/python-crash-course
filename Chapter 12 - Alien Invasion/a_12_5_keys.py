# KEYS
# Make a Pygame file that creates an empty screen. In the event loop, print
# the event.key attribute whenever a pygame.KEYDOWN event is detected.
# Run thew program and press various keys and see how Pygame responds.

import sys

import pygame

class Keys:
    """Overall class to manage game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Print Keys")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._print_keydown_events()
    
    def _print_keydown_events(self):
        """Print keydown events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                print(event.key)

if __name__ == '__main__':
    k = Keys()
    k.run_game()

