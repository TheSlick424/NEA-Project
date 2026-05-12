import tkinter as tk
from Canvas_Frame import CanvasFrame
from Generate_Random_Graph_Sidebar import GenerateRandomGraphSidebar

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("A* Algorithm Solver")
        self.geometry("1500x800")

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(False)

        self.canvas = CanvasFrame(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.menu = tk.Menu(self)
        self.config(menu= self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff= 0)
        self.menu.add_cascade(label="File", menu= self.file_menu)
        self.file_menu.add_command(label="Exit", command = self.destroy)

        self.create_graph_menu = tk.Menu(self.menu, tearoff= 0)
        self.menu.add_cascade(label= "Create Graph", menu= self.create_graph_menu)
        self.create_graph_menu.add_command(label= "Create Random Graph", command= self.random_graph_sidebar)

    def random_graph_sidebar(self):
        self.generate_random_graph_sidebar = GenerateRandomGraphSidebar(self)
        self.generate_random_graph_sidebar.grid(row=0, column=1, sticky="nsew")