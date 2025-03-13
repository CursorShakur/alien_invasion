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
        button_width = 180
        button_height = 40
        button_margin = 10
        
        # Position buttons on the right side of the screen
        base_x = self.screen_rect.right - button_width - 20
        base_y = self.screen_rect.bottom - 5 * (button_height + button_margin)
        
        # Create different upgrade buttons
        self.upgrade_defense_button = Button(
            screen, "Upgrade Defense", 
            base_x + button_width // 2, 
            base_y,
            button_width, button_height
        )
        
        self.upgrade_weapon_button = Button(
            screen, "Upgrade Weapon", 
            base_x + button_width // 2, 
            base_y + (button_height + button_margin),
            button_width, button_height
        )
        
        self.upgrade_speed_button = Button(
            screen, "Upgrade Speed", 
            base_x + button_width // 2, 
            base_y + 2 * (button_height + button_margin),
            button_width, button_height
        )
        
        self.upgrade_fire_rate_button = Button(
            screen, "Upgrade Fire Rate", 
            base_x + button_width // 2, 
            base_y + 3 * (button_height + button_margin),
            button_width, button_height
        )
    
    def display(self, player, base, wave_number, resource_manager=None, game_state_manager=None):
        """Display the in-game UI."""
        # Draw wave number
        wave_text = self.normal_font.render(f"Wave: {wave_number}", True, self.text_color)
        self.screen.blit(wave_text, (20, 20))
        
        # Draw player health
        health_text = self.normal_font.render(f"Health: {player.health}", True, self.text_color)
        self.screen.blit(health_text, (20, 60))
        
        # Draw gems from resource manager
        if resource_manager:
            gems_text = self.normal_font.render(f"Gems: {resource_manager.gems}", True, self.text_color)
            self.screen.blit(gems_text, (20, 100))
        
        # Draw base defense level
        defense_text = self.normal_font.render(f"Defense Level: {base.defense_level}", True, self.text_color)
        self.screen.blit(defense_text, (20, 140))
        
        # Draw weapon info
        weapon_text = self.normal_font.render(f"Weapon: {player.weapon.name} (Lvl {player.weapon.level})", True, self.text_color)
        self.screen.blit(weapon_text, (20, 180))
        
        # Draw speed level
        speed_text = self.normal_font.render(f"Speed Level: {player.speed_level}", True, self.text_color)
        self.screen.blit(speed_text, (20, 220))
        
        # Draw fire rate level
        fire_rate_text = self.normal_font.render(f"Fire Rate Level: {player.fire_rate_level}", True, self.text_color)
        self.screen.blit(fire_rate_text, (20, 260))
        
        # Draw upgrade costs if resource manager is available
        if resource_manager:
            # X position for cost display
            cost_x = self.screen_rect.right - 220
            
            # Defense upgrade cost
            defense_cost = resource_manager.get_upgrade_cost(base.defense_level)
            defense_cost_text = self.normal_font.render(f"Cost: {defense_cost}", True, self.text_color)
            self.screen.blit(defense_cost_text, (cost_x, self.upgrade_defense_button.rect.centery - 15))
            
            # Weapon upgrade cost
            weapon_cost = resource_manager.get_upgrade_cost(player.weapon.level)
            weapon_cost_text = self.normal_font.render(f"Cost: {weapon_cost}", True, self.text_color)
            self.screen.blit(weapon_cost_text, (cost_x, self.upgrade_weapon_button.rect.centery - 15))
            
            # Speed upgrade cost
            speed_cost = resource_manager.get_upgrade_cost(player.speed_level)
            speed_cost_text = self.normal_font.render(f"Cost: {speed_cost}", True, self.text_color)
            self.screen.blit(speed_cost_text, (cost_x, self.upgrade_speed_button.rect.centery - 15))
            
            # Fire rate upgrade cost
            fire_rate_cost = resource_manager.get_upgrade_cost(player.fire_rate_level)
            fire_rate_cost_text = self.normal_font.render(f"Cost: {fire_rate_cost}", True, self.text_color)
            self.screen.blit(fire_rate_cost_text, (cost_x, self.upgrade_fire_rate_button.rect.centery - 15))
        
        # Draw upgrade buttons
        self.upgrade_defense_button.draw()
        self.upgrade_weapon_button.draw()
        self.upgrade_speed_button.draw()
        self.upgrade_fire_rate_button.draw()
        
        # Draw base health bar
        base.draw_health_bar(self.screen_rect.centerx - 150, 20, 300, 30)
        
        # Draw upgrade message if active
        if game_state_manager and game_state_manager.show_upgrade_message:
            self.draw_message(game_state_manager.upgrade_message)
    
    def check_buttons(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.upgrade_defense_button.is_clicked(mouse_pos):
            return "upgrade_defense"
        elif self.upgrade_weapon_button.is_clicked(mouse_pos):
            return "upgrade_weapon"
        elif self.upgrade_speed_button.is_clicked(mouse_pos):
            return "upgrade_speed"
        elif self.upgrade_fire_rate_button.is_clicked(mouse_pos):
            return "upgrade_fire_rate"
        return None
        
    def draw_message(self, message):
        """Draw a message overlay on the screen."""
        # Create a semi-transparent background
        overlay = pygame.Surface((self.screen_rect.width, 60))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        self.screen.blit(overlay, (0, self.screen_rect.centery - 30))
        
        # Render and center the message
        message_font = pygame.font.SysFont(None, 48)
        message_text = message_font.render(message, True, (255, 255, 0))
        message_rect = message_text.get_rect()
        message_rect.center = self.screen_rect.center
        self.screen.blit(message_text, message_rect)


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