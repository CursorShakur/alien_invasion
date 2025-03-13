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
import utils

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
    
    # Create game objects
    player = Player(settings, screen)
    base = Base(settings, screen)
    enemy_wave = EnemyWave(settings, screen)
    resource_manager = ResourceManager(settings)
    story = Story()
    ui = UI(settings, screen)
    print("Created game objects...")
    
    # Set up pygame sprite groups
    beams = Group()
    
    # Create a starfield background
    stars = utils.create_stars(settings, screen, 100)
    print("Created starfield...")
    
    # Set the game state
    game_state = "menu"
    clock = pygame.time.Clock()
    print("Starting main game loop...")
    
    # Start the main game loop
    while True:
        # Check for events
        action = utils.check_events(player, ui, beams)
        
        # Process UI actions
        if action == "start_game":
            print("Starting new game...")
            game_state = "playing"
            # Initialize game objects for a new game
            player = Player(settings, screen)
            base = Base(settings, screen)
            enemy_wave = EnemyWave(settings, screen)
            enemy_wave.create_fleet()
            resource_manager = ResourceManager(settings)
            beams = Group()
        elif action == "exit_game":
            print("Exiting game...")
            sys.exit()
        elif action == "restart_game":
            print("Restarting game...")
            game_state = "playing"
            # Reset game objects
            player = Player(settings, screen)
            base = Base(settings, screen)
            enemy_wave = EnemyWave(settings, screen)
            enemy_wave.create_fleet()
            resource_manager = ResourceManager(settings)
            beams = Group()
        elif action == "upgrade_defense":
            if game_state == "playing":
                print("Upgrading defense...")
                base.upgrade_defense(resource_manager)
        
        # Update game objects if the game is active
        if game_state == "playing":
            # Update player
            player.update()
            
            # Update beams
            beams.update()
            
            # Remove beams that have gone off the top of the screen
            for beam in beams.copy():
                if beam.rect.bottom <= 0:
                    beams.remove(beam)
            
            # Update aliens
            enemy_wave.update()
            
            # Check for beam-alien collisions
            utils.check_beam_alien_collisions(beams, enemy_wave.aliens, player)
            
            # Check if aliens have reached the bottom
            if utils.check_aliens_bottom(screen, enemy_wave.aliens, base):
                # Check if base is destroyed
                if base.health <= 0:
                    print("Game over - Base destroyed!")
                    game_state = "game_over"
                    ui.victory = False
            
            # Check if all aliens are destroyed
            if len(enemy_wave.aliens) == 0:
                print(f"Wave {enemy_wave.wave_number} completed!")
                # Start a new wave
                beams.empty()
                enemy_wave.spawn_enemies()
                
                # Check for victory condition (e.g., after 5 waves)
                if enemy_wave.wave_number > 5:
                    print("Victory!")
                    game_state = "game_over"
                    ui.victory = True
        
        # Update the screen
        utils.update_screen(settings, screen, player, base, enemy_wave, beams, ui, game_state)
        
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