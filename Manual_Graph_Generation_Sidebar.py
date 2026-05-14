import tkinter as tk

class ManualGraphSidebar(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=3)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid_propagate(False)

        self.label = tk.Label(self, text = "Generate Manual Graph", font= ("Helvetica", 20), bg= "red4", fg= "white")
        self.label.grid(row= 0, column= 0, columnspan= 2, sticky= "nsew")

        self.add_node_button = tk.Button(self, text= "Add Node", font= ("Helvetica", 20), bg= "DarkGreen")
        self.add_node_button.grid(row= 1, column= 0)

        self.remove_node_button = tk.Button(self, text= "Remove Node", font= ("Helvetica", 20), bg= "DarkRed")
        self.remove_node_button.grid(row= 1, column= 1)

        self.add_edge_button = tk.Button(self, text= "Add Edge", font= ("Helvetica", 20), bg= "DarkGreen")
        self.add_edge_button.grid(row= 2, column= 0)

        self.remove_edge_button = tk.Button(self, text= "Remove Edge", font= ("Helvetica", 20), bg= "DarkRed")
        self.remove_edge_button.grid(row= 2, column= 1)

        self.listbox = tk.Listbox(self, font= ("Helvetica", 10))
        self.listbox.grid(row= 3, column= 0, columnspan= 2, sticky= "nsew",
                          padx = 50)

        self.edit_button = tk.Button(self, text= "Edit", font= ("Helvetica", 20), bg= "RoyalBlue1")
        self.edit_button.grid(row= 4, column= 0)

        self.run_algorithm_button = tk.Button(self, text= "Run Algorithm", font= ("Helvetica", 20), bg= "purple4")
        self.run_algorithm_button.grid(row= 4, column= 1)