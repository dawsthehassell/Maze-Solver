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

    def test_break_entrance_exit_walls(self):
        num_rows = 10
        num_cols = 10
        fake_window = Mock()
        m4 = Maze(50, 50, num_rows, num_cols, 15, 15, win=fake_window)
        m4._break_entrance_and_exit()
        entrance_cell = m4._cells[0][0]
        self.assertFalse(entrance_cell.has_top_wall, "Entrance wall should be removed")
        exit_cell = m4._cells[m4.num_rows-1][m4.num_cols-1]
        self.assertFalse(exit_cell.has_bottom_wall, "Exit wall should be removed")

    def test_reset_visited_cells(self):
        num_rows = 15
        num_cols = 15
        fake_window = Mock()
        m5 = Maze(50, 50, num_rows, num_cols, 15, 15, win=fake_window)
        for row in m5._cells:
            for cell in row:
                cell.visited = True
        m5._reset_cells_visited()
        for row in m5._cells:
            for cell in row:
                self.assertFalse(cell.visited, "All cells should have visited set to False")

if __name__ == "__main__":
    unittest.main()