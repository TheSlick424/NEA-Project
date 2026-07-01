import tkinter as tk
from Dictionaries import node_dict, THE_path

class ManualGraphSidebar(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame
        self.parent = parent

        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=3)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid_propagate(False)

        self.label = tk.Label(self, text = "Generate Manual Graph", font= ("Helvetica", 20), bg= "red4", fg= "white")
        self.label.grid(row= 0, column= 0, columnspan= 2, sticky= "nsew")

        self.add_node_button = tk.Button(self, text= "Add Node", font= ("Helvetica", 20), bg= "DarkGreen",
                                         command= self.add_node)
        self.add_node_button.grid(row= 1, column= 0)

        self.remove_node_button = tk.Button(self, text= "Remove Node", font= ("Helvetica", 20), bg= "DarkRed",
                                            command= self.remove_node)
        self.remove_node_button.grid(row= 1, column= 1)

        self.add_edge_button = tk.Button(self, text= "Add Edge", font= ("Helvetica", 20), bg= "DarkGreen",
                                         command= self.add_edge)
        self.add_edge_button.grid(row= 2, column= 0)

        self.remove_edge_button = tk.Button(self, text= "Remove Edge", font= ("Helvetica", 20), bg= "DarkRed",
                                            command= self.remove_edge)
        self.remove_edge_button.grid(row= 2, column= 1)

        self.set_start_node_button = tk.Button(self, text= "Set Start Node", font= ("Helvetica", 20), bg= "gold2",
                                               command= self.set_start_node)
        self.set_start_node_button.grid(row= 3, column= 0)

        self.set_end_node_button = tk.Button(self, text= "Set End Node", font= ("Helvetica", 20), bg = "orange3",
                                             command= self.set_end_node)
        self.set_end_node_button.grid(row= 3, column= 1)

        self.listbox = tk.Listbox(self, font= ("Helvetica", 20), selectmode= "multiple")
        self.listbox.grid(row= 4, column= 0, columnspan= 2, sticky= "nsew",
                          padx = 50)

        self.run_algorithm_button = tk.Button(self, text= "Run Algorithm", font= ("Helvetica", 20), bg= "purple4",
                                              command= self.a_star_algorithm)
        self.run_algorithm_button.grid(row= 5, column= 0, columnspan= 2)

    def add_node(self):
        self.label['text'] = "Click To Add Node"
        self.parent.bind("<Button-1>", self.add_single_node)

    def add_single_node(self, event):
        self.canvas.add_node(event)
        self.parent.unbind("<Button-1>")
        self.listbox.insert("end", f"Node {self.canvas.node_count}")
        self.label['text'] = "Generate Manual Graph"

    def add_edge(self):
        self.edge = AddEdgeFrame(self, self.canvas)
        self.edge.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label['text'] = "Enter Node Numbers"

    def remove_node(self):
        self.removing_node = RemoveNodeFrame(self, self.canvas)
        self.removing_node.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label["text"] = "Select 1 Node In List To Remove"

    def remove_edge(self):
        self.removing_edge = RemoveEdgeFrame(self, self.canvas)
        self.removing_edge.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label["text"] = "Select 2 Nodes To Remove Edge"

    def set_start_node(self):
        self.setting_start_node = SetStartNodeFrame(self, self.canvas)
        self.setting_start_node.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label["text"] = "Select 1 Node To Set As Start"

    def set_end_node(self):
        self.setting_end_node = SetEndNodeFrame(self, self.canvas)
        self.setting_end_node.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label["text"] = "Select 1 Node To Set As End"

    def a_star_algorithm(self):
        THE_path = {}
        shortest_path = []
        start = None
        goal = None

        for node in node_dict:
            THE_path[node] = {"Path Distance": float("inf"),
                              "Heuristic": 0,
                              "Combined Distance": float("inf"),
                              "Previous Node": None}
            if node_dict[node]["Start"]:
                start = node
            elif node_dict[node]["End"]:
                goal = node

        THE_path[start]["Combined Distance"] = 0
        THE_path[start]["Path Distance"] = 0

        while node_dict:
            shortest = None

            for node in node_dict:
                if shortest is None:
                    shortest = node
                elif THE_path[node]["Combined Distance"] < THE_path[shortest]["Combined Distance"]:
                    shortest = node

            for neighbour, path_cost in node_dict[shortest].items():
                if neighbour in node_dict and THE_path[shortest]["Path Distance"] + node_dict[shortest][neighbour] < \
                        THE_path[neighbour]["Path Distance"]:
                    THE_path[neighbour]["Path Distance"] = THE_path[shortest]["Path Distance"] + node_dict[shortest][
                        neighbour]
                    THE_path[neighbour]["Combined Distance"] = THE_path[neighbour]["Path Distance"] + \
                                                               THE_path[neighbour]["Heuristic"]
                    THE_path[neighbour]["Previous Node"] = shortest

            node_dict.pop(shortest)

        current_node = goal
        while current_node is not start:
            shortest_path.insert(0, current_node)
            current_node = THE_path[current_node]["Previous Node"]

        shortest_path.insert(0, start)
        print(shortest_path)


class AddEdgeFrame(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label_node1 = tk.Label(self, text= "Node 1:", font= ("Helvetica", 20), bg= "red4")
        self.label_node1.grid(row=0, column=0)

        self.label_node2 = tk.Label(self, text= "Node 2:", font= ("Helvetica", 20), bg= "red4")
        self.label_node2.grid(row=1, column=0)

        self.label_weight = tk.Label(self, text= "Weight:", font= ("Helvetica", 20), bg= "red4")
        self.label_weight.grid(row=2, column=0)

        self.entry_node1 = tk.Entry(self, font= ("Helvetica", 20))
        self.entry_node1.grid(row=0, column=1)

        self.entry_node2 = tk.Entry(self, font= ("Helvetica", 20))
        self.entry_node2.grid(row=1, column=1)

        self.entry_weight = tk.Entry(self, font= ("Helvetica", 20))
        self.entry_weight.grid(row=2, column=1)

        self.add_edge_button = tk.Button(self, text= "Add Edge", font= ("Helvetica", 20), bg= "DarkGreen",
                                         command = self.add_edge)
        self.add_edge_button.grid(row=3, column= 0, columnspan= 2)

        self.label = parent.label

    def add_edge(self):
        self.canvas.add_edge(int(self.entry_node1.get()),
                             int(self.entry_node2.get()),
                             int(self.entry_weight.get()))
        self.label["text"] = "Generate Manual Graph"
        self.destroy()

class RemoveNodeFrame(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.button = tk.Button(self, text= "Remove Node", font= ("Helvetica", 20), bg = "red4",
                                command= self.remove_node)
        self.button.place(relx= 0.5, rely= 0.5, anchor= "center")

        self.listbox = parent.listbox
        self.label = parent.label

    def remove_node(self):
        if self.listbox.curselection():
            self.canvas.remove_node(self.listbox.get(self.listbox.curselection()))
            self.listbox.delete(self.listbox.curselection())
            self.label["text"] = "Generate Manual Graph"
            self.listbox.selection_clear(0, tk.END)
            self.destroy()
        else:
            self.label["text"] = "Generate Manual Graph"
            self.destroy()

class RemoveEdgeFrame(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.button = tk.Button(self, text = "Remove Edge", font= ("Helvetica", 20), bg = "red4",
                                command= self.remove_edge)
        self.button.place(relx= 0.5, rely= 0.5, anchor= "center")

        self.listbox = parent.listbox
        self.label = parent.label

    def remove_edge(self):
        if self.listbox.curselection():
            arr = []
            for value in self.listbox.curselection():
                arr.append(self.listbox.get(value))

            self.canvas.remove_edge(arr)
            self.label["text"] = "Generate Manual Graph"
            self.listbox.selection_clear(0, tk.END)
            self.destroy()
        else:
            self.label["text"] = "Generate Manual Graph"
            self.destroy()

class SetStartNodeFrame(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.set_start_node_button = tk.Button(self, text="Set Start Node", font=("Helvetica", 20), bg="gold2",
                                               command= self.set_start_node)
        self.set_start_node_button.place(relx= 0.5, rely= 0.5, anchor= "center")

        self.listbox = parent.listbox
        self.label = parent.label

    def set_start_node(self):
        if self.listbox.curselection():
            self.canvas.set_start_node(self.listbox.get(self.listbox.curselection()))
            self.label["text"] = "Generate Manual Graph"
            self.listbox.selection_clear(0, tk.END)
            self.destroy()
        else:
            self.label["text"] = "Generate Manual Graph"
            self.destroy()

class SetEndNodeFrame(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.set_end_node_button = tk.Button(self, text="Set End Node", font=("Helvetica", 20), bg="orange3",
                                             command= self.set_end_node)
        self.set_end_node_button.place(relx= 0.5, rely= 0.5, anchor= "center")

        self.listbox = parent.listbox
        self.label = parent.label

    def set_end_node(self):
        if self.listbox.curselection():
            self.canvas.set_end_node(self.listbox.get(self.listbox.curselection()))
            self.label["text"] = "Generate Manual Graph"
            self.listbox.selection_clear(0, tk.END)
            self.destroy()
        else:
            self.label["text"] = "Generate Manual Graph"
            self.destroy()