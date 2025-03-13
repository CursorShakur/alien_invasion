# Main game loop
import pygame
import sys
from pygame.sprite import Group

from settings import Settings
from player import Player
from base import Base
from enemies import EnemyWave
from resources import ResourceManager
from story import Story
from ui import UI
from input_handler import InputHandler
from renderer import Renderer
from collision_handler import CollisionHandler
from visual_effects import StarfieldGenerator
from game_state import GameStateManager

def run_game():
    print("Starting game initialization...")
    # Initialize pygame, settings, and screen object
    pygame.init()
    settings = Settings()
    print("Created settings...")
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    print("Created display...")
    
    # Create game state manager
    game_state_manager = GameStateManager(settings, screen)
    
    # Create UI
    ui = UI(settings, screen)
    print("Created game objects...")
    
    # Create handlers
    input_handler = InputHandler()
    renderer = Renderer()
    collision_handler = CollisionHandler()
    
    # Create a starfield background
    starfield_generator = StarfieldGenerator()
    stars = starfield_generator.create_stars(settings, screen, 100)
    print("Created starfield...")
    
    # Set up game clock
    clock = pygame.time.Clock()
    print("Starting main game loop...")
    
    # Start the main game loop
    while True:
        # Check for events
        action = input_handler.handle_events(game_state_manager.player, ui, game_state_manager.beams)
        
        # Process UI actions
        result = game_state_manager.handle_action(action)
        if result == "exit":
            print("Exiting game...")
            sys.exit()
        
        # Update based on current game state
        current_state = game_state_manager.get_state()
        
        if current_state == "playing":
            # Update game objects
            game_state_manager.update_playing_state()
            
            # Update stars
            stars = starfield_generator.update_stars(stars, settings)
            
            # Check for beam-alien collisions
            collision_handler.check_beam_alien_collisions(
                game_state_manager.beams, 
                game_state_manager.enemy_wave.aliens, 
                game_state_manager.resource_manager
            )
            
            # Check if aliens have reached the bottom
            if collision_handler.check_aliens_bottom(
                screen, 
                game_state_manager.enemy_wave.aliens, 
                game_state_manager.base
            ):
                # Check if base is destroyed
                if game_state_manager.base.health <= 0:
                    print("Game over - Base destroyed!")
                    game_state_manager.end_game(victory=False)
        
        # Update the screen
        renderer.update_screen(
            settings, 
            screen, 
            game_state_manager.player, 
            game_state_manager.base, 
            game_state_manager.enemy_wave, 
            game_state_manager.beams, 
            ui, 
            current_state,
            game_state_manager.resource_manager,
            game_state_manager
        )
        
        # Pass victory status to UI
        ui.victory = game_state_manager.victory
        
        # Control the game speed
        clock.tick(settings.fps)

def main():
    try:
        print("Starting Alien Invasion...")
        run_game()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 