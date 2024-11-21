class Game:
    def __init__(self, title, publisher, config):
        self.title = title 
        self.publisher = publisher
        self.__config = config

    def start(self):
        print("starting the game...")
    
    @staticmethod
    def end():
        print("ending the game...")


class PS5Game(Game):
    def __init__(self, title, publisher, config, engine):
        super().__init__(title, publisher, config) # მშობელი კლასის კონსტრუქტორი
        # self.title = title
        self.engine = engine
    
    def __str__(self):
        return f"Game: {self.title}; Publisher: {self.publisher}; Config: {self._Game__config}; Engine: {self.engine}"

    # def __repr__(self):
        # return f"PS5Game(game={self.title}, publisher = {self.publisher}, config = {self._config}, engine = {self.engine})"


ps5_game = PS5Game(title="FIFA 24", publisher="EA Sports", config="conf", engine="PS")
print(ps5_game)

game = Game("FIfa", "ea", "conf")
print(game._Game__config)
