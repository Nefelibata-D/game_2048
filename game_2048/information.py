# noinspection PyRedundantParentheses
class Information():

    def __init__(self):
        self.score = 0
        self.best_score = 0
        self.game_over = False
        self.roll_back_able = False
        self.game_finish = False
        
    def reset(self):
        self.score = 0
        self.game_over = False
