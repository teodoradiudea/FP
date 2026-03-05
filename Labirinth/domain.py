import random
from service import Serviceg

class Tgame:
    def __init__(self):
        self.s=Serviceg()
        self.last_move = ''

    def move(self, direction):
        col, row = self.s.get_row_col(3)
        if direction == 'up':
            if self.s.validate_move(col - 1,row):
                self.s.data[col][row] = 0
                self.s.data[col - 1][row] = 3
                self.last_move = 'up'


        elif direction == 'down':
            if self.s.validate_move(col + 1, row):
                self.s.data[col][row] = 0
                self.s.data[col + 1][row] = 3
                self.last_move = 'down'


        elif direction == 'left':
            if self.s.validate_move(col, row-1):
                self.s.data[col][row] = 0
                self.s.data[col][row - 1] = 3
                self.last_move = 'left'


        else:
            if self.s.validate_move(col, row + 1):
                self.s.data[col][row] = 0
                self.s.data[col][row + 1] = 3
                self.last_move = 'right'

        self.mino_move()

    def move_n_steps(self, n):
        while n > 0:
            self.move(self.last_move)
            n -= 1

    def mino_move(self):
        ok=1
        while ok==1:
            row=random.randint(0,11)
            col=random.randint(0,11)
            last_pos = self.s.get_row_col(2)
            if self.s.validate_mino(col,row):
                self.s.data[last_pos[0]][last_pos[1]] = 0
                self.s.data[col][row] = 2
                ok=0