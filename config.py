class BoardConfig:
    def __init__(self, size:int=100, dices:int=1, snakes:dict={}, ladders:dict={}) -> None:
        self.board_size = size
        self.dices = dices
        self.snakes = snakes or {97:78, 95:56, 88:24, 62:18, 48:26, 36:6, 32:10}
        self.ladders = ladders or {1:38, 4:14, 8:30, 21:42, 28:76, 50:67, 71:92, 80:99}
