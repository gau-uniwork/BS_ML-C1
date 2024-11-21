class Game:
    def __init__(self, title, publisher):
        self.title = title 
        self.publisher = publisher

    def start(self):
        print("starting the game...")
    
    @staticmethod
    def end():
        print("ending the game...")


class PS5Game(Game):
    def __init__(self, title, publisher, engine):
        super().__init__(title, publisher) # მშობელი კლასის კონსტრუქტორი
        # self.title = title
        self.engine = engine


class PCGame(Game):
    def __init__(self, engine, **kwargs):
        # self.title = title
        self.engine = engine
        super().__init__(**kwargs) # მშობელი კლასის კონსტრუქტორი


ps5_game = PS5Game("FIFA 24", "EA Sports", "PS")
print(type(ps5_game))
print(ps5_game.title)
print(ps5_game.engine)
ps5_game.start()
ps5_game.end()


pc_game = PCGame("EU5", title="Manor Lords", publisher="Hooded horse")
print(pc_game.title)
print(pc_game.publisher)

print(isinstance(ps5_game, Game))
