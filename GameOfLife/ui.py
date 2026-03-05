from domain import Board
from repository import TextfileRepo
from service import Service


class Game:
    def __init__(self):
        self.board = Board()
        self.repo = TextfileRepo(self.board)
        self.serv = Service(self.repo)

    def print_tutorial(self):
        print("Welcome to The Game of Life")
        print("- to add pattern: place patetrn_name coord_x coord_y")
        print("- save game: save filename.txt")
        print("- load game: load filename.txt")
        print("- game tutorial: tutorial")
        print("- exit game: exit")

    def start(self):
        self.print_tutorial()
        while True:
            print(self.board.draw_board())
            ch = input("\n> ").lower().split()

            if len(ch) == 1:
                if ch[0] == "exit":
                    break
                elif ch[0] == "tutorial":
                    self.print_tutorial()
                elif ch[0] == "tick":
                    self.serv.tick(1)

            elif len(ch) == 2:
                if ch[0] == "save":
                    self.repo._save(ch[1])
                elif ch[0] == "load":
                    self.repo._load(ch[1])
                elif ch[0] == "tick":
                    try:
                        n = int(ch[1])
                        self.serv.tick(n)
                    except ValueError:
                        print("Ticks must be followed by a number")

            elif len(ch) == 4:
                if ch[0] == "place":
                    try:
                        x, y = int(ch[2]), int(ch[3])
                        self.repo.load_patterns(ch[1])
                        self.serv.place_pattern(self.repo.patterns, x, y)
                    except ValueError:
                        print("Coordonates shpuld be integers")

            else:
                print("Invalid command")
g = Game()
g.start()