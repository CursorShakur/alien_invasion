# Collision handler for the game
import pygame

class CollisionHandler:
    """Handles collision detection and resolution in the game."""
    
    @staticmethod
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

    @staticmethod
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