import tkinter as tk
from tkinter import messagebox
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tsp_solver  # Rust module we built

NUM_CITIES = 10
cities = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(NUM_CITIES)]

root = tk.Tk()
root.title("Travelling Salesman Problem (Rust + Python GUI)")

fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def draw_graph(path=None):
    ax.clear()
    xs, ys = zip(*cities)
    ax.scatter(xs, ys, c="blue")

    for i, (x, y) in enumerate(cities):
        ax.text(x + 0.1, y + 0.1, str(i), fontsize=9)

    if path:
        px = [cities[i][0] for i in path] + [cities[path[0]][0]]
        py = [cities[i][1] for i in path] + [cities[path[0]][1]]
        ax.plot(px, py, c="red", lw=2)

    canvas.draw()

def solve_and_show():
    order, dist = tsp_solver.solve_tsp(cities)
    draw_graph(order)
    messagebox.showinfo("TSP Solution", f"Shortest distance: {dist:.2f}\nOrder: {order}")

button = tk.Button(root, text="Solve TSP", command=solve_and_show)
button.pack(pady=10)

draw_graph()
root.mainloop()
