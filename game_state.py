# Game state manager
import pygame
from pygame.sprite import Group

from player import Player
from base import Base
from enemies import EnemyWave
from resources import ResourceManager

class GameStateManager:
    """Manages game states and transitions between states."""
    
    def __init__(self, settings, screen):
        """Initialize the game state manager."""
        self.settings = settings
        self.screen = screen
        self.state = "menu"  # Initial state
        
        # Game objects
        self.resource_manager = ResourceManager(settings)
        self.player = Player(settings, screen, self.resource_manager)
        self.base = Base(settings, screen)
        self.enemy_wave = EnemyWave(settings, screen)
        self.beams = Group()
        
        # Game status
        self.victory = False
        
        # Upgrade message
        self.show_upgrade_message = False
        self.upgrade_message = ""
        self.message_timer = 0
    
    def get_state(self):
        """Get the current game state."""
        return self.state
    
    def transition_to(self, new_state):
        """Transition to a new game state."""
        print(f"Transitioning from {self.state} to {new_state}")
        self.state = new_state
    
    def start_new_game(self):
        """Initialize a new game."""
        print("Starting new game...")
        self.transition_to("playing")
        
        # Reset game objects
        self.resource_manager = ResourceManager(self.settings)
        self.player = Player(self.settings, self.screen, self.resource_manager)
        self.base = Base(self.settings, self.screen)
        self.enemy_wave = EnemyWave(self.settings, self.screen)
        self.enemy_wave.create_fleet()
        self.beams = Group()
        
        # Reset victory status
        self.victory = False
        
        # Reset upgrade message
        self.show_upgrade_message = False
        self.upgrade_message = ""
        self.message_timer = 0
    
    def restart_game(self):
        """Restart the game after game over."""
        print("Restarting game...")
        self.start_new_game()
    
    def end_game(self, victory=False):
        """End the game with either victory or defeat."""
        self.transition_to("game_over")
        self.victory = victory
    
    def update_playing_state(self):
        """Update game objects in playing state."""
        # Update player
        self.player.update()
        
        # Update beams
        self.beams.update()
        
        # Remove beams that have gone off the top of the screen
        for beam in self.beams.copy():
            if beam.rect.bottom <= 0:
                self.beams.remove(beam)
        
        # Update aliens
        self.enemy_wave.update()
        
        # Update upgrade message timer
        if self.show_upgrade_message:
            self.message_timer -= 1
            if self.message_timer <= 0:
                self.show_upgrade_message = False
        
        # Check if all aliens are destroyed
        if len(self.enemy_wave.aliens) == 0:
            print(f"Wave {self.enemy_wave.wave_number} completed!")
            # Award bonus gems for completing wave
            self.resource_manager.earn_resources(self.enemy_wave.wave_number * 100)
            
            # Show wave completion message
            self.show_message(f"Wave {self.enemy_wave.wave_number} completed! Bonus: {self.enemy_wave.wave_number * 100} gems")
            
            # Start a new wave
            self.beams.empty()
            self.enemy_wave.spawn_enemies()
            
            # Check for victory condition (e.g., after 5 waves)
            if self.enemy_wave.wave_number > 5:
                print("Victory!")
                self.end_game(victory=True)
                
    def handle_action(self, action):
        """Handle UI actions."""
        if action == "start_game":
            self.start_new_game()
        elif action == "exit_game":
            return "exit"
        elif action == "restart_game":
            self.restart_game()
        elif action == "upgrade_defense":
            if self.state == "playing":
                print("Upgrading defense...")
                if self.base.upgrade_defense(self.resource_manager):
                    self.show_message(f"Base defense upgraded to level {self.base.defense_level}!")
                else:
                    self.show_message("Not enough gems for defense upgrade!")
        elif action == "upgrade_weapon":
            if self.state == "playing":
                print("Upgrading weapon...")
                if self.player.upgrade_weapon():
                    self.show_message(f"Weapon upgraded to {self.player.weapon.name}!")
                else:
                    self.show_message("Not enough gems for weapon upgrade!")
        elif action == "upgrade_speed":
            if self.state == "playing":
                print("Upgrading speed...")
                if self.player.upgrade_speed():
                    self.show_message(f"Speed upgraded to level {self.player.speed_level}!")
                else:
                    self.show_message("Not enough gems for speed upgrade!")
        elif action == "upgrade_fire_rate":
            if self.state == "playing":
                print("Upgrading fire rate...")
                if self.player.upgrade_fire_rate():
                    self.show_message(f"Fire rate upgraded to level {self.player.fire_rate_level}!")
                else:
                    self.show_message("Not enough gems for fire rate upgrade!")
        return None
        
    def show_message(self, message, duration=180):
        """Show a message on the screen for a duration (in frames)."""
        self.show_upgrade_message = True
        self.upgrade_message = message
        self.message_timer = duration 