from game import Game
from config import BoardConfig


config = BoardConfig()
game = Game(config)
game.addPlayer("nick")
game.addPlayer("steeve")
game.addPlayer("rogers")
game.addPlayer("thor")

winners = []
while len(winners) != 2:
    for player in game.players:
        status = game.movePlayer(player)
        if status:
            winners.append(player.__dict__)
            game.players.remove(player)
            break
print(f"""
WINNERS
         1st Winner: {winners[0]}
         2nd Winner: {winners[1]}
""")

print("\nREMAINING")

for player in game.players:
    print("\t", player.__dict__)