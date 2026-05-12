import tkinter as tk
from Canvas_Frame import CanvasFrame

class GenerateRandomGraphSidebar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg= "red4")

        self.canvas = CanvasFrame(self)

        self.label = tk.Label(self, text = "Enter Number of Nodes (0-500)", font= ("Helvetica", 20), bg= "red4",
                              fg= "white")
        self.label.place(relx= 0.5, rely= 0.3, anchor= "center")

        self.entry = tk.Entry(self, bg= "SteelBlue1", font= ("Helvetica", 20))
        self.entry.place(relx= 0.5, rely= 0.4, anchor= "center", height= 100, width= 200)

        self.button = tk.Button(self, text= "Generate Random Graph", bg= "DarkGreen", font= ("Helvetica", 15),
                                command= self.canvas.generate_random_graph)
        self.button.place(relx= 0.5, rely= 0.7, anchor= "center", height= 100, width= 300)