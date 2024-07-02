import random

class Dice:
    def __init__(self, dice_cnt:int=1) -> None:
        self.dice_cnt = dice_cnt
    
    def rollDice(self):
        return random.randint(self.dice_cnt, self.dice_cnt*6)