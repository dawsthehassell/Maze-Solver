from main import Cell, Window
from tkinter import Tk, BOTH, Canvas
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Maze dimensions must be greater than 0!")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(self.num_cols):
            column = []
            for row in range(self.num_rows):
                new_cell = Cell(
                    x1=self.x1 + col * self.cell_size_x,
                    y1=self.y1 + row * self.cell_size_y,
                    x2=self.x1 + col * self.cell_size_x + self.cell_size_x,
                    y2=self.y1 + row * self.cell_size_y + self.cell_size_y,
                    win=self._win
                )
                column.append(new_cell)
            self._cells.append(column)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)
    
    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        exit_cell = self._cells[self.num_rows-1][self.num_cols-1]
        entrance_cell.has_top_wall = False
        exit_cell.has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_rows-1, self.num_cols-1)

    def _draw_cell(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        cell = self._cells[i][j]
        cell.draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)