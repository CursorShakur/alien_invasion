# Renderer for the game
import pygame

class Renderer:
    """Handles rendering of game elements to the screen."""
    
    @staticmethod
    def update_screen(settings, screen, player, base, enemy_wave, beams, ui, game_state, resource_manager=None, game_state_manager=None):
        """Update images on the screen and flip to the new screen."""
        # Fill the screen with the background color
        screen.fill(settings.bg_color)
        
        # Draw the base
        base.draw()
        
        # Draw the player
        if game_state == "playing":
            player.blitme()
            
            # Draw all beams
            for beam in beams.sprites():
                beam.draw_beam()
                
            # Draw all aliens
            enemy_wave.aliens.draw(screen)
        
        # Draw the UI with resource manager and game state manager
        ui.display(game_state, player, base, enemy_wave.wave_number, resource_manager, game_state_manager)
        
        # Make the most recently drawn screen visible
        pygame.display.flip()
        
    @staticmethod
    def draw_stars(screen, stars):
        """Draw stars on the screen."""
        for x, y, size, color in stars:
            pygame.draw.circle(screen, color, (x, y), size) 