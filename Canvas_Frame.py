import tkinter as tk
from random import randint

class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg = "Midnight Blue")
        self.canvas.pack(fill= "both", expand = True)

    def generate_random_graph(self, nodes):
        self.canvas.create_oval(0, 0, 500, 500, fill="red")