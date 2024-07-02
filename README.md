# LLD_snake_and_ladders

- This project is the implementation of the classic Snake and Ladders game using design patterns.
- This project has been designed according to the snakes/ladders drawn in the image `board_design.png`. 

## Overview

The game includes the following main components:
- Board
- Players
- Dice
- Snakes and Ladders

### BoardConfig Class
- `BoardConfig` class initializes the game board configuration with customizable parameters like board  size, number of dice, snakes, and ladders. 
- It provides default settings for a standard 100-tile board with predefined snakes and ladders positions.


### Board Class
- `Board` class implements a singleton pattern to ensure only one instance of the game board exists which would help in generating statistics of the played game 
- It uses the `BoardConfig` object to initialize the board with customizable settings for size, snakes, and ladders using `setBoard()`. Use the `get_instance()` method to access the single instance of the board.


### Player Class
- `Player` class represents a player in the game, initialized with a name. 
- It tracks the player's:
            - current position
            - number of turns taken
            - counts of snake bites 
            - counts of ladder climbs.


### Dice Class
- `Dice` class simulates rolling dice in the game, initialized with the number of dice (default=1). 
- `rollDice` method returns a random number representing the combined result of rolling the specified number of dice.


### Game Class
- `Game` class manages the overall gameplay. 
- It initializes with a `BoardConfig` object and sets up the board, dice, and players. 
- `addPlayer` method adds a player to the game. 
- `roll` method simulates dice rolls.
- `movePlayer` method updates a player's position based on dice rolls and board rules, handling encounters with snakes and ladders. 
- `isWinner` method checks if a player has won by reaching the final board position and will be called from `movePlayer` method.
- `movePlayer` method returns `player` instance if he/she wins, otherwise it returns None.


### Main Script (client)
This script sets up and runs a Snake and Ladders game using the `Game` and `BoardConfig` classes.
In this project:
 - I have added four players, simulates their turns until two players win.
 - Also displays the winners and remaining player's status.
