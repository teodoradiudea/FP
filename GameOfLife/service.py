from repository import TextfileRepo


class Service:
    def __init__(self, repo:TextfileRepo):
        self.repo = repo
        self.board = repo.b
        self.patterns=repo.patterns


    def pattern_validation(self, data):
        """
        The function first loads the pattern type from file and places it to the board
        :param data: data[0] is the name of the pattern and data[1] holds the coord
        :raises: Exception if the pattern isn't valid
        """
        self.repo.load_patterns(data[0])
        coord = data[1].strip(' ').split(',')
        if len(coord) == 1:
            raise Exception("Not enough coordonates")
        try:
            x = int(coord[0])
            y = int(coord[1])
        except ValueError:
            raise Exception("Coordonates should be integers")
        try:
            self.repo.place(self.patterns, x, y)
        except Exception as e:
            raise Exception(e)

    def place_pattern(self, pattern, x, y):
        """
        This function ensures that the pattern doesn't have any live cell outside of the border
        :param pattern: matrix of the pattern
        :param x: col coord
        :param y: row coord
        """
        l = len(pattern)

        for i in range(l):
            for j in range(l):
                bx = x + i - 1
                by = y + j - 1

                if not (0 <= bx < 8 and 0 <= by < 8):
                    if pattern[i][j] == 1:
                        raise Exception("Live cell outside of board.")
                    continue

                if pattern[i][j] == 1 and self.repo.data[bx][by] == 1:
                    raise Exception("You cannot overlap a live cell.")

        self.repo.place(pattern, x, y)

    def tick(self, gen):
        """
        The function computes the next generation due to some given features
        :param gen: the number of generations we want to pass
        """
        new_board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        for i in range(gen):
            current_board = self.board.get_board()
            for i in range(8):
                for j in range(8):
                    neighbours = self.get_neighbors(i, j, current_board)
                    if neighbours in [2, 3] and current_board[i][j] == 1:
                        new_board[i][j] = 1
                    elif neighbours < 2 and current_board[i][j] == 1:
                        new_board[i][j] = 0
                    elif neighbours > 3 and current_board[i][j] == 1:
                        new_board[i][j] = 0
                    elif neighbours == 3 and current_board[i][j] == 0:
                        new_board[i][j] = 1
        self.board.set_board(new_board)

    def get_neighbors(self, x, y, board):
        """
        Computes the number of neighbors of each zone
        :param x: coord
        :param y: coord
        :param board: the board we want to compute
        :return: the sum of neighbors
        """
        neighbord = 0
        for i in range (x-1, x+2):
            for j in range (y-1, y+2):
                if 0<=i and i < 8 and 0<=j and j < 8 and (i!=x or j!=y):
                    if board[i][j] == 1:
                        neighbord += 1
        return neighbord