import tkinter as tk
from random import randint
import math
from Dictionaries import node_dict

class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg = "Midnight Blue")
        self.canvas.pack(fill= "both", expand = True)

        self.node_count = 0

    def add_node(self, event):
        size = 50

        xcoord1 = event.x - (size / 2)
        ycoord1 = event.y - (size / 2)
        xcoord2 = event.x + (size / 2)
        ycoord2 = event.y + (size / 2)

        self.node_count += 1
        self.canvas.create_oval(xcoord1, ycoord1, xcoord2, ycoord2, fill = "red", outline = "red")
        self.canvas.create_text((xcoord1 + xcoord2) // 2, (ycoord1 + ycoord2) // 2, text= self.node_count,
                                font= ("Helvetica", 20))

        node_dict[self.node_count] = {"x": (xcoord1 + xcoord2) // 2,
                                      "y": (ycoord1 + ycoord2) // 2}

    def add_edge(self, node1, node2, weight):
        size = 10

        xcoord1 = node_dict[node1]["x"]
        ycoord1 = node_dict[node1]["y"]
        xcoord2 = node_dict[node2]["x"]
        ycoord2 = node_dict[node2]["y"]

        self.canvas.create_line(xcoord1, ycoord1, xcoord2, ycoord2, fill = "red", width = size)
        self.canvas.create_text(node_dict[node1]["x"], node_dict[node1]["y"], text=node1,
                                font=("Helvetica", 20))
        self.canvas.create_text(node_dict[node2]["x"], node_dict[node2]["y"], text=node2,
                                font=("Helvetica", 20))

        node_dict[node1][node2] = weight
        node_dict[node2][node1] = weight

        print(node_dict)

    def generate_random_graph(self, nodes):
        self.canvas.delete("all")
        cols = math.ceil(math.sqrt(nodes))
        rows = math.ceil(nodes / cols)

        cell_height = self.canvas.winfo_height() // rows
        cell_width = self.canvas.winfo_width() // cols

        node_count = 0

        first_node = randint(0, nodes - 1)
        last_node = randint(0, nodes - 1)
        while first_node == last_node:
            last_node = randint(0, nodes)
            print(first_node, last_node)
        print(first_node, last_node)

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

                if node_count == first_node:
                    self.canvas.create_oval(x, y, x + node_size, y + node_size, fill = "green", outline= "green")
                elif node_count == last_node:
                    self.canvas.create_oval(x, y, x + node_size, y + node_size, fill = "black", outline= "black")
                else:
                    self.canvas.create_oval(x, y, x + node_size, y + node_size, fill = "red", outline= "red")
                node_count += 1