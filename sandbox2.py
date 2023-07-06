import tkinter as tk

# Constants for color scheme
COLOR_PACKAGE = "green"
COLOR_SIGNAL = "orange"
COLOR_PREPREG = "skyblue"
COLOR_CORE = "lightgreen"
COLOR_POWER = "red"

# Constants for material sizes
WIDTH_SIGNAL = 1
WIDTH_OTHERS = 5

def draw_stackup(total_layers, signal_layers):
    canvas.delete("all")

    # Calculate the number of core and prepreg layers
    core_prepreg_layers = total_layers - signal_layers - 4

    # Draw the top and bottom package layers
    draw_layer(COLOR_PACKAGE, WIDTH_OTHERS, "Package")

    # Draw the signal, prepreg, and ground layers
    draw_signal_layer(signal_layers)

    # Draw the core, signal, prepreg, and ground layers
    for _ in range(core_prepreg_layers):
        draw_layer(COLOR_CORE, WIDTH_OTHERS, "Core")
        draw_signal_layer(signal_layers)
        draw_layer(COLOR_PREPREG, WIDTH_OTHERS, "Prepreg")
        draw_layer(COLOR_CORE, WIDTH_OTHERS, "Core")

    # Draw the power layer
    draw_layer(COLOR_CORE, WIDTH_OTHERS, "Core")
    draw_layer(COLOR_POWER, WIDTH_OTHERS, "Power")
    draw_layer(COLOR_PREPREG, WIDTH_OTHERS, "Prepreg")
    draw_layer(COLOR_POWER, WIDTH_OTHERS, "Power")
    draw_layer(COLOR_CORE, WIDTH_OTHERS, "Core")

    # Draw the remaining signal, prepreg, and ground layers
    draw_signal_layer(signal_layers)
    draw_layer(COLOR_PREPREG, WIDTH_OTHERS, "Prepreg")
    draw_layer(COLOR_CORE, WIDTH_OTHERS, "Core")

def draw_layer(color, width, label_text):
    x1 = 10
    x2 = 390
    y1 = canvas.winfo_height() - 10
    y2 = y1 - 40

    # Center the signal material
    if width == WIDTH_SIGNAL:
        x1 = (x1 + x2) / 2 - (x2 - x1) / 10
        x2 = (x1 + x2) / 2 + (x2 - x1) / 10

    canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)
    canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=label_text)

def draw_signal_layer(signal_layers):
    for _ in range(signal_layers):
        draw_layer(COLOR_SIGNAL, WIDTH_SIGNAL, "Signal")

# Create the main window
window = tk.Tk()
window.title("PCB Stackup Visualizer")

# Create the UI elements
label_total_layers = tk.Label(window, text="Total Layers:")
entry_total_layers = tk.Entry(window)
label_signal_layers = tk.Label(window, text="Signal Layers:")
entry_signal_layers = tk.Entry(window)
button_draw = tk.Button(window, text="Draw", command=lambda: draw_stackup(int(entry_total_layers.get()), int(entry_signal_layers.get())))
canvas = tk.Canvas(window, width=400, height=800)

# Add the UI elements to the window
label_total_layers.pack()
entry_total_layers.pack()
label_signal_layers.pack()
entry_signal_layers.pack()
button_draw.pack()
canvas.pack()

# Start the main event loop
window.mainloop()
