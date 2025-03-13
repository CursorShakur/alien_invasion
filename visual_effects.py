# Visual effects for the game
import random
import pygame

class StarfieldGenerator:
    """Generates and manages starfield backgrounds."""
    
    @staticmethod
    def create_stars(settings, screen, num_stars=50):
        """Create a starfield background."""
        stars = []
        for _ in range(num_stars):
            x = random.randint(0, settings.screen_width)
            y = random.randint(0, settings.screen_height)
            size = random.randint(1, 3)
            brightness = random.randint(150, 255)
            color = (brightness, brightness, brightness)
            stars.append((x, y, size, color))
        return stars
    
    @staticmethod
    def update_stars(stars, settings):
        """Update star positions for twinkling or movement effect."""
        updated_stars = []
        for x, y, size, color in stars:
            # Move stars slightly downward to create a falling effect
            y = (y + 1) % settings.screen_height
            
            # Randomly change brightness for twinkling effect
            if random.random() < 0.05:  # 5% chance to change brightness
                brightness = random.randint(150, 255)
                color = (brightness, brightness, brightness)
                
            updated_stars.append((x, y, size, color))
        
        return updated_stars 