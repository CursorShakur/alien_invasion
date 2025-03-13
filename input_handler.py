# Input handler for the game
import pygame
import sys

class InputHandler:
    """Class to handle player inputs and interactions."""
    
    @staticmethod
    def handle_events(player, ui, beams):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                InputHandler._handle_keydown_events(event, player)
            elif event.type == pygame.KEYUP:
                InputHandler._handle_keyup_events(event, player)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                return ui.check_button(mouse_pos)
        
        # Check for auto-firing
        if player.should_auto_fire():
            new_beam = player.fire_beam()
            beams.add(new_beam)
            
        return None

    @staticmethod
    def _handle_keydown_events(event, player):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            player.moving_right = True
        elif event.key == pygame.K_LEFT:
            player.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    @staticmethod
    def _handle_keyup_events(event, player):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            player.moving_right = False
        elif event.key == pygame.K_LEFT:
            player.moving_left = False 