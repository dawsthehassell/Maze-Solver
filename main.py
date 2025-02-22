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
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall: 
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

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
    # Create a window first (assuming you have graphics.py)

    # Create a small test maze
    # Parameters:
    # - Start at position (50,50) in the window
    # - Create a 3x3 grid
    # - Each cell is 40x40 pixels
    test_maze = Maze(
        x1=100,           # start 50 pixels from left
        y1=100,           # start 50 pixels from top
        num_rows=6,      # small 3x3 maze
        num_cols=6,
        cell_size_x=60,  # cells are 40x40 pixels
        cell_size_y=60,
        win=win
    )
    win.wait_for_close()

if __name__ == "__main__":
    main()