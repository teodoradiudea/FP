from domain import Tgame

class Game:
    def __init__(self):
        self.dom=Tgame()

    def main(self):
        print("Welcome to the game!")
        print("You play as Ariadne(A). You have to escape Minotaur's(M) labyrinth.")
        print("To make a one-step move up write: up")
        print("To make a one-step move down write: down")
        print("To make a one-step move left write: left")
        print("To make a one-step move right write: right")
        print("To advance more steps in the same direction you did before write: move 'n'")
        print('\n')
        print("To start the game press 1")
        print("To exit the game press 2")
        print('\n')
        while True:
            choice=int(input(">"))
            if choice==1:

                while True:
                    print(self.dom.s.draw_board())

                    player = self.dom.s.get_row_col(3)
                    mino = self.dom.s.get_row_col(2)
                    game = self.dom.s.is_lost(player[0], player[1], mino[0], mino[1]) or self.dom.s.is_won(player[0], player[1])

                    if game is True:
                        break

                    ch = input(">> ").split()

                    if len(ch) == 1:
                        if ch[0] == "up":
                            self.dom.move('up')
                        elif ch[0]=="down":
                            self.dom.move('down')
                        elif ch[0]=="left":
                            self.dom.move('left')
                        elif ch[0]=="right":
                            self.dom.move('right')
                        elif ch[0]== "exit":
                            break
                        else:
                            print("Invalid command. try again. dont forget lowercaps only")
                    elif len(ch)==2:
                        if ch[0]=="move" and int(ch[1]):
                            self.dom.move_n_steps(int(ch[1]))
                        else:
                            print("Invalid command. try again. dont forget lowercaps only and the second is a number")
                            print("to move one step use:up,down,left,right")

            elif choice==2:
                break
            else:
                print("Invalid choice")

g=Game()
g.main()