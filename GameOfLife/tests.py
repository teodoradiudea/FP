import unittest
from domain import Board
from repository import TextfileRepo
from service import Service


class TestService(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.repo = TextfileRepo(self.board)
        self.service = Service(self.repo)
        self.block = [1,1],[1,1]

    def test_place_pattern(self):
        """
        validation test
        """
        self.service.place_pattern(self.block, 1, 1)
        board = self.board.get_board()
        self.assertEqual(board[0][0], 1)
        self.assertEqual(board[0][1], 1)
        self.assertEqual(board[1][0], 1)
        self.assertEqual(board[1][1], 1)

        """
        out of board coordonates test
        """
        with self.assertRaises(Exception):
            self.service.place_pattern(self.block, 8, 8)

        """
        overlap live cells test
        """
        self.service.place_pattern(self.block, 1, 1)
        with self.assertRaises(Exception):
            self.service.place_pattern(self.block, 1, 1)


    def test_tick(self):
        """
        block unchanged after tick test
        """
        self.service.place_pattern(self.block, 1, 1)
        self.service.tick(1)
        board = self.board.get_board()
        expected = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(board[0][0], expected[0][0])
        self.assertEqual(board[0][1], expected[0][1])
        self.assertEqual(board[1][0], expected[1][0])
        self.assertEqual(board[1][1], expected[1][1])

        """
        single live cell should die test
        """
        self.board.data[3][3] = 1
        self.service.tick(1)
        self.assertEqual(self.board.data[3][3], 0)

if __name__ == "__main__":
    unittest.main()