# Stores game configurations
class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)  # Black background
        
        # Player settings
        self.player_speed = 5
        self.player_health = 100
        self.player_beam_speed = 10
        self.player_beam_width = 3
        self.player_beam_color = (0, 255, 0)  # Green beam
        
        # Enemy settings
        self.enemy_speed = 2
        self.enemy_health = 20
        self.enemy_points = 50  # Points earned for destroying an enemy
        self.wave_increment = 5  # Number of additional enemies per wave
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        
        # Resource settings
        self.initial_gems = 100
        self.upgrade_cost = 50
        
        # Game settings
        self.fps = 60
        self.difficulty_scale = 1.2  # Multiplier for difficulty increase per wave 