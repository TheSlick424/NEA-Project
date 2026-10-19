import tkinter as tk
from random import randint, choice
import math
from Dictionaries import node_dict, node_dict_copy

class CanvasFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg = "Midnight Blue")
        self.canvas.pack(fill= "both", expand = True)

        self.node_count = 0
        self.node_size = 0

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
                                      "End": False,
                                      "Heuristic": None,
                                      "Neighbours": {},
                                      "Checked": False}

        node_dict_copy[f"Node {self.node_count}"] = {"x": (xcoord1 + xcoord2) // 2,
                                      "y": (ycoord1 + ycoord2) // 2,
                                      "Start": False,
                                      "End": False,
                                      "Heuristic": None,
                                      "Neighbours": {},
                                      "Checked": False}

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
                del node_dict_copy[key][node]

        node_dict.pop(node)
        node_dict_copy.pop(node)

    def add_edge(self, node1, node2, weight):
        size = 10

        xcoord1 = node_dict[f"Node {node1}"]["x"]
        ycoord1 = node_dict[f"Node {node1}"]["y"]
        xcoord2 = node_dict[f"Node {node2}"]["x"]
        ycoord2 = node_dict[f"Node {node2}"]["y"]

        self.canvas.create_line(xcoord1, ycoord1, xcoord2, ycoord2, fill = "brown4", width = size)

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
            self.canvas.create_oval(xcoord1 - 25, ycoord1 - 25, xcoord1 + 25, ycoord1 + 25, fill= "red", outline= "red")
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
            self.canvas.create_oval(xcoord2 - 25, ycoord2 - 25, xcoord2 + 25, ycoord2 + 25, fill="red",
                                    outline="red")
            self.canvas.create_text(xcoord2, ycoord2, text=node2,
                                    font=("Helvetica", 20))

        node_dict[f"Node {node1}"]["Neighbours"][f"Node {node2}"] = weight
        node_dict[f"Node {node2}"]["Neighbours"][f"Node {node1}"] = weight
        node_dict_copy[f"Node {node1}"]["Neighbours"][f"Node {node2}"] = weight
        node_dict_copy[f"Node {node2}"]["Neighbours"][f"Node {node1}"] = weight

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

        del node_dict[node1]["Neighbours"][node2]
        del node_dict[node2]["Neighbours"][node1]
        del node_dict_copy[node1]["Neighbours"][node2]
        del node_dict_copy[node2]["Neighbours"][node1]

    def set_start_node(self, node):
        xcoord = node_dict[node]["x"]
        ycoord = node_dict[node]["y"]

        self.canvas.create_oval(xcoord - 25, ycoord - 25, xcoord + 25, ycoord + 25, fill = "DarkGreen", outline= "DarkGreen")
        self.canvas.create_text(xcoord, ycoord, text= node[5:], font = ("Helvetica", 20))

        node_dict[node]["Start"] = True
        node_dict_copy[node]["Start"] = True

    def set_end_node(self, node):
        xcoord = node_dict[node]["x"]
        ycoord = node_dict[node]["y"]

        self.canvas.create_oval(xcoord - 25, ycoord - 25, xcoord + 25, ycoord + 25, fill="black",
                                outline="black")
        self.canvas.create_text(xcoord, ycoord, text=node[5:], font=("Helvetica", 20), fill= "white")

        node_dict[node]["End"] = True
        node_dict_copy[node]["End"] = True

        for key in node_dict:
            node_dict[key]["Heuristic"] = math.ceil(math.sqrt(((node_dict[key]["x"] - node_dict[node]["x"])**2) + (node_dict[key]["y"] - node_dict[node]["y"]) **2))
            node_dict_copy[key]["Heuristic"] = math.ceil(math.sqrt(((node_dict_copy[key]["x"] - node_dict_copy[node]["x"]) ** 2) + (
                        node_dict_copy[key]["y"] - node_dict_copy[node]["y"]) ** 2))

    def new_shortest_node_visual(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - 25, y_coord - 25, x_coord + 25, y_coord + 25, fill= "gold",
                                outline= "gold")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", 20), fill= "black")

    def checked_shortest_node_visual(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - 25, y_coord - 25, x_coord + 25, y_coord + 25, fill= "gray50",
                                outline= "gray50")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", 20), fill= "black")

    def checking_path_visual(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gold", width = 10)
        self.canvas.create_oval(x_coord1 - 25, y_coord1 - 25, x_coord1 + 25, y_coord1 + 25, fill= "gold", outline= "gold")
        self.canvas.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", 20), fill= "black")

        if node_dict[node2]["End"]:
            self.canvas.create_oval(x_coord2 - 25, y_coord2 - 25, x_coord2 + 25, y_coord2 + 25, fill= "black", outline= "black")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", 20), fill= "white")
        else:
            self.canvas.create_oval(x_coord2 - 25, y_coord2 - 25, x_coord2 + 25, y_coord2 + 25, fill="red",
                                    outline="red")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", 20), fill="black")

    def checked_path_visual(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gray50", width = 10)
        self.canvas.create_oval(x_coord1 - 25, y_coord1 - 25, x_coord1 + 25, y_coord1 + 25, fill= "gold", outline= "gold")
        self.canvas.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", 20), fill= "black")

        if node_dict[node2]["End"]:
            self.canvas.create_oval(x_coord2 - 25, y_coord2 - 25, x_coord2 + 25, y_coord2 + 25, fill= "black", outline= "black")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", 20), fill= "white")
        else:
            self.canvas.create_oval(x_coord2 - 25, y_coord2 - 25, x_coord2 + 25, y_coord2 + 25, fill="red",
                                    outline="red")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", 20), fill="black")

    def final_path_start_visual(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - 25, y_coord - 25, x_coord + 25, y_coord + 25, fill= "forest green", outline= "forest green")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", 20), fill= "black")

    def final_path_visual(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "forest green", width = 10)
        self.canvas.create_oval(x_coord1 - 25, y_coord1 - 25, x_coord1 + 25, y_coord1 + 25, fill= "forest green", outline= "forest green")
        self.canvas.create_text(x_coord1, y_coord1, text=node1[5:], font= ("Helvetica", 20), fill= "black")
        self.canvas.create_oval(x_coord2 - 25, y_coord2 - 25, x_coord2 + 25, y_coord2 + 25, fill = "forest green", outline= "forest green")
        self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", 20), fill = "black")

    def generate_random_graph(self, nodes):
        node_dict.clear()
        node_dict_copy.clear()
        self.canvas.delete("all")
        num = math.ceil(math.sqrt(nodes))
        cols = 0
        rows = 0

        for i in range(num, 0, -1):
            if nodes % i == 0:
                cols = i
                rows = nodes // i
                break

        cell_height = self.canvas.winfo_height() // rows
        cell_width = self.canvas.winfo_width() // cols

        self.node_size = min(cell_height, cell_width) // 3

        node_count = 1
        x_end = randint((cols - 1) * cell_width + self.node_size, cols * cell_width - self.node_size)
        y_end = randint((rows - 1) * cell_height + self.node_size, rows * cell_height - self.node_size)

        for row in range(rows):
            for col in range(cols):
                if node_count > nodes:
                    break

                cell_x1 = col * cell_width
                cell_y1 = row * cell_height
                cell_x2 = cell_x1 + cell_width
                cell_y2 = cell_y1 + cell_height

                x = randint(cell_x1 + self.node_size, cell_x2 - self.node_size)
                y = randint(cell_y1 + self.node_size, cell_y2 - self.node_size)

                if node_count == 1:
                    self.canvas.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2, y + self.node_size / 2, fill = "green", outline= "green")
                    self.canvas.create_text(x, y, text= node_count, font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")
                    node_dict[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": True,
                                                       "End": False,
                                                       "Heuristic": ((x_end - x) ** 2 + (y_end - y) ** 2)**30,
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": True,
                                                            "End": False,
                                                            "Heuristic": ((x_end - x) ** 2 + (y_end - y) ** 2)**30,
                                                            "Neighbours": {},
                                                            "Checked": False}
                elif node_count == nodes:
                    x = x_end
                    y = y_end
                    self.canvas.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2, y + self.node_size / 2, fill = "black", outline= "black")
                    self.canvas.create_text(x, y, text= node_count, font= ("Helvetica", math.floor(self.node_size / 2)), fill= "white")
                    node_dict[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": False,
                                                       "End": True,
                                                       "Heuristic": 0,
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": False,
                                                            "End": True,
                                                            "Heuristic": 0,
                                                            "Neighbours": {},
                                                            "Checked": False}
                else:
                    self.canvas.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2, y + self.node_size / 2, fill = "red", outline= "red")
                    self.canvas.create_text(x, y, text=node_count, font=("Helvetica", math.floor(self.node_size / 2)), fill="black")
                    node_dict[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": False,
                                                       "End": False,
                                                       "Heuristic": ((x_end - x) ** 2 + (y_end - y) ** 2)**30,
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": False,
                                                            "End": False,
                                                            "Heuristic": ((x_end - x) ** 2 + (y_end - y) ** 2)**30,
                                                            "Neighbours": {},
                                                            "Checked": False}

                node_count += 1

        for node in node_dict:
            if nodes <= 10:
                edges = randint(1, 2)
            elif 11 < nodes < 300:
                edges = randint(1, 5)
            else:
                edges = randint(1, 7)

            close_nodes = [int(node[5:]) - 1, int(node[5:]) + 1, int(node[5:]) + cols, int(node[5:]) - cols, int(node[5:]) + cols - 1,
                           int(node[5:]) + cols + 1, int(node[5:]) - cols - 1, int(node[5:]) - cols + 1]

            for i in range(edges + 1):
                connected_node = choice(close_nodes)
                while int(connected_node) < 1 or int(connected_node) > nodes or connected_node in node_dict[node]["Neighbours"] \
                        or (node_dict[node]["row"] == node_dict[f"Node {connected_node}"]["row"] and max(int(node[5:]),
                                                                                                         int(connected_node)) - min(int(node[5:]), int(connected_node)) != 1)\
                        or (max(int(node_dict[node]["row"]), int(node_dict[f"Node {connected_node}"]["row"])) - min(int(node_dict[node]["row"]),
                                                                                                                    int(node_dict[f"Node {connected_node}"]["row"])) > 1)\
                        or (max(int(node_dict[node]["column"]), int(node_dict[f"Node {connected_node}"]["column"])) - min(int(node_dict[node]["column"]),
                                                                                                                          int(node_dict[f"Node {connected_node}"]["column"])) > 1):
                    connected_node = choice(close_nodes)

                weight = math.floor(((node_dict[node]["x"] - node_dict[f"Node {connected_node}"]["x"])**2 +
                                  (node_dict[node]["y"] - node_dict[f"Node {connected_node}"]["y"])**2)**(1/4))

                node_dict[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict_copy[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict[f"Node {connected_node}"]["Neighbours"][node] = weight
                node_dict_copy[f"Node {connected_node}"]["Neighbours"][node] = weight

                x_coord1 = node_dict[node]["x"]
                y_coord1 = node_dict[node]["y"]
                x_coord2 = node_dict[f"Node {connected_node}"]["x"]
                y_coord2 = node_dict[f"Node {connected_node}"]["y"]

                self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "brown4", width = self.node_size / 10)

                if node_dict[node]["Start"]:
                    self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill="DarkGreen", outline="green")
                    self.canvas.create_text(x_coord1, y_coord1, text=node[5:], font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="black")
                elif node_dict[node]["End"]:
                    self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill="black", outline="black")
                    self.canvas.create_text(x_coord1, y_coord1, text=node[5:], font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="white")
                else:
                    self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill="red", outline="red")
                    self.canvas.create_text(x_coord1, y_coord1, text=node[5:], font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="black")

                if node_dict[f"Node {connected_node}"]["Start"]:
                    self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill="DarkGreen", outline="green")
                    self.canvas.create_text(x_coord2, y_coord2, text=connected_node, font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="black")
                elif node_dict[f"Node {connected_node}"]["End"]:
                    self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill="black", outline="black")
                    self.canvas.create_text(x_coord2, y_coord2, text=connected_node, font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="white")
                else:
                    self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill="red", outline="red")
                    self.canvas.create_text(x_coord2, y_coord2, text=connected_node, font=("Helvetica", math.floor(self.node_size / 2)),
                                            fill="black")

    def new_shortest_node_visual_rand(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "gold",
                                outline= "gold")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")

    def checked_shortest_node_visual_rand(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "gray50",
                                outline= "gray50")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")

    def checking_path_visual_rand(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gold", width = self.node_size / 10)
        self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "gold", outline= "gold")
        self.canvas.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")

        if node_dict[node2]["End"]:
            self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill= "black", outline= "black")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "white")
        else:
            self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                    outline="red")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", math.floor(self.node_size / 2)), fill="black")

    def checked_path_visual_rand(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gray50", width = self.node_size / 10)
        self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "gold", outline= "gold")
        self.canvas.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")

        if node_dict[node2]["End"]:
            self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill= "black", outline= "black")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "white")
        else:
            self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                    outline="red")
            self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", math.floor(self.node_size / 2)), fill="black")

    def final_path_start_visual_rand(self, node):
        x_coord = node_dict[node]["x"]
        y_coord = node_dict[node]["y"]

        self.canvas.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "forest green", outline= "forest green")
        self.canvas.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")

    def final_path_visual_rand(self, node1, node2):
        x_coord1 = node_dict[node1]["x"]
        y_coord1 = node_dict[node1]["y"]
        x_coord2 = node_dict[node2]["x"]
        y_coord2 = node_dict[node2]["y"]

        self.canvas.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "forest green", width = self.node_size / 3)
        self.canvas.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "forest green", outline= "forest green")
        self.canvas.create_text(x_coord1, y_coord1, text=node1[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")
        self.canvas.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill = "forest green", outline= "forest green")
        self.canvas.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill = "black")