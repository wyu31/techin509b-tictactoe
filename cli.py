from game import Game

if __name__ == "__main__":
    mode = int(input("Choose mode (1 for single player, 2 for two players): "))
    game = Game(mode)
    game.play()