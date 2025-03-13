# Helper functions for expansion
import pygame
import sys
import random

def check_events(player, ui, beams):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event, player, beams)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event, player)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            return ui.check_button(mouse_pos)
    return None

def _check_keydown_events(event, player, beams):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = True
    elif event.key == pygame.K_LEFT:
        player.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Fire a beam
        new_beam = player.fire_beam()
        beams.add(new_beam)
    elif event.key == pygame.K_q:
        sys.exit()

def _check_keyup_events(event, player):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        player.moving_right = False
    elif event.key == pygame.K_LEFT:
        player.moving_left = False

def update_screen(settings, screen, player, base, enemy_wave, beams, ui, game_state):
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
    
    # Draw the UI
    ui.display(game_state, player, base, enemy_wave.wave_number)
    
    # Make the most recently drawn screen visible
    pygame.display.flip()

def check_beam_alien_collisions(beams, aliens, player):
    """Check for collisions between beams and aliens."""
    # Check for any beams that have hit aliens
    # If so, get rid of the beam and the alien
    collisions = pygame.sprite.groupcollide(beams, aliens, True, False)
    
    # Process collisions
    if collisions:
        for aliens_hit in collisions.values():
            for alien in aliens_hit:
                # Apply damage to the alien
                if alien.take_damage(10):  # If alien is destroyed
                    alien.kill()
                    player.gems += 50  # Award gems for destroying an alien
                    
    return collisions

def check_aliens_bottom(screen, aliens, base):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Alien reached the bottom, damage the base
            base.take_damage(10)
            alien.kill()
            return True
    return False

def create_stars(settings, screen, num_stars=50):
    """Create a starfield background."""
    stars = []
    for _ in range(num_stars):
        x = random.randint(0, settings.screen_width)
        y = random.randint(0, settings.screen_height)
        size = random.randint(1, 3)
        brightness = random.randint(150, 255)
        color = (brightness, brightness, brightness)
        stars.append((x, y, size, color))
    return stars

def draw_stars(screen, stars):
    """Draw stars on the screen."""
    for x, y, size, color in stars:
        pygame.draw.circle(screen, color, (x, y), size) 