# Sandbox 2: Signal, Power, Ground layer placement.

import tkinter as tk

stackup_array = []
layer_number = []

def create_stackup_array(given_layers):
    global stackup_array
    global layer_number

    if ((given_layers - 2) / 2) % 2 != 0:
        error_message = "Unable to generate symmetrical stackup with the given number of layers."
        label_output.config(text=error_message)
        return

    symmetric_line = given_layers // 2

    stackup_array = []

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

    final_array = stackup_array
    output_text = "\n".join(stackup_array)
    label_output.config(text=output_text)

    print(stackup_array)

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
