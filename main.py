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

    def wait_for_close(self):
        self.running = True
        while self.running is True:
            self.redraw()
            # slows down redraw() for CPU sake
            time.sleep(0.01)

    def close(self):
        self.running = False

def main():
    win = Window(800,600)
    win.wait_for_close()

if __name__ == "__main__":
    main()