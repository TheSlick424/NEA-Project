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

        node_dict[f"Node {self.node_count}"] = {"x": (xcoord1 + xcoord2) // 2,
                                      "y": (ycoord1 + ycoord2) // 2,
                                      "Start": False,
                                      "End": False}


    def remove_node(self, node):
        xcoord = node_dict[node]["x"]
        ycoord = node_dict[node]["y"]

        self.canvas.create_oval(xcoord - 25, ycoord - 25, xcoord + 25, ycoord + 25, fill = "Midnight Blue",
                                outline = "Midnight Blue")

        for key in node_dict[node]:
            if key[0:4] == "Node":
                xcoord2 = node_dict[key]["x"]
                ycoord2 = node_dict[key]["y"]
                if node_dict[key]["Start"]:
                    self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill="Dark Green",
                                            outline="DarkGreen")
                    self.canvas.create_text(xcoord2, ycoord2, text=key[6:],
                                            font=("Helvetica", 20))
                elif node_dict[key]["End"]:
                    self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill="Black",
                                            outline="Black")
                    self.canvas.create_text(xcoord2, ycoord2, text=key[6:], fill="white",
                                            font=("Helvetica", 20))
                else:
                    self.canvas.create_text(xcoord2, ycoord2, text=key[6:],
                                            font=("Helvetica", 20))

                del node_dict[key][node]

        node_dict.pop(node)

    def add_edge(self, node1, node2, weight):
        size = 10

        xcoord1 = node_dict[f"Node {node1}"]["x"]
        ycoord1 = node_dict[f"Node {node1}"]["y"]
        xcoord2 = node_dict[f"Node {node2}"]["x"]
        ycoord2 = node_dict[f"Node {node2}"]["y"]

        self.canvas.create_line(xcoord1, ycoord1, xcoord2, ycoord2, fill = "red", width = size)

        if node_dict[f"Node {node1}"]["Start"]:
            self.canvas.create_oval(xcoord1 - 25, ycoord1 - 25, xcoord1 + 25, ycoord1 + 25, fill = "Dark Green",
                                    outline= "DarkGreen")
            self.canvas.create_text(xcoord1, ycoord1, text=node1,
                                    font=("Helvetica", 20))
        elif node_dict[f"Node {node1}"]["End"]:
            self.canvas.create_oval(xcoord1 - 25, ycoord1 - 25, xcoord1 + 25, ycoord1 + 25, fill="Black",
                                    outline="Black")
            self.canvas.create_text(xcoord1, ycoord1, text=node1, fill= "white",
                                    font=("Helvetica", 20))
        else:
            self.canvas.create_text(xcoord1, ycoord1, text=node1,
                                    font=("Helvetica", 20))

        if node_dict[f"Node {node2}"]["Start"]:
            self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill = "Dark Green",
                                    outline= "DarkGreen")
            self.canvas.create_text(xcoord2, ycoord2, text=node2,
                                    font=("Helvetica", 20))
        elif node_dict[f"Node {node2}"]["End"]:
            self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill="Black",
                                    outline="Black")
            self.canvas.create_text(xcoord2, ycoord2, text=node2, fill= "white",
                                    font=("Helvetica", 20))
        else:
            self.canvas.create_text(xcoord2, ycoord2, text=node2,
                                    font=("Helvetica", 20))

        node_dict[f"Node {node1}"][f"Node {node2}"] = weight
        node_dict[f"Node {node2}"][f"Node {node1}"] = weight

    def remove_edge(self, nodes):
        node1 = nodes[0]
        node2 = nodes[1]

        xcoord1 = node_dict[node1]["x"]
        ycoord1 = node_dict[node1]["y"]
        xcoord2 = node_dict[node2]["x"]
        ycoord2 = node_dict[node2]["y"]

        self.canvas.create_line(xcoord1, ycoord1, xcoord2, ycoord2, fill = "Midnight Blue", width = 10)

        if node_dict[node1]["Start"]:
            self.canvas.create_oval(xcoord1 - 25, ycoord1 - 25, xcoord1 + 25, ycoord1 + 25, fill = "Dark Green",
                                    outline= "DarkGreen")
            self.canvas.create_text(xcoord1, ycoord1, text=node1[5:],
                                    font=("Helvetica", 20))
        elif node_dict[node1]["End"]:
            self.canvas.create_oval(xcoord1 - 25, ycoord1 - 25, xcoord1 + 25, ycoord1 + 25, fill="Black",
                                    outline="Black")
            self.canvas.create_text(xcoord1, ycoord1, text=node1[5:], fill= "white",
                                    font=("Helvetica", 20))
        else:
            self.canvas.create_text(xcoord1, ycoord1, text=node1[5:],
                                    font=("Helvetica", 20))

        if node_dict[node2]["Start"]:
            self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill = "Dark Green",
                                    outline= "DarkGreen")
            self.canvas.create_text(xcoord2, ycoord2, text=node2[5:],
                                    font=("Helvetica", 20))
        elif node_dict[node2]["End"]:
            self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill="Black",
                                    outline="Black")
            self.canvas.create_text(xcoord2, ycoord2, text=node2[5:], fill= "white",
                                    font=("Helvetica", 20))
        else:
            self.canvas.create_text(xcoord2, ycoord2, text=node2[5:],
                                    font=("Helvetica", 20))

        del node_dict[node1][node2]
        del node_dict[node2][node1]

    def set_start_node(self, node):
        xcoord = node_dict[node]["x"]
        ycoord = node_dict[node]["y"]

        self.canvas.create_oval(xcoord - 25, ycoord - 25, xcoord + 25, ycoord + 25, fill = "DarkGreen", outline= "DarkGreen")
        self.canvas.create_text(xcoord, ycoord, text= node[5:], font = ("Helvetica", 20))

        node_dict[node]["Start"] = True

    def set_end_node(self, node):
        xcoord = node_dict[node]["x"]
        ycoord = node_dict[node]["y"]

        self.canvas.create_oval(xcoord - 25, ycoord - 25, xcoord + 25, ycoord + 25, fill="black",
                                outline="black")
        self.canvas.create_text(xcoord, ycoord, text=node[5:], font=("Helvetica", 20), fill= "white")

        node_dict[node]["End"] = True

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