from board import Board
from dice import Dice
from config import BoardConfig
from player import Player

class Game:
    def __init__(self, config:BoardConfig) -> None:
        self.players = []
        self.config = config
        self.dice = Dice(config.dices)
        self.board = Board(config)
    
    def addPlayer(self, name):
        self.players.append(Player(name))
    
    def roll(self):
        return self.dice.rollDice()
    
    def getNewPosition(self, position:int):
        if position in self.config.snakes:
            return self.config.snakes[position], "snake"
        
        elif position in self.config.ladders:
            return self.config.ladders[position], "ladder"
        
        return position, "normal"
    
    def movePlayer(self, player:Player):
        rolled_value = self.roll()
        self.dice_value = rolled_value

        while rolled_value == self.dice.dice_cnt * 6:        
            bonus_role = self.roll()
            rolled_value = bonus_role
            self.dice_value += rolled_value
        
        new_position  = self.getNewPosition(player.position + self.dice_value)
        
        if new_position[0] <= self.board.board_size:
            player.position = new_position[0]
            player.turns_taken += 1

            if new_position[1] == "snake":
                print(f"{player.name} [SNAKE]: falled from {player.position} to {new_position[0]}")
                player.bite_count += 1
            elif new_position[1] == "ladder":
                print(f"{player.name} [LADDER]: climbed from {player.position} to {new_position[0]}")
                player.climb_count += 1

        if player.position == self.board.board_size:
            return self.isWinner(player)
    
    def isWinner(self, player):
        return player

