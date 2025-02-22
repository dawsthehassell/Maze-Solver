import unittest
from maze import *
from main import *
from unittest.mock import Mock

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        fake_window = Mock()
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win=fake_window)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_create_cells_2(self):
        num_cols = 15
        num_rows = 15
        fake_window = Mock()
        m2 = Maze(50, 50, num_rows, num_cols, 15, 20, win=fake_window)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_create_cells_3(self):
        num_cols = 10
        num_rows = 2
        fake_window = Mock()
        m3 = Maze(20, 25, num_rows, num_cols, 10, 15, win=fake_window)
        self.assertEqual(len(m3._cells), num_cols)
        self.assertEqual(len(m3._cells[0]), num_rows)

    def test_zero_dimensions(self):
        with self.assertRaises(ValueError):
            Maze(0, 0, 0, 0, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 5, 0, 10, 10)
        with self.assertRaises(ValueError):
            Maze(0, 0, 0, 5, 10, 10)

if __name__ == "__main__":
    unittest.main()