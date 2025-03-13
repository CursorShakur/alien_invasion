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
        
        # Get damage from player's weapon
        self.damage = player.weapon.damage if hasattr(player, 'weapon') else 10
        
        # Customize color based on weapon level
        if hasattr(player, 'weapon'):
            level = player.weapon.level
            if level <= 1:
                self.color = settings.player_beam_color  # Green by default
            elif level == 2:
                self.color = (0, 200, 255)  # Blue
            elif level == 3:
                self.color = (255, 0, 255)  # Purple
            else:
                self.color = (255, 215, 0)  # Gold
        else:
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
        self.name = "Basic Laser"
        
    def upgrade(self):
        """Upgrade the weapon to the next level."""
        self.level += 1
        self.damage = 10 * self.level
        
        # Update weapon name based on level
        if self.level == 2:
            self.name = "Dual Laser"
        elif self.level == 3:
            self.name = "Plasma Cannon"
        elif self.level >= 4:
            self.name = "Quantum Beam"
            
        return self.level

    def get_description(self):
        """Get a description of the weapon."""
        return f"{self.name} (Level {self.level}) - Damage: {self.damage}"

    def attack(self):
        pass  # Logic for weapon attack 