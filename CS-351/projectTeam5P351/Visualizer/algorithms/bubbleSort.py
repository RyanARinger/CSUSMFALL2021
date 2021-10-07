# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
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


def bubbleSort(numbers, drawNumbers, timeTick):
    size = len(numbers)
    for i in range(size - 1):
        for j in range(size - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                drawNumbers(numbers, [YELLOW if x == j or x == j + 1 else BLUE for x in range(len(numbers))])
                time.sleep(timeTick)

    drawNumbers(numbers, [BLUE for x in range(len(numbers))])