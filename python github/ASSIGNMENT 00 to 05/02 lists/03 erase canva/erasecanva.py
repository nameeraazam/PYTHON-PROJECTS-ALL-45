import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.cells = []
        self.create_grid()
        
        # Create the eraser (initial position will be where the user clicks)
        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<B1-Motion>", self.move_eraser)
    
    def create_grid(self):
        """Create the grid of blue cells."""
        for row in range(CANVAS_HEIGHT // CELL_SIZE):
            for col in range(CANVAS_WIDTH // CELL_SIZE):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='blue')
                self.cells.append(cell)

    def create_eraser(self, event):
        """Create the eraser at the click location."""
        x = event.x
        y = event.y
        self.eraser = self.canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill='pink', outline='pink')

    def move_eraser(self, event):
        """Move the eraser and erase cells."""
        if self.eraser:
            x = event.x
            y = event.y
            # Move the eraser
            self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

            # Erase any cell that's within the eraser's area
            self.erase_cells(x, y)

    def erase_cells(self, eraser_x, eraser_y):
        """Erase cells in contact with the eraser."""
        for cell in self.cells:
            x1, y1, x2, y2 = self.canvas.coords(cell)
            if (eraser_x + ERASER_SIZE > x1 and eraser_x < x2) and (eraser_y + ERASER_SIZE > y1 and eraser_y < y2):
                self.canvas.itemconfig(cell, fill='white')

def main():
    root = tk.Tk()
    app = EraserCanvas(root)
    root.mainloop()

if __name__ == '__main__':
    main()
