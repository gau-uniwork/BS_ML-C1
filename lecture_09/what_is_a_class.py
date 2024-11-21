class Game:
    engine = "EU5" # საერთო ყველა ობიექტისთვის

    def __init__(self, title):
        self.title = title # ყველა ობიექტისთვის განსხვავებული
    
    def start(self):
        print("starting the game...")
    
    @staticmethod
    def end():
        print("ending the game...")


obj = Game(title="The Ghost of Tsushima")
print(obj)
print(obj.title)

# obj.title = "The Ghost of Tsushima"
print(obj.title)
print(type(obj))

obj.start()
obj.end()

Game.end()
