# Sorting Visualizer

A desktop app built with Python and Tkinter that visually shows how sorting algorithms work. I made this to better understand how Bubble Sort, Selection Sort, and Insertion Sort actually behave under the hood.

---

## What it does

You generate a random array of bars, pick a sorting algorithm, and watch it sort step by step. Each bar represents a number — taller bar means bigger number. Colors show what the algorithm is doing at each moment.

- **Red** → elements being compared
- **Yellow / Purple** → current position or minimum element
- **Green** → sorted

There's also a speed slider so you can slow it down if you want to follow along.

---

## How to run

Make sure you have Python 3 installed. Tkinter comes built-in so no extra installs needed.

```bash
git clone https://github.com/shreyansh-hub/Sorting-Visualizer.git
cd Sorting-Visualizer
python main.py
```

---

## Algorithms included

- Bubble Sort
- Selection Sort
- Insertion Sort

---

## One thing worth mentioning

Early on I used `time.sleep()` for the animation delay, which froze the entire window. Switched to Tkinter's `after()` method instead — it schedules each step without blocking the main loop, so the UI stays responsive throughout.

---

## Files

- `main.py` — starts the app
- `visualizer.py` — everything else (UI, drawing, sorting logic)

---

## What I'd add next

- Merge Sort and Quick Sort
- Pause and reset controls
- Adjustable array size
