import tkinter as tk

stackup_array = []
layer_number = []

def create_stackup_array(given_layers):
    global stackup_array
    global layer_number

    if ((given_layers - 2) / 2) % 2 != 0:
        error_message = "Unable to generate a symmetrical stackup with the given number of layers."
        label_output.config(text=error_message)
        return

    symmetric_line = given_layers // 2

    stackup_array = []
    layer_number = []

    for i in range(1, symmetric_line):
        if i % 2 == 1:
            stackup_array.append("Signal")
            layer_number.append(f"Layer {i}")
        else:
            stackup_array.append("Ground")
            layer_number.append(f"Layer {i}")

    stackup_array.append("Power")
    layer_number.append(f"Layer {symmetric_line}")
    stackup_array.append("Power")
    layer_number.append(f"Layer {symmetric_line + 1}")

    for i in range(symmetric_line + 2, given_layers + 1):
        if i % 2 == 1:
            stackup_array.append("Ground")
            layer_number.append(f"Layer {i}")
        else:
            stackup_array.append("Signal")
            layer_number.append(f"Layer {i}")

    output_text = "\n".join(stackup_array)
    label_output.config(text=output_text)

    display_stackup_visual()

def display_stackup_visual():
    stackup_window = tk.Toplevel(window)
    stackup_window.title("Stackup Structure")

    num_layers = len(stackup_array)
    layer_height = 30  # Reduce the layer height for a more compact visualization
    stackup_width = 400
    stackup_height = num_layers * layer_height

    stackup_canvas = tk.Canvas(stackup_window, width=stackup_width, height=stackup_height)
    stackup_canvas.pack()

    for i, layer in enumerate(stackup_array):
        layer_y = i * layer_height  # Adjust the y-coordinate based on the layer index

        if layer == "Signal":
            rect_width = stackup_width * 2 / 5
            color = "orange"
        elif layer == "Ground":
            rect_width = stackup_width
            color = "grey"
        elif layer == "Power":
            rect_width = stackup_width
            color = "red"

        layer_rect_x1 = (stackup_width - rect_width) / 2
        layer_rect_x2 = layer_rect_x1 + rect_width

        stackup_canvas.create_rectangle(layer_rect_x1, layer_y, layer_rect_x2, layer_y + layer_height, fill=color)
        stackup_canvas.create_text(20, layer_y + layer_height / 2, text=layer_number[i], anchor="w")
        stackup_canvas.create_text(stackup_width / 2, layer_y + layer_height / 2, text=layer, anchor="center")

    stackup_window.geometry(f"{stackup_width}x{stackup_height}")

def draw_stackup():
    given_layers = int(entry_given_layers.get())
    create_stackup_array(given_layers)

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
label_output = tk.Label(window, text="")

label_given_layers.pack()
entry_given_layers.pack()
button_draw.pack()
label_output.pack()

window.mainloop()
