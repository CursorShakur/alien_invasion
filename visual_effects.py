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

class UpgradeEffect:
    """Class to create visual effects for upgrades."""
    
    def __init__(self, screen, x, y, color=(255, 215, 0)):
        """Initialize the upgrade effect."""
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.lifetime = 60  # Effect lasts for 60 frames (1 second at 60 FPS)
        self.create_particles()
        
    def create_particles(self, num_particles=30):
        """Create particles for the effect."""
        for _ in range(num_particles):
            # Random velocity
            vx = random.uniform(-3, 3)
            vy = random.uniform(-5, 0)
            
            # Random size
            size = random.randint(2, 5)
            
            # Random lifetime
            lifetime = random.randint(30, 60)
            
            # Add particle
            self.particles.append({
                'x': self.x,
                'y': self.y,
                'vx': vx,
                'vy': vy,
                'size': size,
                'lifetime': lifetime,
                'max_lifetime': lifetime
            })
    
    def update(self):
        """Update the particles."""
        self.lifetime -= 1
        
        for particle in self.particles[:]:
            # Update position
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            
            # Apply gravity
            particle['vy'] += 0.1
            
            # Decrease lifetime
            particle['lifetime'] -= 1
            
            # Remove dead particles
            if particle['lifetime'] <= 0:
                self.particles.remove(particle)
                
        return self.lifetime > 0 and self.particles
    
    def draw(self):
        """Draw the particles."""
        for particle in self.particles:
            # Calculate alpha based on remaining lifetime
            alpha = int(255 * (particle['lifetime'] / particle['max_lifetime']))
            
            # Create a surface for the particle
            particle_surface = pygame.Surface((particle['size'] * 2, particle['size'] * 2), pygame.SRCALPHA)
            
            # Draw the particle with alpha
            pygame.draw.circle(
                particle_surface, 
                (*self.color, alpha), 
                (particle['size'], particle['size']), 
                particle['size']
            )
            
            # Blit the particle surface to the screen
            self.screen.blit(
                particle_surface, 
                (particle['x'] - particle['size'], particle['y'] - particle['size'])
            ) 