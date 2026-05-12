import tkinter as tk
from random import randint
import math

class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg = "Midnight Blue")
        self.canvas.pack(fill= "both", expand = True)

    def generate_random_graph(self, nodes):
        self.canvas.delete("all")
        cols = math.ceil(math.sqrt(nodes))
        rows = math.ceil(nodes / cols)

        cell_height = self.canvas.winfo_height() // rows
        cell_width = self.canvas.winfo_width() // cols

        node_count = 0

        for row in range(rows):
            for col in range(cols):
                if node_count >= nodes:
                    break

                cell_x1 = col * cell_width
                cell_y1 = row * cell_height
                cell_x2 = cell_x1 + cell_width
                cell_y2 = cell_y1 + cell_height

                node_size = min(cell_height, cell_width) // 3

                x = randint(cell_x1, cell_x2 - node_size)
                y = randint(cell_y1, cell_y2 - node_size)
                self.canvas.create_oval(x, y, x + node_size, y + node_size, fill = "red", outline= "red")
                node_count += 1