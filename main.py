from tkinter import Tk, BOTH, Canvas
import time

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

def main():
    win = Window(800,600)
    cell1 = Cell(50, 100, 150, 200, win)
    cell1.draw()
    
    cell2 = Cell(150, 200, 250, 300, win)
    cell2.draw()
    win.wait_for_close()

if __name__ == "__main__":
    main()