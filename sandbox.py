import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


def update_layer_names():
    new_layer_names = entry.get().split(',')
    new_layer_names = [name.strip() for name in new_layer_names]

    global layer_names
    layer_names = new_layer_names

    global num_layers
    num_layers = len(layer_names)

    update_plot()


def update_plot():
    ax.clear()

    for i in range(num_layers):
        if layer_names[i] == 'Signal':
            ax.fill_between([0.2, 0.8], i, i + 1, color=layer_colors[i])
        else:
            ax.fill_between([0, 1], i, i + 1, color=layer_colors[i])

        ax.text(1.1, i + 0.5, f'{layer_thickness[i]}', ha='left', va='center')
        ax.text(0.5, i + 0.5, layer_names[i], ha='center', va='center', color='white')

    for i in range(num_layers):
        ax.text(-0.5, i + 0.5, f'{i}', ha='center', va='center')

    ax.text(1.2, num_layers/2, 'Thickness', ha='center', va='center', rotation=-90)
    ax.text(0.5, -0.2, 'PCB Stackup', ha='center', va='center')

    canvas.draw()


layer_names = ['Signal', 'Core', 'Prepreg', 'Ground', 'Power']
layer_thickness = [3, 3, 3, 3, 3]
num_layers = len(layer_names)
layer_colors = ['tab:orange', 'lightgreen', 'skyblue', 'gray', 'tab:red']

window = tk.Tk()
window.title("PCB Stackup Configuration")

label = tk.Label(window, text="Layer Names:")
label.pack()

entry = tk.Entry(window)
entry.pack()

entry.insert(tk.END, ", ".join(layer_names))

button = tk.Button(window, text="Update", command=update_layer_names)
button.pack()

fig, ax = plt.subplots(figsize=(4, 6))

canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

update_plot()

window.title('PCB Stackup')
tk.mainloop()
