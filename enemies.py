# Enemy wave logic
import pygame
import random
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        
        # Load the alien image and set its rect attribute
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red alien (placeholder)
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Health points
        self.health = settings.enemy_health
        
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
        
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False
        
    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.enemy_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    def take_damage(self, damage):
        """Reduce alien health by damage amount."""
        self.health -= damage
        return self.health <= 0  # Return True if alien is destroyed

class EnemyWave:
    def __init__(self, settings, screen):
        """Initialize the enemy wave."""
        self.settings = settings
        self.screen = screen
        self.aliens = pygame.sprite.Group()
        self.wave_number = 1
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        
    def create_fleet(self):
        """Create a full fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        alien = Alien(self.settings, self.screen)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows of aliens that fit on the screen
        alien_height = alien.rect.height
        available_space_y = (self.settings.screen_height - 
                            (3 * alien_height))
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
                
    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self.settings, self.screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        # Adjust alien health based on wave number
        alien.health = self.settings.enemy_health * (1 + (self.wave_number - 1) * 0.2)
        self.aliens.add(alien)
        
    def check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
                
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.enemy_drop_speed  # Use the new drop speed setting
        self.fleet_direction *= -1
        
    def update(self):
        """Update the positions of all aliens in the fleet."""
        self.check_fleet_edges()
        self.aliens.update()
        
    def spawn_enemies(self):
        """Spawn a new wave of enemies."""
        self.wave_number += 1
        # Increase enemy speed slightly with each wave, but cap it
        self.settings.enemy_speed = min(
            self.settings.enemy_speed * 1.1,  # Increase by 10% each wave
            2.0  # Maximum speed cap
        )
        self.create_fleet()
        return self.wave_number 