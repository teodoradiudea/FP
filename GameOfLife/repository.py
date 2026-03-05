from domain import Board

class TextfileRepo:
    def __init__(self, b:Board):
        self.b = b
        self.data = b.data
        self.patterns=[]
        self._file_loaded= False
        self._file_loaded2= False

    def get_entities(self):
        entities = self.data
        return entities

    def get_pattern(self):
        return self.patterns

    def get_pattern_array(self, pattern):
        array = []
        row = []
        for i in range(len(pattern)):
            if pattern[i] == "[":
                row = []
            elif pattern[i] == ",":
                continue
            elif pattern[i] == "]":
                array.append(row)
            elif pattern[i] == '\n':
                continue
            else:
                row.append(int(pattern[i]))
        return array


    def place(self, pattern, x, y):
        """
        This function place the pattern on the board
        :param pattern: matrix of the pattern
        :param x: col coord
        :param y: row coord
        """
        l = len(pattern)
        for i in range(l):
            for j in range(l):
                if self.data[x+i-1][j+y-1] == 0 and pattern[i][j] == 1:
                    self.data[x+i-1][j+y-1] = pattern[i][j]

    def _load(self, filename):
        try:
            with open(filename, "rt") as fin:
                board = []
                for line in fin:
                    row = [int(x) for x in line.strip().split(',') if x != '']
                    board.append(row)

                self.b.set_board(board)
                self.data = self.b.data

        except FileNotFoundError:
            print(f"The file {filename} was not found.")

    def load_patterns(self, pattern):
        """
        Function loads the pattern type from file and passes it to self.patterns as a list of lists
        :param pattern: the name of the pattern
        """
        if self._file_loaded2:
            return
        self._file_loaded2 = True
        with open("patterns.txt", "r") as f:
            found = False
            for line in f:
                p = line.split("=")
                if p[0] == pattern:
                    self.patterns = self.get_pattern_array(p[1])
                    found = True
                    break
            if not found:
                raise ValueError(f"Pattern {pattern} was not found.")

    def _save(self, filename):
        board = self.b.get_board()
        with open(filename, "wt") as file:
            for row in board:
                file.write(",".join(str(coll) for coll in row) + "\n")