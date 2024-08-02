import json
import os
class GameStats():
    """ Track statistics for Alien Invasion """
    def __init__(self, ai_settings):
        """ Initialize statistics. """
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # Load the high score from a file:
        self.high_score = GameStats.load_high_score()
        print("Loaded high score:", self.high_score)

    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    @staticmethod
    def load_high_score():
        """ Load the high score from a file. """
        filename = 'high_score.json'
        if not os.path.isfile(filename):
            print(f"{filename} does not exist. Creating file with default high score.")
            # Create the file with a default high score of 0 if it doesn't exist
            with open(filename, 'w') as f:
                json.dump(0, f)
            return 0

        # If the file exists, read and return the high score
        try:
            with open(filename) as f:
                score = json.load(f)
                print(f"High score read from file: {score}")
                return score
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading {filename}: {e}")
            return 0