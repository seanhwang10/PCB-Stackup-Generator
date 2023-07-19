import tkinter as tk
from tkinter import ttk

def calculate_impedance():
    # Get user inputs from the entry widgets
    w = float(w_entry.get())
    s = float(s_entry.get())
    t = float(t_entry.get())
    h_1 = float(h1_entry.get())
    impedance_type = impedance_type_var.get()

    # Calculate impedance based on the type selected
    if impedance_type == "Single Ended":
        Er_1 = float(Er1_entry.get())
        impedance = w / (2 * 3.141592653589793 * s * t) * (1 + (1 + 2 * h_1 / w) ** 0.5)
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er_1 - 1)) + 0.54 * ((Er_1 - 1) ** 2))
    else:
        h_2 = float(h2_entry.get())
        Er_1 = float(Er1_entry.get())
        Er_2 = float(Er2_entry.get())
        impedance = w / (2 * 3.141592653589793 * s * t) * ((1 + (2 * h_1 / w) ** 0.5) + (1 + (2 * h_2 / w) ** 0.5))
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er_1 - 1)) + 0.54 * ((Er_1 - 1) ** 2))
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er_2 - 1)) + 0.54 * ((Er_2 - 1) ** 2))

    # Update the output label with the calculated impedance
    output_label.config(text=f"Impedance: {impedance:.2f} Ohms")

# Create the main application window
root = tk.Tk()
root.title("Impedance Calculator")
root.geometry("400x300")

# Create a label and dropdown menu for impedance type selection
impedance_type_label = tk.Label(root, text="Select Impedance Type:")
impedance_type_label.pack(pady=10)
impedance_type_var = tk.StringVar()
impedance_type_var.set("Single Ended")
impedance_type_menu = ttk.OptionMenu(root, impedance_type_var, "Single Ended", "Differential")
impedance_type_menu.pack()

# Create entry widgets for user inputs
w_label = tk.Label(root, text="Enter w:")
w_label.pack()
w_entry = tk.Entry(root)
w_entry.pack()

s_label = tk.Label(root, text="Enter s:")
s_label.pack()
s_entry = tk.Entry(root)
s_entry.pack()

t_label = tk.Label(root, text="Enter t:")
t_label.pack()
t_entry = tk.Entry(root)
t_entry.pack()

h1_label = tk.Label(root, text="Enter h_1:")
h1_label.pack()
h1_entry = tk.Entry(root)
h1_entry.pack()

Er1_label = tk.Label(root, text="Enter Er_1:")
Er1_label.pack()
Er1_entry = tk.Entry(root)
Er1_entry.pack()

# Entries for differential impedance
h2_label = tk.Label(root, text="Enter h_2:")
h2_entry = tk.Entry(root)
Er2_label = tk.Label(root, text="Enter Er_2:")
Er2_entry = tk.Entry(root)

# Create the "Calculate Impedance" button
calculate_button = tk.Button(root, text="Calculate Impedance", command=calculate_impedance)
calculate_button.pack(pady=20)

# Create a label to display the output impedance
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
