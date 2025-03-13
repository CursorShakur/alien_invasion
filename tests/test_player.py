import unittest
import pygame
import sys
import os

# Add the parent directory to the path so we can import the game modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from player import Player
from settings import Settings

class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.Surface((self.settings.screen_width, self.settings.screen_height))
        self.player = Player(self.settings, self.screen)
        
    def tearDown(self):
        """Tear down test fixtures."""
        pygame.quit()
        
    def test_initialization(self):
        """Test that the player is initialized correctly."""
        self.assertEqual(self.player.health, self.settings.player_health)
        self.assertEqual(self.player.gems, self.settings.initial_gems)
        
    def test_movement(self):
        """Test player movement."""
        # Initial position
        initial_centerx = self.player.centerx
        
        # Move right
        self.player.moving_right = True
        self.player.moving_left = False
        self.player.update()
        self.assertGreater(self.player.centerx, initial_centerx)
        
        # Move left
        current_centerx = self.player.centerx
        self.player.moving_right = False
        self.player.moving_left = True
        self.player.update()
        self.assertLess(self.player.centerx, current_centerx)
        
    def test_reset_position(self):
        """Test resetting player position."""
        # Move the player
        self.player.moving_right = True
        self.player.update()
        
        # Reset position
        self.player.reset_position()
        
        # Check that the player is at the center bottom
        self.assertEqual(self.player.rect.centerx, self.screen.get_rect().centerx)
        self.assertEqual(self.player.rect.bottom, self.screen.get_rect().bottom - 10)
        
if __name__ == '__main__':
    unittest.main() 