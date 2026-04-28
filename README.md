# 🔢 Sorting Visualizer

> A Python + Tkinter desktop app that brings sorting algorithms to life — watch Bubble, Selection, and Insertion Sort work step-by-step in real time.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📸 Preview

Each bar represents a number in the array. Colors show what's happening at each step:

| Color | Meaning |
|-------|---------|
| 🔵 Sky Blue | Unsorted element |
| 🔴 Red | Currently being compared |
| 🟡 Yellow | Current position (Selection Sort) |
| 🟣 Purple | Minimum / Key element |
| 🟢 Green | Sorted ✓ |

---

## ✨ Features

- 🎲 **Random Array Generation** — Generate a fresh 50-element array instantly
- 📊 **3 Sorting Algorithms** — Bubble Sort, Selection Sort, Insertion Sort
- ⚡ **Adjustable Speed** — Slow down or speed up the animation with a slider
- 🎨 **Color-Coded Visualization** — See exactly which elements are being compared or swapped
- 🖥️ **Smooth, Non-Blocking UI** — Uses `after()` instead of `time.sleep()` so the window never freezes

---

## 🧠 Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Bubble Sort | O(n²) | O(1) |
| Selection Sort | O(n²) | O(1) |
| Insertion Sort | O(n²) | O(1) |

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** — built-in Python GUI library (no extra installs needed)

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/shreyansh-hub/Sorting-Visualizer.git
cd Sorting-Visualizer
```

**2. Run the app**
```bash
python main.py
```

> ✅ No external dependencies — Tkinter comes built into Python.

---

## 📁 Project Structure

```
Sorting-Visualizer/
│
├── main.py          # Entry point — launches the Tkinter window
└── visualizer.py    # Core logic — UI, drawing, and sorting algorithms
```

---

## 🎮 How to Use

1. Click **"Generate Array"** to create a random array
2. Use the **speed slider** to set animation speed
3. Click any sort button — **Bubble Sort**, **Selection Sort**, or **Insertion Sort**
4. Watch the algorithm sort the array step-by-step
5. Bars turn **green** when fully sorted ✅

---

## 🔮 Future Enhancements

- [ ] Add Merge Sort and Quick Sort
- [ ] Pause / Resume / Reset controls
- [ ] Adjustable array size
- [ ] Sound effects for comparisons and swaps
- [ ] Step counter and comparison counter display

---

## 👤 Author

**Shreyansh** — [github.com/shreyansh-hub](https://github.com/shreyansh-hub)
