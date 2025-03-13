# Base defense mechanics
import pygame

class Base:
    def __init__(self, settings, screen):
        """Initialize base attributes."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Base attributes
        self.health = 100
        self.max_health = 100
        self.defense_level = 1
        
        # Base appearance
        self.width = self.screen_rect.width
        self.height = 20
        self.color = (0, 255, 0)  # Green
        self.rect = pygame.Rect(0, self.screen_rect.height - self.height, 
                               self.width, self.height)
        
    def upgrade_defense(self, resource_manager):
        """Upgrade the base defense if resources are available."""
        upgrade_cost = resource_manager.get_upgrade_cost(self.defense_level)
        
        if resource_manager.spend_resources(upgrade_cost):
            self.defense_level += 1
            self.max_health += 20
            self.health = self.max_health
            return True
        return False
        
    def take_damage(self, damage):
        """Reduce base health by damage amount, considering defense level."""
        # Defense level reduces damage by 10% per level
        damage_reduction = 0.1 * (self.defense_level - 1)
        actual_damage = damage * (1 - damage_reduction)
        self.health -= actual_damage
        
        # Ensure health doesn't go below 0
        if self.health < 0:
            self.health = 0
            
        return self.health > 0  # Return True if base is still standing
        
    def draw(self):
        """Draw the base on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
    def draw_health_bar(self, x, y, width, height):
        """Draw a health bar for the base."""
        # Draw background (red)
        bg_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, (255, 0, 0), bg_rect)
        
        # Calculate health percentage
        health_percentage = self.health / self.max_health
        
        # Draw health bar (green)
        if health_percentage > 0:
            health_rect = pygame.Rect(x, y, int(width * health_percentage), height)
            pygame.draw.rect(self.screen, (0, 255, 0), health_rect)
            
        # Draw border
        pygame.draw.rect(self.screen, (255, 255, 255), bg_rect, 2) 