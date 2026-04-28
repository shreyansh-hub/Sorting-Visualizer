# main.py
from visualizer import SortingVisualizer
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
