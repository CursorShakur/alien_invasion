# Button component for UI interfaces
import pygame

class Button:
    def __init__(self, screen, msg, x, y, width=200, height=50):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    def is_clicked(self, mouse_pos):
        """Return True if the button is clicked."""
        return self.rect.collidepoint(mouse_pos) 