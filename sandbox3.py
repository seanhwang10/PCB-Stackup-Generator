import tkinter as tk
import matplotlib.pyplot as plt

COLOR_SIGNAL = "orange"
COLOR_GROUND = "grey"
COLOR_POWER = "red"

def create_stackup_image(given_layers):
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)

    stackup_array = create_stackup_array(given_layers)

    ax.axis('off')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    for i, layer in enumerate(stackup_array[::-1]):
        layer_name, layer_type = layer.split(" - ")
        if layer_type == "Signal":
            layer_width = 1/5
            x_start = (1 - layer_width) / 2
            x_end = x_start + layer_width
            ax.fill_between([x_start, x_end], [i / given_layers, i / given_layers], [(i + 1) / given_layers, (i + 1) / given_layers], color=COLOR_SIGNAL)
        else:
            ax.fill_between([0, 1], [i / given_layers, i / given_layers], [(i + 1) / given_layers, (i + 1) / given_layers], color=COLOR_GROUND)

        ax.text(0.05, (i + 0.5) / given_layers, layer_name, va='center')

    return fig

def create_stackup_array(given_layers):
    stackup_array = []

    if ((given_layers - 2) / 2) % 2 != 0:
        error_message = "Unable to generate symmetrical stackup with given number of layers."
        stackup_array.append(error_message)
        return stackup_array

    symmetric_line = given_layers // 2

    for i in range(1, symmetric_line):
        if i % 2 == 1:
            stackup_array.append(f"Layer {i} - Upper - Signal")
        else:
            stackup_array.append(f"Layer {i} - Upper - Ground")

    stackup_array.append(f"Layer {symmetric_line} - Middle - Power")
    stackup_array.append(f"Layer {symmetric_line + 1} - Middle - Power")

    for i in range(symmetric_line + 2, given_layers + 1):
        if i % 2 == 1:
            stackup_array.append(f"Layer {i} - Lower - Ground")
        else:
            stackup_array.append(f"Layer {i} - Lower - Signal")

    return stackup_array

def draw_stackup():
    given_layers = int(entry_given_layers.get())

    fig = create_stackup_image(given_layers)

    fig.show()

window = tk.Tk()
window.title("PCB Stackup Visualizer")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = int(screen_width * 0.6)
window_height = int(screen_height * 0.6)
window.geometry(f"{window_width}x{window_height}")

label_given_layers = tk.Label(window, text="Total Layers:")
entry_given_layers = tk.Entry(window)
button_draw = tk.Button(window, text="Draw", command=draw_stackup)

label_given_layers.pack()
entry_given_layers.pack()
button_draw.pack()

window.mainloop()
