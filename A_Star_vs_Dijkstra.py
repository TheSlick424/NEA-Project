import tkinter as tk
import math
from Dictionaries import node_dict, THE_path_a_star, THE_path_dijkstra, node_dict_copy, node_dict_a_star, node_dict_a_star_copy, node_dict_dijkstra, node_dict_dijkstra_copy
from random import choice, randint

class AStarVsDijkstra(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg= "red4")

        self.rowconfigure(0, weight= 6)
        self.rowconfigure(1, weight= 1)
        self.rowconfigure(2, weight= 1)
        self.columnconfigure(0, weight= 1)
        self.columnconfigure(1, weight= 1)
        self.grid_propagate(False)

        self.canvas_a_star = tk.Canvas(self, bg= "black")
        self.canvas_a_star.grid(row= 0, column= 0, sticky= "nsew")

        self.canvas_dijkstra = tk.Canvas(self, bg= "black")
        self.canvas_dijkstra.grid(row= 0, column= 1, sticky= "nsew")

        self.a_star_label = tk.Label(self, text= "A* Algorithm", font= ("Helvetica", 20), bg= "red4")
        self.a_star_label.grid(row= 1, column= 0)

        self.dijkstra_label = tk.Label(self, text= "Dijkstra's Algorithm", font= ("Helvetica", 20), bg= "red4")
        self.dijkstra_label.grid(row= 1, column= 1)

        self.generate_graph_button = tk.Button(self, text= "Generate Graphs", bg= "DarkGreen", font= ("Helvetica", 20),
                                               command= self.generate_graphs)
        self.generate_graph_button.grid(row= 2, column= 0)
        
        self.run_simulation_button = tk.Button(self, text= "Run Simulation", bg= "purple4", font= ("Helvetica", 20),
                                               command= self.run_simulation)
        self.run_simulation_button.grid(row= 2, column= 1)

    def generate_graphs(self):
        node_dict_a_star.clear()
        node_dict_a_star_copy.clear()
        node_dict_dijkstra.clear()
        node_dict_dijkstra_copy.clear()
        self.canvas_a_star.delete("all")
        self.canvas_dijkstra.delete("all")
        num = math.ceil(math.sqrt(1000))
        cols = 0
        rows = 0

        for i in range(num, 0, -1):
            if 1000 % i == 0:
                cols = i
                rows = 1000 // i
                break

        cell_height = self.canvas_a_star.winfo_height() // rows
        cell_width = self.canvas_a_star.winfo_width() // cols

        self.node_size = math.ceil(min(cell_height, cell_width) // 1.5)

        node_count = 1
        x_end = randint((cols - 1) * cell_width + self.node_size // 2, cols * cell_width - self.node_size // 2)
        y_end = randint((rows - 1) * cell_height + self.node_size // 2, rows * cell_height - self.node_size // 2)

        for row in range(rows):
            for col in range(cols):
                if node_count > 1000:
                    break

                cell_x1 = col * cell_width
                cell_y1 = row * cell_height
                cell_x2 = cell_x1 + cell_width
                cell_y2 = cell_y1 + cell_height

                x = randint(cell_x1 + self.node_size // 2, cell_x2 - self.node_size // 2)
                y = randint(cell_y1 + self.node_size // 2, cell_y2 - self.node_size // 2)

                if node_count == 1:
                    self.canvas_a_star.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2,
                                            y + self.node_size / 2, fill="green", outline="green")
                    self.canvas_dijkstra.create_oval(x - self.node_size / 2, y - self.node_size / 2,
                                                   x + self.node_size / 2,
                                                   y + self.node_size / 2, fill="green", outline="green")
                    self.canvas_a_star.create_text(x, y, text=node_count, font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x, y, text=node_count,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")
                    node_dict_a_star[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": True,
                                                       "End": False,
                                                       "Heuristic": math.ceil(
                                                           math.sqrt((x_end - x) ** 2 + (y_end - y) ** 2)),
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_a_star_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": True,
                                                            "End": False,
                                                            "Heuristic": math.ceil(
                                                                math.sqrt((x_end - x) ** 2 + (y_end - y) ** 2)),
                                                            "Neighbours": {},
                                                            "Checked": False}
                    node_dict_dijkstra[f"Node {node_count}"] = {"x": x,
                                                              "y": y,
                                                              "row": row,
                                                              "column": col,
                                                              "Start": True,
                                                              "End": False,
                                                              "Heuristic": 0,
                                                              "Neighbours": {},
                                                              "Checked": False}

                    node_dict_dijkstra_copy[f"Node {node_count}"] = {"x": x,
                                                                   "y": y,
                                                                   "row": row,
                                                                   "column": col,
                                                                   "Start": True,
                                                                   "End": False,
                                                                   "Heuristic": 0,
                                                                   "Neighbours": {},
                                                                   "Checked": False}
                elif node_count == 1000:
                    x = x_end
                    y = y_end
                    self.canvas_a_star.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2,
                                            y + self.node_size / 2, fill="black", outline="black")
                    self.canvas_dijkstra.create_oval(x - self.node_size / 2, y - self.node_size / 2,
                                                   x + self.node_size / 2,
                                                   y + self.node_size / 2, fill="black", outline="black")
                    self.canvas_a_star.create_text(x, y, text=node_count, font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="white")
                    self.canvas_dijkstra.create_text(x, y, text=node_count,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="white")
                    node_dict_a_star[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": False,
                                                       "End": True,
                                                       "Heuristic": 0,
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_a_star_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": False,
                                                            "End": True,
                                                            "Heuristic": 0,
                                                            "Neighbours": {},
                                                            "Checked": False}
                    node_dict_dijkstra[f"Node {node_count}"] = {"x": x,
                                                              "y": y,
                                                              "row": row,
                                                              "column": col,
                                                              "Start": False,
                                                              "End": True,
                                                              "Heuristic": 0,
                                                              "Neighbours": {},
                                                              "Checked": False}

                    node_dict_dijkstra_copy[f"Node {node_count}"] = {"x": x,
                                                                   "y": y,
                                                                   "row": row,
                                                                   "column": col,
                                                                   "Start": False,
                                                                   "End": True,
                                                                   "Heuristic": 0,
                                                                   "Neighbours": {},
                                                                   "Checked": False}
                else:
                    self.canvas_a_star.create_oval(x - self.node_size / 2, y - self.node_size / 2, x + self.node_size / 2,
                                            y + self.node_size / 2, fill="red", outline="red")
                    self.canvas_dijkstra.create_oval(x - self.node_size / 2, y - self.node_size / 2,
                                                   x + self.node_size / 2,
                                                   y + self.node_size / 2, fill="red", outline="red")
                    self.canvas_a_star.create_text(x, y, text=node_count, font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x, y, text=node_count,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")
                    node_dict_a_star[f"Node {node_count}"] = {"x": x,
                                                       "y": y,
                                                       "row": row,
                                                       "column": col,
                                                       "Start": False,
                                                       "End": False,
                                                       "Heuristic": math.ceil(
                                                           math.sqrt((x_end - x) ** 2 + (y_end - y) ** 2)),
                                                       "Neighbours": {},
                                                       "Checked": False}

                    node_dict_a_star_copy[f"Node {node_count}"] = {"x": x,
                                                            "y": y,
                                                            "row": row,
                                                            "column": col,
                                                            "Start": False,
                                                            "End": False,
                                                            "Heuristic": math.ceil(
                                                                math.sqrt((x_end - x) ** 2 + (y_end - y) ** 2)),
                                                            "Neighbours": {},
                                                            "Checked": False}
                    node_dict_dijkstra[f"Node {node_count}"] = {"x": x,
                                                              "y": y,
                                                              "row": row,
                                                              "column": col,
                                                              "Start": False,
                                                              "End": False,
                                                              "Heuristic": 0,
                                                              "Neighbours": {},
                                                              "Checked": False}

                    node_dict_dijkstra_copy[f"Node {node_count}"] = {"x": x,
                                                                   "y": y,
                                                                   "row": row,
                                                                   "column": col,
                                                                   "Start": False,
                                                                   "End": False,
                                                                   "Heuristic": 0,
                                                                   "Neighbours": {},
                                                                   "Checked": False}

                node_count += 1

        for node in node_dict_a_star:
            if node_dict_a_star[node]["Heuristic"] >= (5 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2):
                red = 200
                green = 100
                blue = 100
                interpolation = ((node_dict_a_star[node]["Heuristic"] - (5 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                green += (100 - round(interpolation * 100))
            elif (4 / 6) * math.sqrt(self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2) <= \
                    node_dict_a_star[node]["Heuristic"] < (5 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2):
                red = 200
                green = 200
                blue = 100
                interpolation = ((node_dict_a_star[node]["Heuristic"] - (4 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                red -= (100 - round(interpolation * 100))
            elif (3 / 6) * math.sqrt(self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2) <= \
                    node_dict_a_star[node]["Heuristic"] < (4 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2):
                red = 100
                green = 200
                blue = 100
                interpolation = ((node_dict_a_star[node]["Heuristic"] - (3 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                blue += (100 - round(interpolation * 100))
            elif (2 / 6) * math.sqrt(self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2) <= \
                    node_dict_a_star[node]["Heuristic"] < (3 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2):
                red = 100
                green = 200
                blue = 200
                interpolation = ((node_dict_a_star[node]["Heuristic"] - (2 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                green -= (100 - round(interpolation * 100))
            elif (1 / 6) * math.sqrt(self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2) <= \
                    node_dict_a_star[node]["Heuristic"] < (2 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2):
                red = 100
                green = 100
                blue = 200
                interpolation = ((node_dict_a_star[node]["Heuristic"] - (1 / 6) * math.sqrt(
                    self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                red += (100 - round(interpolation * 100))
            else:
                red = 200
                green = 100
                blue = 200
                interpolation = ((node_dict_a_star[node]["Heuristic"]) /
                                 ((1 / 6) * math.sqrt(
                                     self.canvas_a_star.winfo_width() ** 2 + self.canvas_a_star.winfo_height() ** 2)))
                blue -= (100 - round(interpolation * 100))

            colour = "#" + str(hex(red).split("x")[-1]) + str(hex(green).split("x")[-1]) + str(hex(blue).split("x")[-1])

            edges = randint(1, 7)

            close_nodes = [int(node[5:]) - 1, int(node[5:]) + 1, int(node[5:]) + cols, int(node[5:]) - cols,
                           int(node[5:]) + cols - 1,
                           int(node[5:]) + cols + 1, int(node[5:]) - cols - 1, int(node[5:]) - cols + 1]

            for i in range(edges + 1):
                connected_node = choice(close_nodes)
                while int(connected_node) < 1 or int(connected_node) > 1000 or connected_node in node_dict_a_star[node][
                    "Neighbours"] \
                        or (node_dict_a_star[node]["row"] == node_dict_a_star[f"Node {connected_node}"]["row"] and max(int(node[5:]),
                                                                                                         int(connected_node)) - min(
                    int(node[5:]), int(connected_node)) != 1) \
                        or (max(int(node_dict_a_star[node]["row"]), int(node_dict_a_star[f"Node {connected_node}"]["row"])) - min(
                    int(node_dict_a_star[node]["row"]),
                    int(node_dict_a_star[f"Node {connected_node}"]["row"])) > 1) \
                        or (
                        max(int(node_dict_a_star[node]["column"]), int(node_dict_a_star[f"Node {connected_node}"]["column"])) - min(
                    int(node_dict_a_star[node]["column"]),
                    int(node_dict_a_star[f"Node {connected_node}"]["column"])) > 1):
                    connected_node = choice(close_nodes)

                weight = math.ceil(math.sqrt((node_dict_a_star[node]["x"] - node_dict_a_star_copy[f"Node {connected_node}"]["x"]) ** 2 +
                                             (node_dict_a_star[node]["y"] - node_dict_a_star_copy[f"Node {connected_node}"]["y"]) ** 2))

                node_dict_a_star[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict_a_star_copy[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict_dijkstra[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict_dijkstra_copy[node]["Neighbours"][f"Node {connected_node}"] = weight
                node_dict_a_star[f"Node {connected_node}"]["Neighbours"][node] = weight
                node_dict_a_star_copy[f"Node {connected_node}"]["Neighbours"][node] = weight
                node_dict_dijkstra[f"Node {connected_node}"]["Neighbours"][node] = weight
                node_dict_dijkstra_copy[f"Node {connected_node}"]["Neighbours"][node] = weight

                x_coord1 = node_dict_a_star[node]["x"]
                y_coord1 = node_dict_a_star[node]["y"]
                x_coord2 = node_dict_a_star[f"Node {connected_node}"]["x"]
                y_coord2 = node_dict_a_star[f"Node {connected_node}"]["y"]

                self.canvas_a_star.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill="gray50",
                                        width=self.node_size / 20)
                self.canvas_dijkstra.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill="gray50",
                                               width=self.node_size / 20)

                if node_dict_a_star[node]["Start"]:
                    self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                            x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill="DarkGreen", outline="green")
                    self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                                   x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                                   fill="DarkGreen", outline="green")
                    self.canvas_a_star.create_text(x_coord1, y_coord1, text=node[5:],
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node[5:],
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")
                elif node_dict_a_star[node]["End"]:
                    self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                            x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill="purple4", outline="purple4")
                    self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                                   x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                                   fill="purple4", outline="purple4")
                    self.canvas_a_star.create_text(x_coord1, y_coord1, text=node[5:],
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="white")
                    self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node[5:],
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="white")
                else:
                    self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                            x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                            fill=colour, outline=colour)
                    self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                                   x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                                   fill=colour, outline=colour)
                    self.canvas_a_star.create_text(x_coord1, y_coord1, text=node[5:],
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node[5:],
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")

                if node_dict_a_star[f"Node {connected_node}"]["Start"]:
                    self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                            x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill="DarkGreen", outline="green")
                    self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                                   x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                                   fill="DarkGreen", outline="green")
                    self.canvas_a_star.create_text(x_coord2, y_coord2, text=connected_node,
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=connected_node,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")
                elif node_dict_a_star[f"Node {connected_node}"]["End"]:
                    self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                            x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill="purple4", outline="purple4")
                    self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                                   x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                                   fill="purple4", outline="purple4")
                    self.canvas_a_star.create_text(x_coord2, y_coord2, text=connected_node,
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="white")
                    self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=connected_node,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="white")
                else:
                    self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                            x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                            fill=colour, outline=colour)
                    self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                                   x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                                   fill=colour, outline=colour)
                    self.canvas_a_star.create_text(x_coord2, y_coord2, text=connected_node,
                                            font=("Helvetica", math.floor(self.node_size / 2.5)),
                                            fill="black")
                    self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=connected_node,
                                                   font=("Helvetica", math.floor(self.node_size / 2.5)),
                                                   fill="black")
    
    def run_simulation(self):
        shortest_path_a_star = []
        visuals_a_star = []
        start_a_star = None
        goal_a_star = None
        step_count_a_star = 0
        iteration_count_a_star = 1

        for node in node_dict_a_star_copy:
            THE_path_a_star[node] = {"Path Distance": float("inf"),
                              "Heuristic": node_dict_a_star[node]["Heuristic"],
                              "Combined Distance": float("inf"),
                              "Previous Node": None}
            if node_dict_a_star_copy[node]["Start"]:
                start_a_star = node
            elif node_dict_a_star_copy[node]["End"]:
                goal_a_star = node

        step_count_a_star += 1

        THE_path_a_star[start_a_star]["Combined Distance"] = 0
        THE_path_a_star[start_a_star]["Path Distance"] = 0

        while node_dict_a_star_copy:
            shortest_a_star = None
            step_count_a_star += 1
            for node in node_dict_a_star_copy:
                if shortest_a_star is None:
                    shortest_a_star = node
                elif THE_path_a_star[node]["Combined Distance"] < THE_path_a_star[shortest_a_star]["Combined Distance"]:
                    shortest_a_star = node

            visuals_a_star.append(["New shortest node", shortest_a_star])

            if node_dict_a_star[shortest_a_star]["End"]:
                break

            for neighbour, path_cost in node_dict_a_star_copy[shortest_a_star]["Neighbours"].items():
                if neighbour == THE_path_a_star[shortest_a_star]["Previous Node"] or node_dict_a_star[neighbour]["Checked"]:
                    continue

                step_count_a_star += 1
                visuals_a_star.append(["Checking path", shortest_a_star, neighbour])

                if neighbour in node_dict_a_star_copy and THE_path_a_star[shortest_a_star]["Path Distance"] + \
                        node_dict_a_star_copy[shortest_a_star]["Neighbours"][
                            neighbour] < \
                        THE_path_a_star[neighbour]["Path Distance"]:
                    step_count_a_star += 1

                    THE_path_a_star[neighbour]["Path Distance"] = THE_path_a_star[shortest_a_star]["Path Distance"] + \
                                                           node_dict_a_star_copy[shortest_a_star]["Neighbours"][neighbour]
                    THE_path_a_star[neighbour]["Combined Distance"] = THE_path_a_star[neighbour]["Path Distance"] + \
                                                               THE_path_a_star[neighbour]["Heuristic"]
                    THE_path_a_star[neighbour]["Previous Node"] = shortest_a_star

                    step_count_a_star += 3
                step_count_a_star += 1
                visuals_a_star.append(["Checked path", shortest_a_star, neighbour])
                node_dict_a_star[shortest_a_star]["Checked"] = True

            node_dict_a_star_copy.pop(shortest_a_star)
            step_count_a_star += 1
            visuals_a_star.append(["Checked shortest node", shortest_a_star])
            iteration_count_a_star += 1

        step_count_a_star += 1

        current_node = goal_a_star
        while current_node is not start_a_star:
            shortest_path_a_star.insert(0, current_node)
            current_node = THE_path_a_star[current_node]["Previous Node"]

        shortest_path_a_star.insert(0, start_a_star)

        for i in range(len(shortest_path_a_star) - 1):
            if i == 0:
                visuals_a_star.append(["Final path start", shortest_path_a_star[i]])
            else:
                visuals_a_star.append(["Final path", shortest_path_a_star[i], shortest_path_a_star[i - 1]])
        visuals_a_star.append(["Final path", shortest_path_a_star[len(shortest_path_a_star) - 1], shortest_path_a_star[len(shortest_path_a_star) - 2]])

        shortest_path_dijkstra = []
        visuals_dijkstra = []
        start_dijkstra = None
        goal_dijkstra = None
        step_count_dijkstra = 0
        iteration_count_dijkstra = 1

        for node in node_dict_dijkstra_copy:
            THE_path_dijkstra[node] = {"Path Distance": float("inf"),
                                     "Heuristic": node_dict_dijkstra[node]["Heuristic"],
                                     "Combined Distance": float("inf"),
                                     "Previous Node": None}
            if node_dict_dijkstra_copy[node]["Start"]:
                start_dijkstra = node
            elif node_dict_dijkstra_copy[node]["End"]:
                goal_dijkstra = node

        step_count_dijkstra += 1

        THE_path_dijkstra[start_dijkstra]["Combined Distance"] = 0
        THE_path_dijkstra[start_dijkstra]["Path Distance"] = 0

        while node_dict_dijkstra_copy:
            shortest_dijkstra = None
            step_count_dijkstra += 1
            for node in node_dict_dijkstra_copy:
                if shortest_dijkstra is None:
                    shortest_dijkstra = node
                elif THE_path_dijkstra[node]["Combined Distance"] < THE_path_dijkstra[shortest_dijkstra]["Combined Distance"]:
                    shortest_dijkstra = node

            visuals_dijkstra.append(["New shortest node", shortest_dijkstra])

            if node_dict_dijkstra[shortest_dijkstra]["End"]:
                break

            for neighbour, path_cost in node_dict_dijkstra_copy[shortest_dijkstra]["Neighbours"].items():
                if neighbour == THE_path_dijkstra[shortest_dijkstra]["Previous Node"] or node_dict_dijkstra[neighbour][
                    "Checked"]:
                    continue

                step_count_dijkstra += 1
                visuals_dijkstra.append(["Checking path", shortest_dijkstra, neighbour])

                if neighbour in node_dict_dijkstra_copy and THE_path_dijkstra[shortest_dijkstra]["Path Distance"] + \
                        node_dict_dijkstra_copy[shortest_dijkstra]["Neighbours"][
                            neighbour] < \
                        THE_path_dijkstra[neighbour]["Path Distance"]:
                    step_count_dijkstra += 1

                    THE_path_dijkstra[neighbour]["Path Distance"] = THE_path_dijkstra[shortest_dijkstra]["Path Distance"] + \
                                                                  node_dict_dijkstra_copy[shortest_dijkstra]["Neighbours"][
                                                                      neighbour]
                    THE_path_dijkstra[neighbour]["Combined Distance"] = THE_path_dijkstra[neighbour]["Path Distance"] + \
                                                                      THE_path_dijkstra[neighbour]["Heuristic"]
                    THE_path_dijkstra[neighbour]["Previous Node"] = shortest_dijkstra

                    step_count_dijkstra += 3
                step_count_dijkstra += 1
                visuals_dijkstra.append(["Checked path", shortest_dijkstra, neighbour])
                node_dict_dijkstra[shortest_dijkstra]["Checked"] = True

            node_dict_dijkstra_copy.pop(shortest_dijkstra)
            step_count_dijkstra += 1
            visuals_dijkstra.append(["Checked shortest node", shortest_dijkstra])
            iteration_count_dijkstra += 1

        step_count_dijkstra += 1

        current_node = goal_dijkstra
        while current_node is not start_dijkstra:
            shortest_path_dijkstra.insert(0, current_node)
            current_node = THE_path_dijkstra[current_node]["Previous Node"]

        shortest_path_dijkstra.insert(0, start_dijkstra)

        for i in range(len(shortest_path_dijkstra) - 1):
            if i == 0:
                visuals_dijkstra.append(["Final path start", shortest_path_dijkstra[i]])
            else:
                visuals_dijkstra.append(["Final path", shortest_path_dijkstra[i], shortest_path_dijkstra[i - 1]])
        visuals_dijkstra.append(["Final path", shortest_path_dijkstra[len(shortest_path_dijkstra) - 1],
                               shortest_path_dijkstra[len(shortest_path_dijkstra) - 2]])
        self.index = 0
        self.run_visuals(visuals_a_star, visuals_dijkstra, self.index)
    
    def run_visuals(self, visuals_a_star, visuals_dijkstra, index):
        if index < len(visuals_a_star):
            if visuals_a_star[index] is not None:
                if visuals_a_star[index][0] == "New shortest node":
                    self.new_shortest_node_visual(visuals_a_star[index][1], "A*")
                elif visuals_a_star[index][0] == "Checking path":
                    self.checking_path_visual(visuals_a_star[index][1], visuals_a_star[index][2], "A*")
                elif visuals_a_star[index][0] == "Checked shortest node":
                    self.checked_shortest_node_visual(visuals_a_star[index][1], "A*")
                elif visuals_a_star[index][0] == "Checked path":
                    self.checked_path_visual(visuals_a_star[index][1], visuals_a_star[index][2], "A*")
                elif visuals_a_star[index][0] == "Final path start":
                    self.final_path_start_visual(visuals_a_star[index][1], "A*")
                elif visuals_a_star[index][0] == "Final path":
                    self.final_path_visual(visuals_a_star[index][1], visuals_a_star[index][2], "A*")
        
        if index < len(visuals_dijkstra):
            if visuals_dijkstra[index] is not None:
                if visuals_dijkstra[index][0] == "New shortest node":
                    self.new_shortest_node_visual(visuals_dijkstra[index][1], "Dijkstra")
                elif visuals_dijkstra[index][0] == "Checking path":
                    self.checking_path_visual(visuals_dijkstra[index][1], visuals_dijkstra[index][2], "Dijkstra")
                elif visuals_dijkstra[index][0] == "Checked shortest node":
                    self.checked_shortest_node_visual(visuals_dijkstra[index][1], "Dijkstra")
                elif visuals_dijkstra[index][0] == "Checked path":
                    self.checked_path_visual(visuals_dijkstra[index][1], visuals_dijkstra[index][2], "Dijkstra")
                elif visuals_dijkstra[index][0] == "Final path start":
                    self.final_path_start_visual(visuals_dijkstra[index][1], "Dijkstra")
                elif visuals_dijkstra[index][0] == "Final path":
                    self.final_path_visual(visuals_dijkstra[index][1], visuals_dijkstra[index][2], "Dijkstra")

        self.index += 1
        self.after(1, lambda: self.run_visuals(visuals_a_star, visuals_dijkstra, self.index))
            
    def new_shortest_node_visual(self, node, canvas):
        if canvas == "A*":
            x_coord = node_dict_a_star[node]["x"]
            y_coord = node_dict_a_star[node]["y"]
    
            self.canvas_a_star.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "gold",
                                    outline= "gold")
            self.canvas_a_star.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "black")
        else:
            x_coord = node_dict_dijkstra[node]["x"]
            y_coord = node_dict_dijkstra[node]["y"]

            self.canvas_dijkstra.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2,
                                           x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill="gold",
                                           outline="gold")
            self.canvas_dijkstra.create_text(x_coord, y_coord, text=node[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")

    def checked_shortest_node_visual(self, node, canvas):
        if canvas == "A*":
            x_coord = node_dict_a_star[node]["x"]
            y_coord = node_dict_a_star[node]["y"]
    
            self.canvas_a_star.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "gray50",
                                    outline= "gray50")
            self.canvas_a_star.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "black")
        else:
            x_coord = node_dict_dijkstra[node]["x"]
            y_coord = node_dict_dijkstra[node]["y"]

            self.canvas_dijkstra.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2,
                                           x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill="gray50",
                                           outline="gray50")
            self.canvas_dijkstra.create_text(x_coord, y_coord, text=node[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")

    def checking_path_visual(self, node1, node2, canvas):
        if canvas == "A*":
            x_coord1 = node_dict_a_star[node1]["x"]
            y_coord1 = node_dict_a_star[node1]["y"]
            x_coord2 = node_dict_a_star[node2]["x"]
            y_coord2 = node_dict_a_star[node2]["y"]
    
            self.canvas_a_star.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gold", width = self.node_size / 8)
            self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "gold", outline= "gold")
            self.canvas_a_star.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "black")
    
            if node_dict_a_star[node2]["End"]:
                self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill= "black", outline= "black")
                self.canvas_a_star.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "white")
            else:
                self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                        outline="red")
                self.canvas_a_star.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")
        else:
            x_coord1 = node_dict_dijkstra[node1]["x"]
            y_coord1 = node_dict_dijkstra[node1]["y"]
            x_coord2 = node_dict_dijkstra[node2]["x"]
            y_coord2 = node_dict_dijkstra[node2]["y"]

            self.canvas_dijkstra.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill="gold",
                                           width=self.node_size / 8)
            self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                           x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill="gold",
                                           outline="gold")
            self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node1[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")

            if node_dict_dijkstra[node2]["End"]:
                self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                               x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                               fill="black", outline="black")
                self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=node2[5:],
                                               font=("Helvetica", math.floor(self.node_size / 2.5)), fill="white")
            else:
                self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                               x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                               outline="red")
                self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=node2[5:],
                                               font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")
            

    def checked_path_visual(self, node1, node2, canvas):
        if canvas == "A*":
            x_coord1 = node_dict_a_star[node1]["x"]
            y_coord1 = node_dict_a_star[node1]["y"]
            x_coord2 = node_dict_a_star[node2]["x"]
            y_coord2 = node_dict_a_star[node2]["y"]
    
            self.canvas_a_star.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "gray50", width = self.node_size / 8)
            self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "gold", outline= "gold")
            self.canvas_a_star.create_text(x_coord1, y_coord1, text= node1[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "black")
    
            if node_dict_a_star[node2]["End"]:
                self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill= "black", outline= "black")
                self.canvas_a_star.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "white")
            else:
                self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                        outline="red")
                self.canvas_a_star.create_text(x_coord2, y_coord2, text=node2[5:], font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")
        else:
            x_coord1 = node_dict_dijkstra[node1]["x"]
            y_coord1 = node_dict_dijkstra[node1]["y"]
            x_coord2 = node_dict_dijkstra[node2]["x"]
            y_coord2 = node_dict_dijkstra[node2]["y"]

            self.canvas_dijkstra.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill="gray50",
                                           width=self.node_size / 8)
            self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                           x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill="gold",
                                           outline="gold")
            self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node1[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")

            if node_dict_dijkstra[node2]["End"]:
                self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                               x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                               fill="black", outline="black")
                self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=node2[5:],
                                               font=("Helvetica", math.floor(self.node_size / 2.5)), fill="white")
            else:
                self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                               x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill="red",
                                               outline="red")
                self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=node2[5:],
                                               font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")

    def final_path_start_visual(self, node, canvas):
        if canvas == "A*":
            x_coord = node_dict_a_star[node]["x"]
            y_coord = node_dict_a_star[node]["y"]

            self.canvas_a_star.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2, x_coord + self.node_size / 2, y_coord + self.node_size / 2, fill= "forest green", outline= "forest green")
            self.canvas_a_star.create_text(x_coord, y_coord, text= node[5:], font= ("Helvetica", math.floor(self.node_size / 2)), fill= "black")
        else:
            x_coord = node_dict_dijkstra[node]["x"]
            y_coord = node_dict_dijkstra[node]["y"]

            self.canvas_dijkstra.create_oval(x_coord - self.node_size / 2, y_coord - self.node_size / 2,
                                           x_coord + self.node_size / 2, y_coord + self.node_size / 2,
                                           fill="forest green", outline="forest green")
            self.canvas_dijkstra.create_text(x_coord, y_coord, text=node[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2)), fill="black")

    def final_path_visual(self, node1, node2, canvas):
        if canvas == "A*":
            x_coord1 = node_dict_a_star[node1]["x"]
            y_coord1 = node_dict_a_star[node1]["y"]
            x_coord2 = node_dict_a_star[node2]["x"]
            y_coord2 = node_dict_a_star[node2]["y"]

            self.canvas_a_star.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill= "forest green", width = self.node_size / 2)
            self.canvas_a_star.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2, x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2, fill= "forest green", outline= "forest green")
            self.canvas_a_star.create_text(x_coord1, y_coord1, text=node1[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill= "black")
            self.canvas_a_star.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2, x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2, fill = "forest green", outline= "forest green")
            self.canvas_a_star.create_text(x_coord2, y_coord2, text=node2[5:], font= ("Helvetica", math.floor(self.node_size / 2.5)), fill = "black")
        else:
            x_coord1 = node_dict_dijkstra[node1]["x"]
            y_coord1 = node_dict_dijkstra[node1]["y"]
            x_coord2 = node_dict_dijkstra[node2]["x"]
            y_coord2 = node_dict_dijkstra[node2]["y"]

            self.canvas_dijkstra.create_line(x_coord1, y_coord1, x_coord2, y_coord2, fill="forest green",
                                           width=self.node_size / 2)
            self.canvas_dijkstra.create_oval(x_coord1 - self.node_size / 2, y_coord1 - self.node_size / 2,
                                           x_coord1 + self.node_size / 2, y_coord1 + self.node_size / 2,
                                           fill="forest green", outline="forest green")
            self.canvas_dijkstra.create_text(x_coord1, y_coord1, text=node1[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")
            self.canvas_dijkstra.create_oval(x_coord2 - self.node_size / 2, y_coord2 - self.node_size / 2,
                                           x_coord2 + self.node_size / 2, y_coord2 + self.node_size / 2,
                                           fill="forest green", outline="forest green")
            self.canvas_dijkstra.create_text(x_coord2, y_coord2, text=node2[5:],
                                           font=("Helvetica", math.floor(self.node_size / 2.5)), fill="black")