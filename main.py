from tkinter import Tk, BOTH, Canvas
import time
from maze import *

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.master = Tk()
        self.master.title("Maze Solver")
        self.canvas = Canvas(self.master, width=self.width, height=self.height)
        self.canvas.pack()
        self.running = False
        self.master.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.master.update_idletasks()
        self.master.update()

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()
            # slows down redraw() for CPU sake
            time.sleep(0.01)

    def close(self):
        self.running = False

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        x1 = self.point1.x
        y1 = self.point1.y
        x2 = self.point2.x
        y2 = self.point2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell:
    def __init__(self, x1, y1, x2, y2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
        self.visited = False

    def draw(self):
        # TOP WALL
        line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        color = "black" if self.has_top_wall else "white"
        self._win.draw_line(line, color)
        # LEFT WALL
        line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        color = "black" if self.has_left_wall else "white"
        self._win.draw_line(line, color)
        # BOTTOM WALL
        line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(line, color)
        # RIGHT WALL
        line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        color = "black" if self.has_right_wall else "white"
        self._win.draw_line(line, color)

    def draw_move(self, to_cell, undo=False):
        center_x = self._x1 + ((self._x2 - self._x1) / 2)
        center_y = self._y1 + ((self._y2 - self._y1) / 2)
        to_center_x = to_cell._x1 + ((to_cell._x2 - to_cell._x1) / 2)
        to_center_y = to_cell._y1 + ((to_cell._y2 - to_cell._y1) / 2)
        if undo == False:
            line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))
            self._win.draw_line(line, "red")
        else:
            line = Line(Point(center_x, center_y), Point(to_center_x, to_center_y))
            self._win.draw_line(line, "gray")

def main():
    win = Window(800,600)
    maze = Maze(
        x1=100,
        y1=100,
        num_rows=6,
        num_cols=6,
        cell_size_x=60,
        cell_size_y=60,
        win=win
    )
    maze._create_cells()
    maze._break_walls_r(0, 0)
    maze._break_entrance_and_exit()
    maze._reset_cells_visited()
    maze.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()