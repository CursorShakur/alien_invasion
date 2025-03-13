# Handles user input and output
import pygame
from ui_components.ui_screens import MainMenuScreen, GameplayScreen, GameOverScreen

class UI:
    def __init__(self, settings, screen):
        """Initialize UI components."""
        self.settings = settings
        self.screen = screen
        
        # Game state
        self.game_active = False
        self.show_menu = True
        self.show_game_over_screen = False
        self.victory = False
        
        # Initialize screen components
        self.main_menu_screen = MainMenuScreen(settings, screen)
        self.gameplay_screen = GameplayScreen(settings, screen)
        self.game_over_screen = GameOverScreen(settings, screen)
    
    def check_button(self, mouse_pos):
        """Check if buttons are clicked."""
        if self.show_menu:
            return self.main_menu_screen.check_buttons(mouse_pos)
        elif self.show_game_over_screen:
            result = self.game_over_screen.check_buttons(mouse_pos)
            if result == "restart_game":
                self.game_active = True
                self.show_game_over_screen = False
            return result
        elif self.game_active:
            return self.gameplay_screen.check_buttons(mouse_pos)
                
        return None
        
    def display(self, game_state, player=None, base=None, wave_number=1, resource_manager=None, game_state_manager=None):
        """Display the appropriate UI based on game state."""
        if game_state == "menu":
            self.show_menu = True
            self.game_active = False
            self.show_game_over_screen = False
            self.main_menu_screen.display()
        elif game_state == "playing":
            self.show_menu = False
            self.game_active = True
            self.show_game_over_screen = False
            self.gameplay_screen.display(player, base, wave_number, resource_manager, game_state_manager)
        elif game_state == "game_over":
            self.show_menu = False
            self.game_active = False
            self.show_game_over_screen = True
            self.game_over_screen.display(self.victory) 