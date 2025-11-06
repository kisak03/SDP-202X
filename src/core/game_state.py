import json
import os

class GameState:
    """
    Holds and manages core player and game status data.
    Loads initial player stats from data/player_config.json
    """
    def __init__(self):
        # Load initial player configuration
        config_path = os.path.join(os.path.dirname(__file__), "..", "data", "player_config.json")
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)

        # Player core stats
        self.hp = cfg.get('health', 3)
        self.attack_speed = cfg.get('speed', 300)
        self.attack_power = 10

        # Level / Exp stats
        self.exp = 0
        self.level = 1
        self.level_exp = 50

        # Item storage
        self.items = {"bomb" : 2, "heal": 0}

        # Player configuration values
        self.scale = cfg.get("scale", 0.5)
        self.invincible = cfg.get("invincible", False)
        self.hitbox_scale = cfg.get("hitbox_scale", 1.0)

    # Getter / Setter functions

    def get_exp(self):
        return self.exp

    def set_exp(self, value: int):
        self.exp = max(0, value)

    def get_level(self):
        return self.level

    def set_level(self, value: int):
        self.level = max(1, value)

    def get_level_exp(self):
        return self.level_exp

    def set_level_exp(self, value: int):
        self.level_exp = value

    def reset_exp(self):
        self.exp = 0

    def calc_next_level_exp(self):
        """Increase required EXP for next level with gradual exponential growth. """
        base = self.level_exp
        growth = 1.2
        self.level_exp = int(base * (growth ** (self.level - 1)))