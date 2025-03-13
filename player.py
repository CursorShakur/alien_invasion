# Manages player attributes and actions
import pygame
from weapons import Weapon

class Player:
    def __init__(self, settings, screen, resource_manager=None):
        """Initialize the player and set its starting position."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.resource_manager = resource_manager
        
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
        
        # Weapon system
        self.weapon = Weapon(settings)
        
        # Upgrade levels
        self.speed_level = 1
        self.fire_rate_level = 1
        
        # Auto-shooting attributes
        self.last_shot_time = pygame.time.get_ticks()
        
    def update(self):
        """Update the player's position based on movement flags."""
        # Update the player's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.settings.player_speed * (1 + (self.speed_level - 1) * 0.2)
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.player_speed * (1 + (self.speed_level - 1) * 0.2)
            
        # Update rect object from self.center
        self.rect.centerx = self.centerx
        
    def blitme(self):
        """Draw the player at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def fire_beam(self):
        """Create a new beam and add it to the beams group."""
        from weapons import Beam
        return Beam(self.settings, self.screen, self)
        
    def should_auto_fire(self):
        """Check if enough time has passed to fire another shot."""
        current_time = pygame.time.get_ticks()
        # Reduced delay based on fire rate level
        adjusted_delay = self.settings.auto_fire_delay / (1 + (self.fire_rate_level - 1) * 0.2)
        if current_time - self.last_shot_time > adjusted_delay:
            self.last_shot_time = current_time
            return True
        return False
        
    def reset_position(self):
        """Center the player on the screen."""
        self.centerx = self.screen_rect.centerx
        self.rect.centerx = self.centerx
        self.rect.bottom = self.screen_rect.bottom - 10
        
    def upgrade_weapon(self):
        """Upgrade the player's weapon if enough resources are available."""
        if not self.resource_manager:
            return False
            
        upgrade_cost = self.resource_manager.get_upgrade_cost(self.weapon.level)
        if self.resource_manager.spend_resources(upgrade_cost):
            self.weapon.upgrade()
            return True
        return False
        
    def upgrade_speed(self):
        """Upgrade the player's movement speed if enough resources are available."""
        if not self.resource_manager:
            return False
            
        upgrade_cost = self.resource_manager.get_upgrade_cost(self.speed_level)
        if self.resource_manager.spend_resources(upgrade_cost):
            self.speed_level += 1
            return True
        return False
        
    def upgrade_fire_rate(self):
        """Upgrade the player's fire rate if enough resources are available."""
        if not self.resource_manager:
            return False
            
        upgrade_cost = self.resource_manager.get_upgrade_cost(self.fire_rate_level)
        if self.resource_manager.spend_resources(upgrade_cost):
            self.fire_rate_level += 1
            return True
        return False

    def take_action(self):
        pass  # Logic for player actions 