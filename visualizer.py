import tkinter as tk
import random

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.geometry("800x500")
        self.root.config(bg="white")

        self.array = []
        self.speed = tk.DoubleVar()
        self.speed.set(0.1)

        # UI Frame
        self.ui_frame = tk.Frame(root, width=800, height=100, bg="lightgray")
        self.ui_frame.pack(padx=10, pady=5)

        # Buttons
        self.generate_button = tk.Button(self.ui_frame, text="Generate Array", command=self.generate_array, bg="green", fg="white")
        self.generate_button.grid(row=0, column=0, padx=5, pady=5)

        self.bubble_button = tk.Button(self.ui_frame, text="Bubble Sort", command=self.start_bubble_sort, bg="orange", fg="white", state="disabled")
        self.bubble_button.grid(row=0, column=1, padx=5, pady=5)

        self.selection_button = tk.Button(self.ui_frame, text="Selection Sort", command=self.start_selection_sort, bg="blue", fg="white", state="disabled")
        self.selection_button.grid(row=0, column=2, padx=5, pady=5)

        self.insertion_button = tk.Button(self.ui_frame, text="Insertion Sort", command=self.start_insertion_sort, bg="purple", fg="white", state="disabled")
        self.insertion_button.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(self.ui_frame, text="Speed (sec):").grid(row=0, column=4, padx=5, pady=5)
        tk.Scale(self.ui_frame, from_=0.01, to=1.0, length=100, resolution=0.01, orient=tk.HORIZONTAL, variable=self.speed).grid(row=0, column=5, padx=5, pady=5)

        # Canvas for bars
        self.canvas = tk.Canvas(root, width=780, height=380, bg="white")
        self.canvas.pack(padx=10, pady=5)

    # -------------------------
    # Generate random array
    # -------------------------
    def generate_array(self):
        self.array = [random.randint(10, 100) for _ in range(50)]
        self.draw_array()
        # Enable sort buttons
        self.bubble_button.config(state="normal")
        self.selection_button.config(state="normal")
        self.insertion_button.config(state="normal")

    # -------------------------
    # Draw array bars
    # -------------------------
    def draw_array(self, color_array=None):
        if not self.array:
            return
        self.canvas.delete("all")
        c_height = 380
        c_width = 780
        x_width = c_width / len(self.array)
        offset = 5
        spacing = 2

        if color_array is None:
            color_array = ["skyblue" for _ in range(len(self.array))]

        for i, val in enumerate(self.array):
            x0 = i * x_width + offset + spacing
            y0 = c_height - val * 3
            x1 = (i + 1) * x_width + offset
            y1 = c_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
            self.canvas.create_text(x0+2, y0, anchor=tk.SW, text=str(val), font=("Arial", 8))
        self.root.update_idletasks()

    # -------------------------
    # Start sorting wrappers
    # -------------------------
    def start_bubble_sort(self):
        self.disable_buttons()
        self.bubble_sort_generator(0,0)

    def start_selection_sort(self):
        self.disable_buttons()
        self.selection_sort_generator(0,1,0)

    def start_insertion_sort(self):
        self.disable_buttons()
        self.insertion_sort_generator(1)

    # -------------------------
    # Disable / Enable buttons
    # -------------------------
    def disable_buttons(self):
        self.bubble_button.config(state="disabled")
        self.selection_button.config(state="disabled")
        self.insertion_button.config(state="disabled")
        self.generate_button.config(state="disabled")

    def enable_buttons(self):
        self.bubble_button.config(state="normal")
        self.selection_button.config(state="normal")
        self.insertion_button.config(state="normal")
        self.generate_button.config(state="normal")

    # -------------------------
    # Bubble Sort (generator with after)
    # -------------------------
    def bubble_sort_generator(self, i, j):
        if i < len(self.array)-1:
            if j < len(self.array)-i-1:
                color_array = ["skyblue" for _ in range(len(self.array))]
                color_array[j] = "red"
                color_array[j+1] = "red"
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                self.draw_array(color_array)
                self.root.after(int(self.speed.get()*1000), lambda: self.bubble_sort_generator(i,j+1))
            else:
                self.root.after(0, lambda: self.bubble_sort_generator(i+1,0))
        else:
            self.draw_array(["green" for _ in range(len(self.array))])
            self.enable_buttons()

    # -------------------------
    # Selection Sort (generator with after)
    # -------------------------
    def selection_sort_generator(self, i, j, min_idx):
        if i < len(self.array):
            if j < len(self.array):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
                color_array = ["skyblue" for _ in range(len(self.array))]
                color_array[i] = "yellow"
                color_array[j] = "red"
                color_array[min_idx] = "purple"
                self.draw_array(color_array)
                self.root.after(int(self.speed.get()*1000), lambda: self.selection_sort_generator(i, j+1, min_idx))
            else:
                self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
                self.root.after(0, lambda: self.selection_sort_generator(i+1, i+2, i+1))
        else:
            self.draw_array(["green" for _ in range(len(self.array))])
            self.enable_buttons()

    # -------------------------
    # Insertion Sort (generator with after)
    # -------------------------
    def insertion_sort_generator(self, i):
        if i < len(self.array):
            key = self.array[i]
            j = i-1
            def inner_loop(j_inner):
                if j_inner >= 0 and key < self.array[j_inner]:
                    self.array[j_inner+1] = self.array[j_inner]
                    color_array = ["skyblue" for _ in range(len(self.array))]
                    color_array[j_inner+1] = "red"
                    color_array[i] = "purple"
                    self.draw_array(color_array)
                    self.root.after(int(self.speed.get()*1000), lambda: inner_loop(j_inner-1))
                else:
                    self.array[j_inner+1] = key
                    self.root.after(0, lambda: self.insertion_sort_generator(i+1))
            inner_loop(j)
        else:
            self.draw_array(["green" for _ in range(len(self.array))])
            self.enable_buttons()
