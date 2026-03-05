import texttable

class Board:
    def __init__(self):
        self.data= [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

    def draw_board(self):
        t = texttable.Texttable()
        for row in range(8):
            row_data = ["  "] * 8
            for col in range(len(self.data)):
                if self.data[row][col] == 1:
                    row_data[col] = 'X'
                if self.data[row][col] == 0:
                    row_data[col] = ' '
            t.add_row(row_data)
        return t.draw()

    def get_board(self):
        return self.data

    def set_board(self, board):
        self.data = board

# b= Board()
# print(b.draw_board())