class Player:
    def __init__(self, name:str) -> None:
        self.name = name
        self.position = 0
        self.turns_taken = 0
        self.bite_count = 0
        self.climb_count = 0