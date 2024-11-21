class Game:
    def __init__(self, title, publisher):
        self.title = title 
        self.publisher = publisher

    def start(self):
        raise NotImplementedError("Override method in subclass")
    
    @staticmethod
    def end():
        print("ending the game...")


class PS5Game(Game):
    def __init__(self, title, publisher, engine):
        super().__init__(title, publisher) # მშობელი კლასის კონსტრუქტორი
        # self.title = title
        self.engine = engine

    def start(self):
        print("starting on PS")

    def __str__(self):
        return f"Game: {self.title}; Publisher: {self.publisher}; Engine: {self.engine}"


class PCGame(Game):
    def __init__(self, engine, **kwargs):
        # self.title = title
        self.engine = engine
        super().__init__(**kwargs) # მშობელი კლასის კონსტრუქტორი

    def start(self):
        print("starting on PC")

    def __str__(self):
        return f"Game: {self.title}; Publisher: {self.publisher}; Engine: {self.engine}"
        

ps5_game = PS5Game("FIFA 24", "EA Sports", "PS")
pc_game = PCGame("EU5", title="Manor Lords", publisher="Hooded horse")


ps5_game.start()
pc_game.start()

print(isinstance(ps5_game, Game))
