# Introduces weapon mechanics
import pygame
from pygame.sprite import Sprite

class Beam(Sprite):
    """A class to manage beams fired from the player's ship."""
    
    def __init__(self, settings, screen, player):
        """Create a beam object at the player's current position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Create a beam rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, settings.player_beam_width, 15)
        self.rect.centerx = player.rect.centerx
        self.rect.top = player.rect.top
        
        # Store the beam's position as a decimal value
        self.y = float(self.rect.y)
        
        self.color = settings.player_beam_color
        self.speed_factor = settings.player_beam_speed
        
    def update(self):
        """Move the beam up the screen."""
        # Update the decimal position of the beam
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y
        
    def draw_beam(self):
        """Draw the beam to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class Weapon:
    def __init__(self, settings):
        """Initialize weapon attributes."""
        self.settings = settings
        self.level = 1
        self.damage = 10 * self.level
        
    def upgrade(self):
        """Upgrade the weapon to the next level."""
        self.level += 1
        self.damage = 10 * self.level
        return self.level

    def attack(self):
        pass  # Logic for weapon attack 