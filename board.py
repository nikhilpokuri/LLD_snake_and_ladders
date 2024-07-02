class Board:
    __instance = None

    @staticmethod
    def get_instance():
        if Board.__instance == None:
            Board()
        return Board.__instance
    
    def __init__(self, config:object) -> None:
        if Board.__instance == None:
            Board.__instance = self
            Board.__instance.setBoard(config)
        else:
            raise Exception("Cannot Create New Instance / Use get_instance()")

    def setBoard(self, config:object):
        self.board_size = config.board_size
        self.snakes = config.snakes
        self.ladders = config.ladders

    