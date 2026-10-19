import tkinter as tk

from Dictionaries import node_dict, node_dict_copy, THE_path

class GenerateRandomGraphSidebar(tk.Frame):
    def __init__(self, parent, canvas_frame, size = 0):
        super().__init__(parent, bg= "red4")

        self.canvas = canvas_frame
        self.rowconfigure(0, weight = 5)
        self.rowconfigure(1, weight= 5)
        self.rowconfigure(2, weight= 2)
        self.rowconfigure(3, weight= 2)
        self.columnconfigure(0, weight= 1)
        self.grid_propagate(False)

        self.size = size

        self.label = tk.Label(self, text = "Enter Number of Nodes (2-1000)", font= ("Helvetica", 20), bg= "red4",
                              fg= "white")
        self.label.grid(row= 0, column= 0, sticky= "nsew")

        self.entry = tk.Entry(self, bg= "SteelBlue1", font= ("Helvetica", 20))
        self.entry.grid(row= 1, column= 0, sticky= "nsew")

        self.generate_graph_button = tk.Button(self, text= "Generate Random Graph", bg= "DarkGreen", font= ("Helvetica", 15),
                                command= self.generate_random_graph)
        self.generate_graph_button.grid(row= 2, column= 0, sticky= "nsew")

        self.finalise_setup_button = tk.Button(self, text= "Finalise Setup", bg= "purple4", font= ("Helvetica", 20),
                                               command= self.finalise_setup)
        self.finalise_setup_button.grid(row= 3, column= 0, sticky= "nsew")

    def generate_random_graph(self):
        nodes = int(self.entry.get())
        self.canvas.generate_random_graph(nodes)

    def finalise_setup(self):
        shortest_path = []
        explanations = []
        visuals = []
        start = None
        goal = None
        step_count = 0
        iteration_count = 1

        for node in node_dict_copy:
            THE_path[node] = {"Path Distance": float("inf"),
                              "Heuristic": 0,
                              "Combined Distance": float("inf"),
                              "Previous Node": None}
            if node_dict_copy[node]["Start"]:
                start = node
            elif node_dict_copy[node]["End"]:
                goal = node

        step_count += 1

        THE_path[start]["Combined Distance"] = 0
        THE_path[start]["Path Distance"] = 0

        explanations.append(f"{step_count}) Set the combined distance of {start} to 0.\n")
        visuals.append(None)

        while node_dict_copy:
            explanations.append(f"Iteration {iteration_count}:\n")
            visuals.append(None)

            shortest = None
            step_count += 1
            for node in node_dict_copy:
                if shortest is None:
                    shortest = node
                elif THE_path[node]["Combined Distance"] < THE_path[shortest]["Combined Distance"]:
                    shortest = node

            explanations.append(f"{step_count}) Found the node with current shortest distance to be {shortest}.\n")
            visuals.append(["New shortest node", shortest])

            if node_dict[shortest]["End"]:
                break

            for neighbour, path_cost in node_dict_copy[shortest]["Neighbours"].items():
                if neighbour == THE_path[shortest]["Previous Node"] or node_dict[neighbour]["Checked"]:
                    continue

                step_count += 1
                explanations.append(f"{step_count}) Checking path between {shortest} and {neighbour}.\n")
                visuals.append(["Checking path", shortest, neighbour])

                if neighbour in node_dict_copy and THE_path[shortest]["Combined Distance"] + \
                        node_dict_copy[shortest]["Neighbours"][
                            neighbour] + node_dict_copy[neighbour]["Heuristic"] < \
                        THE_path[neighbour]["Path Distance"]:
                    step_count += 1
                    explanations.append(
                        f"{step_count}) Found that the path between {shortest} and {neighbour} is quicker than what we originally had for {neighbour}.\n")
                    visuals.append(None)

                    THE_path[neighbour]["Path Distance"] = THE_path[shortest]["Path Distance"] + \
                                                           node_dict_copy[shortest]["Neighbours"][neighbour]
                    THE_path[neighbour]["Combined Distance"] = THE_path[neighbour]["Path Distance"] + \
                                                               THE_path[neighbour]["Heuristic"]
                    THE_path[neighbour]["Previous Node"] = shortest

                    step_count += 1
                    explanations.append(
                        f'''{step_count}) Changed the path distance of {neighbour} to {THE_path[shortest]["Path Distance"] + node_dict_copy[shortest]["Neighbours"][neighbour]}.\n''')
                    visuals.append(None)
                    step_count += 1
                    explanations.append(
                        f'''{step_count}) Change the combined distance of {neighbour} to {THE_path[neighbour]["Path Distance"] + THE_path[neighbour]["Heuristic"]}.\n''')
                    visuals.append(None)
                    step_count += 1
                    explanations.append(f'''{step_count}) Set the previous node for {neighbour} to {shortest}.\n''')
                    visuals.append(None)
                step_count += 1
                explanations.append(f"{step_count}) Finished checking the path between {shortest} and {neighbour}.\n")
                visuals.append(["Checked path", shortest, neighbour])
                node_dict[shortest]["Checked"] = True

            node_dict_copy.pop(shortest)
            step_count += 1
            explanations.append(f"{step_count}) Finished checking all paths for {shortest}.\n")
            visuals.append(["Checked shortest node", shortest])
            iteration_count += 1

        step_count += 1
        explanations.append(
            f"{step_count}) {goal} has the shortest distance. This means we can now work backwards to find the shortest path.\n")
        visuals.append(None)

        current_node = goal
        while current_node is not start:
            shortest_path.insert(0, current_node)
            current_node = THE_path[current_node]["Previous Node"]

        shortest_path.insert(0, start)

        explanations.append("The shortest path is:\n")
        visuals.append(None)
        for i in range(len(shortest_path) - 1):
            explanations.append(f"{shortest_path[i]} -> ")

            if i == 0:
                visuals.append(["Final path start", shortest_path[i]])
            else:
                visuals.append(["Final path", shortest_path[i], shortest_path[i - 1]])
        explanations.append(f"{shortest_path[len(shortest_path) - 1]}")
        visuals.append(["Final path", shortest_path[len(shortest_path) - 1], shortest_path[len(shortest_path) - 2]])

        self.finalising_setup = AStarAlgorithmFrame(self, self.canvas, explanations, visuals)
        self.finalising_setup.grid(row= 0, column= 0, rowspan= 4, sticky= "nsew")

class AStarAlgorithmFrame(tk.Frame):
    def __init__(self, parent, canvas_frame, explanations, visuals):
        super().__init__(parent, bg="red4")

        self.canvas = canvas_frame

        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid_propagate(False)

        self.explanations = explanations
        self.visuals = visuals

        self.textbox = tk.Text(self, wrap=tk.WORD, font=("Helvetica", 15))
        self.textbox.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.label = tk.Label(self, text="Speed:", font=("Helvetica", 20), bg="red4", fg="white")
        self.label.grid(row=1, column=0, sticky="nsew")

        self.speed_slider = tk.Scale(self, from_=1, to=100, orient="horizontal", length=150)
        self.speed_slider.grid(row=1, column=1)

        self.next_step_button = tk.Button(self, text="Next Step", bg="red4", font=("Helvetica", 20),
                                          command= self.run_visuals_man)
        self.next_step_button.grid(row=2, column=0)
        self.next_step_index = 0

        self.run_algorithm_button = tk.Button(self, text="Run Algorithm Auto", font=("Helvetica", 20), bg="purple4",
                                              command= self.run_visuals_auto)
        self.run_algorithm_button.grid(row=2, column=1)

    def run_visuals_auto(self):
        speed = self.speed_slider.get()
        self.run_visuals_automatic(self.explanations, self.visuals, self.next_step_index, speed)

    def run_visuals_automatic(self, explanations, visuals, index, speed):
        if index < len(explanations):
            if explanations[index] is not None:
                self.textbox.insert(tk.END, explanations[index])
                self.textbox.see(tk.END)

            if visuals[index] is not None:
                if visuals[index][0] == "New shortest node":
                    self.canvas.new_shortest_node_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Checking path":
                    self.canvas.checking_path_visual_rand(visuals[index][1], visuals[index][2])
                elif visuals[index][0] == "Checked shortest node":
                    self.canvas.checked_shortest_node_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Checked path":
                    self.canvas.checked_path_visual_rand(visuals[index][1], visuals[index][2])
                elif visuals[index][0] == "Final path start":
                    self.canvas.final_path_start_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Final path":
                    self.canvas.final_path_visual_rand(visuals[index][1], visuals[index][2])

            self.next_step_index += 1
            self.after(101 - speed, lambda: self.run_visuals_automatic(explanations, visuals, self.next_step_index, speed))

    def run_visuals_man(self):
        self.run_visuals_manual(self.explanations, self.visuals, self.next_step_index)

    def run_visuals_manual(self, explanations, visuals, index):
        if index < len(explanations):
            if explanations[index] is not None:
                self.textbox.insert(tk.END, explanations[index])
                self.textbox.see(tk.END)

            if visuals[index] is not None:
                if visuals[index][0] == "New shortest node":
                    self.canvas.new_shortest_node_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Checking path":
                    self.canvas.checking_path_visual_rand(visuals[index][1], visuals[index][2])
                elif visuals[index][0] == "Checked shortest node":
                    self.canvas.checked_shortest_node_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Checked path":
                    self.canvas.checked_path_visual_rand(visuals[index][1], visuals[index][2])
                elif visuals[index][0] == "Final path start":
                    self.canvas.final_path_start_visual_rand(visuals[index][1])
                elif visuals[index][0] == "Final path":
                    self.canvas.final_path_visual_rand(visuals[index][1], visuals[index][2])
            self.next_step_index += 1