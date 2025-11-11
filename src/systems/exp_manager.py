from src.core.game_state import GameState
# from src.scenes.levelup_scene import LevelupScene

class ExpManager:
    """
       Handles player EXP increase, level-up detection, and level-up logic.

       Methods:
           exp_up(amount): called when an enemy dies to increase EXP.
           is_level_up(): checks if EXP exceeds required level EXP.
           level_up(): triggers the level-up process (UI + stat increase).
           apply_level_choice(choice): applies selected bonus to GameState.
    """

    def __init__(self, game_state: GameState, scene_manager):
        self.game_state = game_state
        self.scene_manager = scene_manager

    def exp_up(self):
        pass

    def is_level_up(self):
        pass



    def level_up(self):
        pass

