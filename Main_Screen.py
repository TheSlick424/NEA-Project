import tkinter as tk
from Canvas_Frame import CanvasFrame
from Generate_Random_Graph_Sidebar import GenerateRandomGraphSidebar
from Manual_Graph_Generation_Sidebar import ManualGraphSidebar
from A_Star_vs_Dijkstra import AStarVsDijkstra

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("A* Algorithm Solver")

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
        self.create_graph_menu.add_command(label= "Create Manual Graph", command= self.manual_graph_sidebar)
        self.create_graph_menu.add_command(label= "Create Random Graph", command= self.random_graph_sidebar)

        self.compare_graph_menu = tk.Menu(self.menu, tearoff= 0)
        self.menu.add_cascade(label= "Compare Algorithms", menu= self.compare_graph_menu)
        self.compare_graph_menu.add_command(label= "A* Algorithm vs Dijkstra's", command= self.a_star_vs_dijkstra)

    def manual_graph_sidebar(self):
        self.canvas.canvas.delete("all")
        self.generate_manual_graph_sidebar = ManualGraphSidebar(self, self.canvas)
        self.generate_manual_graph_sidebar.grid(row=0, column=1, sticky="nsew")


    def random_graph_sidebar(self):
        self.canvas.canvas.delete("all")
        self.generate_random_graph_sidebar = GenerateRandomGraphSidebar(self, self.canvas)
        self.generate_random_graph_sidebar.grid(row=0, column=1, sticky="nsew")

    def a_star_vs_dijkstra(self):
        self.canvas.canvas.delete("all")
        self.a_star_vs_dijkstra_menu = AStarVsDijkstra(self)
        self.a_star_vs_dijkstra_menu.grid(row= 0, column= 0, columnspan= 2, sticky= "nsew")