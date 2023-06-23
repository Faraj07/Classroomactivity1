import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.title("My Graph")

# Generate some data for the graph
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# Create a Matplotlib figure and plot the data
fig = plt.Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.set_title("My Graph")

# Create a canvas to embed the graph in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Start the Tkinter event loop
root.mainloop()
