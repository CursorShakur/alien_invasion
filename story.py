# Narrative snippets
import pygame

class Story:
    def __init__(self):
        """Initialize story elements."""
        self.intro_text = [
            "The year is 2150. Earth has established colonies across the solar system.",
            "But now, an alien invasion threatens humanity's existence.",
            "As the commander of Earth's last defense base, your mission is to protect",
            "what remains of humanity from the relentless alien attacks.",
            "Use your resources wisely, upgrade your defenses, and fight back!"
        ]
        
        self.wave_intros = [
            "The first wave of alien scouts approaches. Prepare for battle!",
            "The aliens have analyzed your defenses. They're sending in stronger forces!",
            "A massive alien warship has arrived. Brace for impact!",
            "The alien mothership has deployed elite warriors. Stand your ground!",
            "This is it - the final assault. The fate of humanity rests in your hands!"
        ]
        
        self.victory_text = [
            "You've successfully repelled the alien invasion!",
            "Earth's colonies can now rebuild and recover.",
            "Your name will be remembered in the annals of human history.",
            "But stay vigilant... the aliens may return someday."
        ]
        
        self.defeat_text = [
            "Your base has fallen to the alien forces.",
            "Earth's last defense has crumbled.",
            "But perhaps, somewhere among the stars,",
            "humanity will rise again..."
        ]
        
    def display_intro(self, screen, font):
        """Display the introduction story."""
        return self._display_text(screen, font, self.intro_text)
        
    def display_wave_intro(self, screen, font, wave_number):
        """Display the introduction for a specific wave."""
        # Get appropriate wave intro text based on wave number
        index = min(wave_number - 1, len(self.wave_intros) - 1)
        return self._display_text(screen, font, [self.wave_intros[index]])
        
    def display_victory(self, screen, font):
        """Display the victory text."""
        return self._display_text(screen, font, self.victory_text)
        
    def display_defeat(self, screen, font):
        """Display the defeat text."""
        return self._display_text(screen, font, self.defeat_text)
        
    def _display_text(self, screen, font, text_lines):
        """Helper method to display text on the screen."""
        screen_rect = screen.get_rect()
        
        # Render each line of text
        rendered_lines = []
        for line in text_lines:
            rendered_line = font.render(line, True, (255, 255, 255))
            rendered_lines.append(rendered_line)
            
        # Calculate total height of all lines
        line_height = rendered_lines[0].get_height()
        total_height = line_height * len(rendered_lines)
        
        # Calculate starting y position to center text vertically
        start_y = (screen_rect.height - total_height) // 2
        
        # Blit each line to the screen
        for i, line in enumerate(rendered_lines):
            line_rect = line.get_rect()
            line_rect.centerx = screen_rect.centerx
            line_rect.y = start_y + i * line_height
            screen.blit(line, line_rect)
            
        return True  # Indicate that text has been displayed 