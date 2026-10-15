import tkinter as tk

class GenerateRandomGraphSidebar(tk.Frame):
    def __init__(self, parent, canvas_frame):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame

        self.label = tk.Label(self, text = "Enter Number of Nodes (2-750)", font= ("Helvetica", 20), bg= "red4",
                              fg= "white")
        self.label.place(relx= 0.5, rely= 0.3, anchor= "center")

        self.entry = tk.Entry(self, bg= "SteelBlue1", font= ("Helvetica", 20))
        self.entry.place(relx= 0.5, rely= 0.4, anchor= "center", height= 100, width= 200)

        self.generate_graph_button = tk.Button(self, text= "Generate Random Graph", bg= "DarkGreen", font= ("Helvetica", 15),
                                command= self.generate_random_graph)
        self.generate_graph_button.place(relx= 0.5, rely= 0.6, anchor= "center", height= 100, width= 300)

        self.finalise_setup_button = tk.Button(self, text= "Finalise Setup", bg= "purple4", font= ("Helvetica", 20),
                                               command= self.finalise_setup)
        self.finalise_setup_button.place(relx= 0.5, rely= 0.9, anchor= "center", height= 100, width= 300)

    def generate_random_graph(self):
        nodes = int(self.entry.get())
        self.canvas.generate_random_graph(nodes)

    def finalise_setup(self):
        ...