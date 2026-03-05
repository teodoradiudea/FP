import repo
import texttable

class Serviceg:
    def __init__(self):
        self.r=repo.RepoFile()
        self.data = self.r.get_table()

    def validate_move(self, col, row):
        if self.data[col][row] == 1:
            raise ValueError("Can't move! There is a wall!!!")
        elif self.is_won(col, row):
            self.data[col][row] = 3
            print("Congrats, you won!")
            return True
        else:
            return True

    def validate_mino(self,col,row):
        if self.data[col][row] == 1:
            return False
        else:
            return True

    def get_row_col(self, character):
        for i in range (len(self.data)):#col
            for j in range (len(self.data)):#row
                if self.data[i][j] == character:
                    return i, j

    def is_won(self, col, row):
        if self.data[col][row] == 9:
            return True
        else:
            return False

    def is_lost(self, col, row, col2, row2):
        if row == row2 and col == col2:
            print("The mino caught you! Game over!")
            return True
        else:
            return False

    def draw_board(self):
        t = texttable.Texttable()
        for row in range(len(self.data)):
            row_data = ["  "] * len(self.data)
            for col in range(len(self.data)):
                if self.data[row][col] == 1:
                    row_data[col] = 'X'
                if self.data[row][col] == 0:
                    row_data[col] = ' '
                if self.data[row][col] == 9:
                    row_data[col] = '-'
                if self.data[row][col] == 2:
                    row_data[col] = 'M'
                if self.data[row][col] == 3:
                    row_data[col] = 'A'
            t.add_row(row_data)
        return t.draw()