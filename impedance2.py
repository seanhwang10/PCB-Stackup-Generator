# Impedance 2 - Microstrip SE, Diff formula integration.
# Sean Hwang (seahwang@cisco.com)

import tkinter as tk
from tkinter import ttk
import math

def calculate_impedance():
    # Entry Widget
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
    
        ln_content = (4*math.e)/(math.sqrt((t / h)**2 + (t / (w*pi + 1.1*t*pi))**2))
        w_eff = w + (t/pi) * math.log(ln_content, math.e) * ((Er+1)/(2*Er))                                     #2
        
        X1 = 4 * ((14*Er+8) / (11 * Er)) * (h / w_eff)                                                          #3
        
        X2 = math.sqrt(16 * (h / w_eff)**2 * ((14 * Er + 8) / (11 * Er))**2 + ((Er + 1) / (2 * Er)) * pi**2)    #4
        
        ln_content = 1+4*(h/w_eff)*(X1+X2)
        impedance = (n_0 / (2*pi*math.sqrt(2)*math.sqrt(Er+1))) * math.log(ln_content,math.e)                   #1 

        # # Test to show Parameters
        # print("W_eff: ")
        # print(w_eff)
        # print("\nX1, X2 : ")
        # print(X1,X2)

    elif selected_tab == 1:  # Microstrip - Diff
        w = float(microstrip_diff_w_entry.get())
        s = float(microstrip_diff_s_entry.get())
        t = float(microstrip_diff_t_entry.get())
        h = float(microstrip_diff_h_entry.get())
        Er = float(microstrip_diff_Er_entry.get())

        # Zo calculation (Same with MSSE calc)
        ln_content = (4*math.e)/(math.sqrt((t / h)**2 + (t / (w*pi + 1.1*t*pi))**2))
        w_eff = w + (t/pi) * math.log(ln_content, math.e) * ((Er+1)/(2*Er))                                     #2
        
        X1 = 4 * ((14*Er+8) / (11 * Er)) * (h / w_eff)                                                          #3
        
        X2 = math.sqrt(16 * (h / w_eff)**2 * ((14 * Er + 8) / (11 * Er))**2 + ((Er + 1) / (2 * Er)) * pi**2)    #4
        
        ln_content = 1+4*(h/w_eff)*(X1+X2)
        Zo = (n_0 / (2*pi*math.sqrt(2)*math.sqrt(Er+1))) * math.log(ln_content,math.e)                          #1 
   
        # Calculation Begin
        u = w / h 
        g = s / h 
        Er_eff = 0
        Er_eff0 = 0 
        a0 = 0 
        b0 = 0
        c0 = 0
        

        if u < 1:
            Er_eff = ((Er + 1) / 2) + ((Er - 1) / 2) * ((math.sqrt(w / (w+12*h))) + 0.04 * ((w / (w + 12 * h))**2)) #7

        else: 
            Er_eff = ((Er + 1) / 2) + ((Er - 1) / 2) * (math.sqrt(w / (w+12*h)))                #8 

        a0 = 0.7287 * (Er_eff - ((Er + 1)/2)) * (math.sqrt(1 - (math.exp(-0.179 * u))))         #9 
        
        b0 = (0.747 * Er) / (0.15 + Er)                                                         #10 
        
        c0 = b0 - (b0 - 0.207) * (math.exp(-0.414 * u))                                         #11 
        
        d0 = 0.593 + 0.694 * math.exp(-0.562 * u)                                               #12 
        
        q1 = 0.8695 * u**0.194                                                                  #13
        
        q2 = 1 + 0.7519 * g + 0.189 * g**2.31                                                   #14
        
        ln_content = (g**10)/(1+(g/3.4)**10)
        q3 = 0.1975 + ((16.6 + (8.4 / g)**6)**-0.387) + (1/241)*math.log(ln_content,math.e)     #15
        
        q4 = (2 * q1) / (q2*(math.exp(-g) * u**q3 + (2- math.exp(-g)) * u**(-q3)))              #16
        
        ln_content = 1 + (0.638 / (g + 0.517 * g**2.43))
        q5 = 1.794 + 1.14 * math.log(ln_content, math.e)                                        #17
        
        ln_content = (g**10) / (1 + (g / 5.8)**10)
        q6 = 0.2305 + (1 / 281.3) * math.log(ln_content, math.e)                                
        ln_content = 1 + 0.598 * (g**1.154)
        q6 = q6 + (1/5.1) * math.log(ln_content, math.e)                                        #18
        
        q7 = (10 + 190 * (g**2)) / (1 + 82.3 * (g**3))                                          #19

        q8 = math.exp(-6.5 - 0.95 * math.log(g, math.e) - (g / 0.15)**5)                        #20 

        q9 = math.log(q7, math.e) * (q8 + (1 / 16.5))                                           #21

        q10 = (1/q2) * (q2 * q4 - q5 * math.exp(math.log(u, math.e)*q6*u**(-q9)))               #22 

        Er_eff0 = ((0.5 * (Er + 1) + a0 - Er_eff) * math.exp(-c0 * g**d0)) + Er_eff             #23 

        impedance = Zo * (math.sqrt(Er_eff / Er_eff0) / (1 - ((Zo/n_0)* q10 * math.sqrt(Er_eff))))  #24 


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

    output_label.config(text=f"Impedance: {impedance:.2f} Ohms")

# main application window
root = tk.Tk()
root.title("Impedance Calculator")
root.geometry("500x550")

# Create a notebook (tabbed interface)
impedance_notebook = ttk.Notebook(root)
impedance_notebook.pack(fill=tk.BOTH, expand=True)

# Microstrip 0- SE tab
microstrip_se_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(microstrip_se_tab, text="Microstrip - SE")

# Microstrip - SE inputs
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

# Microstrip - Diff tab
microstrip_diff_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(microstrip_diff_tab, text="Microstrip - Diff")

# Microstrip - Diff inputs
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

# Stripline - SE tab
stripline_se_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(stripline_se_tab, text="Stripline - SE")

# Stripline - SE inputs
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

# Stripline - Diff tab
stripline_diff_tab = ttk.Frame(impedance_notebook)
impedance_notebook.add(stripline_diff_tab, text="Stripline - Diff")

# Stripline - Diff inputs
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

# "Calculate Impedance" button
calculate_button = tk.Button(root, text="Calculate Impedance", command=calculate_impedance)
calculate_button.pack(pady=20)

# output impedance
output_label = tk.Label(root, text="")
output_label.pack(pady=10)

root.mainloop()
