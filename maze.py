from main import Cell, Window
from tkinter import Tk, BOTH, Canvas
import time, random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        if num_rows <= 0 or num_cols <= 0:
            raise ValueError("Maze dimensions must be greater than 0!")
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
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

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        to_visit = []
        if i > 0 and not self._cells[i-1][j].visited:
            to_visit.append((i-1, j, "N"))
        if j < self.num_cols-1 and not self._cells[i][j+1].visited:
            to_visit.append((i, j+1, "E"))
        if i < self.num_rows-1 and not self._cells[i+1][j].visited:
            to_visit.append((i+1, j, "S"))
        if j > 0 and not self._cells[i][j-1].visited:
            to_visit.append((i, j-1, "W"))
        
        if len(to_visit) == 0:
            self._draw_cell(i, j)
            return
        else:
            random_index = random.randrange(len(to_visit))
            next_cell_i, next_cell_j, direction = to_visit[random_index]
            if direction == "N":
                self._cells[i][j].has_top_wall = False
                self._cells[next_cell_i][next_cell_j].has_bottom_wall = False
            elif direction == "E":
                self._cells[i][j].has_right_wall = False
                self._cells[next_cell_i][next_cell_j].has_left_wall = False
            elif direction == "S":
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_cell_i][next_cell_j].has_top_wall = False
            elif direction == "W":
                self._cells[i][j].has_left_wall = False
                self._cells[next_cell_i][next_cell_j].has_right_wall = False
            self._break_walls_r(next_cell_i, next_cell_j)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)