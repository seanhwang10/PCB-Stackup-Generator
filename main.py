import matplotlib.pyplot as plt
import numpy as np

red = [[255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255]]
green = [[0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0], [0, 255, 0]]
blue = [[0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]]

data = [
    red, green, blue, red, green, blue
]

fig, ax1 = plt.subplots()

ax1.imshow(data, aspect='auto')
ax1.axis('off')

# Add text to a specific grid

plt.show()
