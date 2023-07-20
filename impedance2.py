# Impedance 2 - Microstrip SE, Diff formula integration.

import tkinter as tk
from tkinter import ttk
import math

def calculate_impedance():
    # Get user inputs from the entry widgets based on the selected tab
    selected_tab = impedance_notebook.index(impedance_notebook.select())
    
    # (Local) Global Parameters for comfort
    n_0 = 376.730313668         # Wave Impedance in free space 
    pi = math.pi                # Pi - 3.14..... 


    if selected_tab == 0:  # Microstrip - SE
        w = float(microstrip_se_w_entry.get())
        t = float(microstrip_se_t_entry.get())
        h = float(microstrip_se_h_entry.get())
        Er = float(microstrip_se_Er_entry.get())

        ln_content = 0          
        w_eff = 0
        X1 = 0
        X2 = 0 
        
        # Equation (1) 
        ln_content = (4*math.e)/(math.sqrt((t / h)**2 + (t / (w*pi + 1.1*t*pi))**2))
        w_eff = w + (t/pi) * math.log(ln_content, math.e) * ((Er+1)/(2*Er))
        X1 = 4 * ((14*Er+8) / (11 * Er)) * (h / w_eff)
        X2 = math.sqrt(16 * (h / w_eff)**2 * ((14 * Er + 8) / (11 * Er))**2 + ((Er + 1) / (2 * Er)) * pi**2) 
        ln_content = 1+4*(h/w_eff)
        impedance = (n_0 / (2*pi*math.sqrt(2)*math.sqrt(Er+1))) * math.log(ln_content,math.e) * (X1+X2)

        # Test to show Kevin
        print("W_eff: ")
        print(w_eff)
        print("\nX1, X2 : ")
        print(X1,X2)

    elif selected_tab == 1:  # Microstrip - Diff
        w = float(microstrip_diff_w_entry.get())
        s = float(microstrip_diff_s_entry.get())
        t = float(microstrip_diff_t_entry.get())
        h = float(microstrip_diff_h_entry.get())
        Er = float(microstrip_diff_Er_entry.get())
        impedance = w / (2 * 3.141592653589793 * s * t) * (1 + (1 + 12 * h / w) ** 0.5)
        impedance *= (1 + 0.04 * (Er - 1) / (Er + 1))

    elif selected_tab == 2:  # Stripline - SE
        w = float(stripline_se_w_entry.get())
        t = float(stripline_se_t_entry.get())
        h1 = float(stripline_se_h1_entry.get())
        Er1 = float(stripline_se_Er1_entry.get())
        impedance = w / (2 * 3.141592653589793 * t) * (1 + (1 + 2 * h1 / w) ** 0.5)
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er1 - 1)) + 0.54 * ((Er1 - 1) ** 2))

    else:  # Stripline - Diff
        w = float(stripline_diff_w_entry.get())
        s = float(stripline_diff_s_entry.get())
        t = float(stripline_diff_t_entry.get())
        h1 = float(stripline_diff_h1_entry.get())
        h2 = float(stripline_diff_h2_entry.get())
        Er1 = float(stripline_diff_Er1_entry.get())
        Er2 = float(stripline_diff_Er2_entry.get())
        impedance = w / (2 * 3.141592653589793 * s * t) * ((1 + (2 * h1 / w) ** 0.5) + (1 + (2 * h2 / w) ** 0.5))
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er1 - 1)) + 0.54 * ((Er1 - 1) ** 2))
        impedance *= (1 - 0.48 * math.exp(-0.96 * (Er2 - 1)) + 0.54 * ((Er2 - 1) ** 2))

    # Update the output label with the calculated impedance
    output_label.config(text=f"Impedance: {impedance:.2f} Ohms")

# Create the main application window
root = tk.Tk()
root.title("Impedance Calculator")
root.geometry("500x550")

# Create a notebook (tabbed interface)
impedance_notebook = ttk.Notebook(root)
impedance_notebook.pack(fill=tk.BOTH, expand=True)

# Create the Microstrip - SE tab
microstrip_se_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(microstrip_se_tab, text="Microstrip - SE")

# Create entry widgets for Microstrip - SE inputs
microstrip_se_w_label = tk.Label(microstrip_se_tab, text="Enter w:")
microstrip_se_w_label.pack()
microstrip_se_w_entry = tk.Entry(microstrip_se_tab)
microstrip_se_w_entry.pack()

microstrip_se_t_label = tk.Label(microstrip_se_tab, text="Enter t:")
microstrip_se_t_label.pack()
microstrip_se_t_entry = tk.Entry(microstrip_se_tab)
microstrip_se_t_entry.pack()

microstrip_se_h_label = tk.Label(microstrip_se_tab, text="Enter h:")
microstrip_se_h_label.pack()
microstrip_se_h_entry = tk.Entry(microstrip_se_tab)
microstrip_se_h_entry.pack()

microstrip_se_Er_label = tk.Label(microstrip_se_tab, text="Enter Er:")
microstrip_se_Er_label.pack()
microstrip_se_Er_entry = tk.Entry(microstrip_se_tab)
microstrip_se_Er_entry.pack()

# Create the Microstrip - Diff tab
microstrip_diff_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(microstrip_diff_tab, text="Microstrip - Diff")

# Create entry widgets for Microstrip - Diff inputs
microstrip_diff_w_label = tk.Label(microstrip_diff_tab, text="Enter w:")
microstrip_diff_w_label.pack()
microstrip_diff_w_entry = tk.Entry(microstrip_diff_tab)
microstrip_diff_w_entry.pack()

microstrip_diff_s_label = tk.Label(microstrip_diff_tab, text="Enter s:")
microstrip_diff_s_label.pack()
microstrip_diff_s_entry = tk.Entry(microstrip_diff_tab)
microstrip_diff_s_entry.pack()

microstrip_diff_t_label = tk.Label(microstrip_diff_tab, text="Enter t:")
microstrip_diff_t_label.pack()
microstrip_diff_t_entry = tk.Entry(microstrip_diff_tab)
microstrip_diff_t_entry.pack()

microstrip_diff_h_label = tk.Label(microstrip_diff_tab, text="Enter h:")
microstrip_diff_h_label.pack()
microstrip_diff_h_entry = tk.Entry(microstrip_diff_tab)
microstrip_diff_h_entry.pack()

microstrip_diff_Er_label = tk.Label(microstrip_diff_tab, text="Enter Er:")
microstrip_diff_Er_label.pack()
microstrip_diff_Er_entry = tk.Entry(microstrip_diff_tab)
microstrip_diff_Er_entry.pack()

# Create the Stripline - SE tab
stripline_se_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(stripline_se_tab, text="Stripline - SE")

# Create entry widgets for Stripline - SE inputs
stripline_se_w_label = tk.Label(stripline_se_tab, text="Enter w:")
stripline_se_w_label.pack()
stripline_se_w_entry = tk.Entry(stripline_se_tab)
stripline_se_w_entry.pack()

stripline_se_t_label = tk.Label(stripline_se_tab, text="Enter t:")
stripline_se_t_label.pack()
stripline_se_t_entry = tk.Entry(stripline_se_tab)
stripline_se_t_entry.pack()

stripline_se_h1_label = tk.Label(stripline_se_tab, text="Enter h_1:")
stripline_se_h1_label.pack()
stripline_se_h1_entry = tk.Entry(stripline_se_tab)
stripline_se_h1_entry.pack()

stripline_se_Er1_label = tk.Label(stripline_se_tab, text="Enter Er_1:")
stripline_se_Er1_label.pack()
stripline_se_Er1_entry = tk.Entry(stripline_se_tab)
stripline_se_Er1_entry.pack()

# Create the Stripline - Diff tab
stripline_diff_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(stripline_diff_tab, text="Stripline - Diff")

# Create entry widgets for Stripline - Diff inputs
stripline_diff_w_label = tk.Label(stripline_diff_tab, text="Enter w:")
stripline_diff_w_label.pack()
stripline_diff_w_entry = tk.Entry(stripline_diff_tab)
stripline_diff_w_entry.pack()

stripline_diff_s_label = tk.Label(stripline_diff_tab, text="Enter s:")
stripline_diff_s_label.pack()
stripline_diff_s_entry = tk.Entry(stripline_diff_tab)
stripline_diff_s_entry.pack()

stripline_diff_t_label = tk.Label(stripline_diff_tab, text="Enter t:")
stripline_diff_t_label.pack()
stripline_diff_t_entry = tk.Entry(stripline_diff_tab)
stripline_diff_t_entry.pack()

stripline_diff_h1_label = tk.Label(stripline_diff_tab, text="Enter h_1:")
stripline_diff_h1_label.pack()
stripline_diff_h1_entry = tk.Entry(stripline_diff_tab)
stripline_diff_h1_entry.pack()

stripline_diff_h2_label = tk.Label(stripline_diff_tab, text="Enter h_2:")
stripline_diff_h2_label.pack()
stripline_diff_h2_entry = tk.Entry(stripline_diff_tab)
stripline_diff_h2_entry.pack()

stripline_diff_Er1_label = tk.Label(stripline_diff_tab, text="Enter Er_1:")
stripline_diff_Er1_label.pack()
stripline_diff_Er1_entry = tk.Entry(stripline_diff_tab)
stripline_diff_Er1_entry.pack()

stripline_diff_Er2_label = tk.Label(stripline_diff_tab, text="Enter Er_2:")
stripline_diff_Er2_label.pack()
stripline_diff_Er2_entry = tk.Entry(stripline_diff_tab)
stripline_diff_Er2_entry.pack()

# Create the "Calculate Impedance" button
calculate_button = tk.Button(root, text="Calculate Impedance", command=calculate_impedance)
calculate_button.pack(pady=20)

# Create a label to display the output impedance
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
