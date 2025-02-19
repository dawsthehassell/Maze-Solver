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

def main():
    win = Window(800,600)
    points = [
        (Point(50, 50), Point(200, 200)),
        (Point(100, 50), Point(300, 150)),
        (Point(150, 100), Point(250, 300)),
        (Point(200, 150), Point(300, 350)),
    ]
    for start, end in points:
        line = Line(start, end)
        win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()