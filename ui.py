# Handles user input and output
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

class UI:
    def __init__(self, settings, screen):
        """Initialize UI components."""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set up fonts
        self.title_font = pygame.font.SysFont(None, 64)
        self.normal_font = pygame.font.SysFont(None, 36)
        
        # Set up colors
        self.text_color = (255, 255, 255)
        
        # Game state
        self.game_active = False
        self.show_menu = True
        self.show_game_over_screen = False
        self.victory = False
        
        # Create buttons
        self.start_button = Button(screen, "Start Game", 
                                  self.screen_rect.centerx, 
                                  self.screen_rect.centery)
        self.upgrade_button = Button(screen, "Upgrade Defense", 
                                    self.screen_rect.right - 150, 
                                    self.screen_rect.bottom - 100)
        self.exit_button = Button(screen, "Exit", 
                                 self.screen_rect.centerx, 
                                 self.screen_rect.centery + 100)
        self.restart_button = Button(screen, "Restart", 
                                    self.screen_rect.centerx, 
                                    self.screen_rect.centery + 100)
        
    def show_main_menu(self):
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
        
    def show_game_ui(self, player, base, wave_number):
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
        
    def display_game_over(self, victory):
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
        
    def check_button(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.show_menu:
            if self.start_button.is_clicked(mouse_pos):
                self.game_active = True
                self.show_menu = False
                return "start_game"
            elif self.exit_button.is_clicked(mouse_pos):
                return "exit_game"
        elif self.show_game_over_screen:
            if self.restart_button.is_clicked(mouse_pos):
                self.game_active = True
                self.show_game_over_screen = False
                return "restart_game"
        elif self.game_active:
            if self.upgrade_button.is_clicked(mouse_pos):
                return "upgrade_defense"
                
        return None
        
    def display(self, game_state, player=None, base=None, wave_number=1):
        """Display the appropriate UI based on game state."""
        if game_state == "menu":
            self.show_menu = True
            self.game_active = False
            self.show_game_over_screen = False
            self.show_main_menu()
        elif game_state == "playing":
            self.show_menu = False
            self.game_active = True
            self.show_game_over_screen = False
            self.show_game_ui(player, base, wave_number)
        elif game_state == "game_over":
            self.show_menu = False
            self.game_active = False
            self.show_game_over_screen = True
            self.display_game_over(self.victory) 