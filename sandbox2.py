import tkinter as tk

def create_stackup_array(given_layers):
    stackup_array = []

    # Verify if given_layers can generate a symmetrical structure
    if given_layers % 2 != 0:
        error_message = "Unable to generate symmetrical stackup with given number of layers."
        stackup_array.append(error_message)
        return stackup_array

    # Calculate the symmetric line
    symmetric_line = given_layers // 2

    # Generate the stackup structure for the upper section
    for i in range(1, symmetric_line):
        if i % 2 == 1:
            stackup_array.append(f"Layer {i} - Upper - Signal")
        else:
            stackup_array.append(f"Layer {i} - Upper - Ground")

    # Generate the stackup structure for the middle section
    stackup_array.append(f"Layer {symmetric_line} - Middle - Power")
    stackup_array.append(f"Layer {symmetric_line + 1} - Middle - Power")

    # Generate the stackup structure for the lower section
    for i in range(symmetric_line + 2, given_layers + 1):
        if i % 2 == 1:
            stackup_array.append(f"Layer {i} - Lower - Ground")
        else:
            stackup_array.append(f"Layer {i} - Lower - Signal")

    return stackup_array

def draw_stackup():
    given_layers = int(entry_given_layers.get())

    # Create the stackup array
    stackup_array = create_stackup_array(given_layers)

    # Display the stackup structure in the console
    for layer in stackup_array:
        print(layer)

# Create the main window
window = tk.Tk()
window.title("PCB Stackup Visualizer")

# Create the UI elements
label_given_layers = tk.Label(window, text="Total Layers:")
entry_given_layers = tk.Entry(window)
button_draw = tk.Button(window, text="Draw", command=draw_stackup)

# Add the UI elements to the window
label_given_layers.pack()
entry_given_layers.pack()
button_draw.pack()

# Start the main event loop
window.mainloop()
