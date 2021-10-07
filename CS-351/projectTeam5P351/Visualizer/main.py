from tkinter import *
from tkinter import ttk
import random


# Importing algorithms
from algorithms.bubbleSort import bubbleSort
from algorithms.mergeSort import merge_sort

# Colors for the visualizer
DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
PURPLE = '#BF01FB'

# Main root



# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    root.update_idletasks()


# This function will generate array with random values every time we hit the generate button
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


# This function will set sorting speed
def set_speed():
    if speedMenu.get() == 'Slow':
        return 0.3
    elif speedMenu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


# This funciton will trigger a selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()

    if sorts.get() == 'Bubble Sort':
        bubbleSort(data, drawData, timeTick)
    elif sorts.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, drawData, timeTick)

if __name__ == '__main__':

    root = Tk()
    root.title("Sorting Algorithms Visualization")
    root.maxsize(1000, 700)
    root.config(bg=WHITE)

    sortName = StringVar()
    sorts = ['Bubble Sort', 'Merge Sort']

    speed = StringVar()
    speed_list = ['Fast', 'Medium', 'Slow']

    # data = []

    frame = Frame(root, width=900, height=300, bg=WHITE)
    frame.grid(row=0, column=0, padx=10, pady=5)

    sortLabel = Label(frame, text="Algorithm: ", bg=WHITE)
    sortLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    sorts = ttk.Combobox(frame, textvariable=sortName, values=sorts)
    sorts.grid(row=0, column=1, padx=5, pady=5)
    sorts.current(0)

    speedLabel = Label(frame, text="Sorting Speed: ", bg=WHITE)
    speedLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    speedMenu = ttk.Combobox(frame, textvariable=speed, values=speed_list)
    speedMenu.grid(row=1, column=1, padx=5, pady=5)
    speedMenu.current(0)

    sortButton = Button(frame, text="Go", command=sort, bg=LIGHT_GRAY)
    sortButton.grid(row=2, column=1, padx=5, pady=5)

    generateButton = Button(frame, text="Generate Numbers", command=generate, bg=LIGHT_GRAY)
    generateButton.grid(row=2, column=0, padx=5, pady=5)

    canvas = Canvas(root, width=800, height=400, bg=BLACK)
    canvas.grid(row=0, column=3, padx=10, pady=5)
    
    root.mainloop()