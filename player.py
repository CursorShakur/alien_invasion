# Manages player attributes and actions
import pygame

class Player:
    def __init__(self, settings, screen):
        """Initialize the player and set its starting position."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Load the player ship image and get its rect
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Blue ship (placeholder)
        self.rect = self.image.get_rect()
        
        # Start each new player at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        
        # Store a decimal value for the player's center
        self.centerx = float(self.rect.centerx)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
        
        # Player attributes
        self.health = settings.player_health
        self.gems = settings.initial_gems
        
    def update(self):
        """Update the player's position based on movement flags."""
        # Update the player's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.player_speed
            
        # Update rect object from self.center
        self.rect.centerx = self.centerx
        
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def fire_beam(self):
        """Create a new beam and add it to the beams group."""
        from weapons import Beam
        return Beam(self.settings, self.screen, self)
        
    def reset_position(self):
        """Center the player on the screen."""
        self.centerx = self.screen_rect.centerx
        self.rect.centerx = self.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

    def take_action(self):
        pass  # Logic for player actions 