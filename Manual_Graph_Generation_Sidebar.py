import tkinter as tk

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

        self.remove_node_button = tk.Button(self, text= "Remove Node", font= ("Helvetica", 20), bg= "DarkRed")
        self.remove_node_button.grid(row= 1, column= 1)

        self.add_edge_button = tk.Button(self, text= "Add Edge", font= ("Helvetica", 20), bg= "DarkGreen",
                                         command= self.add_edge)
        self.add_edge_button.grid(row= 2, column= 0)

        self.remove_edge_button = tk.Button(self, text= "Remove Edge", font= ("Helvetica", 20), bg= "DarkRed")
        self.remove_edge_button.grid(row= 2, column= 1)

        self.set_start_node_button = tk.Button(self, text= "Set Start Node", font= ("Helvetica", 20), bg= "gold2")
        self.set_start_node_button.grid(row= 3, column= 0)

        self.set_end_node_button = tk.Button(self, text= "Set End Node", font= ("Helvetica", 20), bg = "orange3")
        self.set_end_node_button.grid(row= 3, column= 1)

        self.listbox = tk.Listbox(self, font= ("Helvetica", 20))
        self.listbox.grid(row= 4, column= 0, columnspan= 2, sticky= "nsew",
                          padx = 50)

        self.edit_button = tk.Button(self, text= "Edit", font= ("Helvetica", 20), bg= "RoyalBlue1")
        self.edit_button.grid(row= 5, column= 0)

        self.run_algorithm_button = tk.Button(self, text= "Run Algorithm", font= ("Helvetica", 20), bg= "purple4")
        self.run_algorithm_button.grid(row= 5, column= 1)

    def add_node(self):
        self.label['text'] = "Click To Add Node"
        self.parent.bind("<Button-1>", self.add_single_node)

    def add_single_node(self, event):
        self.canvas.add_node(event)
        self.parent.unbind("<Button-1>")
        self.listbox.insert("end", f"Node {self.canvas.node_count}")
        self.label['text'] = "Generate Manual Graph"

    def add_edge(self):
        self.edge = AddEdge(self, self.canvas)
        self.edge.grid(row= 1, column= 0, rowspan= 3, columnspan= 2, sticky= "nsew")
        self.label['text'] = "Enter Node Numbers"

class AddEdge(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label_node1 = tk.Label(self, text= "Node 1:", font= ("Helvetica", 20), bg= "red4")
        self.label_node1.grid(row=0, column=0)

        self.label_node2 = tk.Label(self, text= "Node 2:", font= ("Helvetica", 20), bg= "red4")
        self.label_node2.grid(row=1, column=0)

        self.entry_node1 = tk.Entry(self, font= ("Helvetica", 20))
        self.entry_node1.grid(row=0, column=1)

        self.entry_node2 = tk.Entry(self, font= ("Helvetica", 20))
        self.entry_node2.grid(row=1, column=1)