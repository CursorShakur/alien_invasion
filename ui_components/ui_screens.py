# UI screens for different game states
import pygame
from ui_components.button import Button

class MainMenuScreen:
    """Handles the main menu screen display and interactions."""
    
    def __init__(self, settings, screen):
        """Initialize the main menu screen."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set up fonts
        self.title_font = pygame.font.SysFont(None, 64)
        self.text_color = (255, 255, 255)
        
        # Create buttons
        self.start_button = Button(screen, "Start Game", 
                                   self.screen_rect.centerx, 
                                   self.screen_rect.centery)
        self.exit_button = Button(screen, "Exit", 
                                  self.screen_rect.centerx, 
                                  self.screen_rect.centery + 100)
    
    def display(self):
        """Display the main menu."""
        # Draw title
        title = self.title_font.render("Alien Invasion", True, self.text_color)
        title_rect = title.get_rect()
        title_rect.centerx = self.screen_rect.centerx
        title_rect.top = self.screen_rect.top + 100
        self.screen.blit(title, title_rect)
        
        # Draw buttons
        self.start_button.draw()
        self.exit_button.draw()
    
    def check_buttons(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.start_button.is_clicked(mouse_pos):
            return "start_game"
        elif self.exit_button.is_clicked(mouse_pos):
            return "exit_game"
        return None


class GameplayScreen:
    """Handles the in-game UI display and interactions."""
    
    def __init__(self, settings, screen):
        """Initialize the gameplay screen."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set up fonts
        self.normal_font = pygame.font.SysFont(None, 36)
        self.text_color = (255, 255, 255)
        
        # Create buttons
        self.upgrade_button = Button(screen, "Upgrade Defense", 
                                    self.screen_rect.right - 150, 
                                    self.screen_rect.bottom - 100)
    
    def display(self, player, base, wave_number):
        """Display the in-game UI."""
        # Draw wave number
        wave_text = self.normal_font.render(f"Wave: {wave_number}", True, self.text_color)
        self.screen.blit(wave_text, (20, 20))
        
        # Draw player health
        health_text = self.normal_font.render(f"Health: {player.health}", True, self.text_color)
        self.screen.blit(health_text, (20, 60))
        
        # Draw gems
        gems_text = self.normal_font.render(f"Gems: {player.gems}", True, self.text_color)
        self.screen.blit(gems_text, (20, 100))
        
        # Draw base defense level
        defense_text = self.normal_font.render(f"Defense Level: {base.defense_level}", True, self.text_color)
        self.screen.blit(defense_text, (20, 140))
        
        # Draw upgrade button
        self.upgrade_button.draw()
        
        # Draw base health bar
        base.draw_health_bar(self.screen_rect.centerx - 150, 20, 300, 30)
    
    def check_buttons(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.upgrade_button.is_clicked(mouse_pos):
            return "upgrade_defense"
        return None


class GameOverScreen:
    """Handles the game over screen display and interactions."""
    
    def __init__(self, settings, screen):
        """Initialize the game over screen."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set up fonts
        self.title_font = pygame.font.SysFont(None, 64)
        self.text_color = (255, 255, 255)
        
        # Create buttons
        self.restart_button = Button(screen, "Restart", 
                                    self.screen_rect.centerx, 
                                    self.screen_rect.centery + 100)
    
    def display(self, victory):
        """Display the game over screen."""
        # Draw game over message
        if victory:
            message = "Victory!"
        else:
            message = "Game Over"
            
        game_over_text = self.title_font.render(message, True, self.text_color)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.centerx = self.screen_rect.centerx
        game_over_rect.centery = self.screen_rect.centery - 50
        self.screen.blit(game_over_text, game_over_rect)
        
        # Draw restart button
        self.restart_button.draw()
    
    def check_buttons(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.restart_button.is_clicked(mouse_pos):
            return "restart_game"
        return None 