import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells2(self):
        num_cols = 100
        num_rows = 125
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), 125)
        self.assertEqual(len(maze._cells[120]), 100)

    def test_maze_create_cells3(self):
        num_cols = -1
        num_rows = 5
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), 5)
        self.assertEqual(len(maze._cells[0]), 0)

    def test_maze_create_cells4(self):
        num_cols = 10000
        num_rows = 1000
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), 1000)
        self.assertEqual(len(maze._cells[0]), 10000)

if __name__ == "__main__":
    unittest.main()

