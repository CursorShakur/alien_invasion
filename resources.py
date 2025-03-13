# Handles resource management
class ResourceManager:
    def __init__(self, settings):
        """Initialize resources."""
        self.settings = settings
        self.gems = settings.initial_gems
        self.upgrade_cost = settings.upgrade_cost
        
    def earn_resources(self, points):
        """Add resources based on points earned."""
        self.gems += points
        return self.gems
        
    def spend_resources(self, amount):
        """Spend resources if available."""
        if self.gems >= amount:
            self.gems -= amount
            return True
        return False
        
    def can_afford(self, amount):
        """Check if player can afford an upgrade."""
        return self.gems >= amount
        
    def get_upgrade_cost(self, current_level):
        """Calculate the cost of the next upgrade."""
        return self.upgrade_cost * current_level
        
    def display_resources(self, screen, font, x, y):
        """Display the current resource count on the screen."""
        resource_text = font.render(f"Gems: {self.gems}", True, (255, 255, 255))
        screen.blit(resource_text, (x, y)) 