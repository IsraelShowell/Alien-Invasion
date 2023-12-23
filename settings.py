#Creator: Israel Showell
#Date: 12-19-2023
#Project: Alien Invasion Game



class Settings():

    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        
        #Used to initialize static game settings, whatever we change here like screen width, will be changed in Alien_Invasio_Game.py

        self.screen_w = 1200

        self.screen_h = 800

        self.bg_color = (230,230,230)

        #Movement Speed
        self.ship_speed_factor = 1.5

        #Ship lives
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        #Alien Settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Controls how fast the game speeds up
        self.speedup_rate = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initializes the setting that change during gameplay"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #Scoring variable
        self.alien_points = 5

    def increase_speed(self):
        """Increases speed"""
        self.ship_speed_factor *= self.speedup_rate
        self.bullet_speed_factor *= self.speedup_rate
        self.alien_speed_factor *= self.speedup_rate

        self.alien_points = int(self.alien_points * self.score_scale)
