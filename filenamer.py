import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

def natural_key(s):
    """
    Generate a key for natural sorting of strings.
    Splits the string into a list where numeric parts are converted to integers.
    """
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

class FileRenamerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Renamer")
        self.geometry("600x500")
        self.selected_dir = None
        self.files_sorted = []  # To store sorted file names
        self.create_widgets()

    def create_widgets(self):
        # Frame for directory selection
        dir_frame = tk.Frame(self)
        dir_frame.pack(pady=10)
        self.dir_label = tk.Label(dir_frame, text="No directory selected", width=50, anchor="w")
        self.dir_label.pack(side=tk.LEFT, padx=5)
        select_btn = tk.Button(dir_frame, text="Select Directory", command=self.select_directory)
        select_btn.pack(side=tk.LEFT, padx=5)

        # Frame for file order preview
        preview_frame = tk.Frame(self)
        preview_frame.pack(pady=10, fill=tk.X)
        self.preview_label = tk.Label(preview_frame, text="File order preview will appear here after selecting a directory.", anchor="w")
        self.preview_label.pack(padx=5)

        # Frame for the text area (enter new file names)
        text_frame = tk.Frame(self)
        text_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        instructions = "Note: Files are sorted (alphabetically and numerically) before renaming. Contact Sean for assistance."
        instr_label = tk.Label(text_frame, text=instructions, fg="blue")
        instr_label.pack(anchor="w", padx=5)
        text_label = tk.Label(text_frame, text="Enter new file base names (one per line):")
        text_label.pack(anchor="w", padx=5, pady=(5, 0))
        self.text_area = tk.Text(text_frame, height=10)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Button to execute renaming
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        rename_btn = tk.Button(btn_frame, text="Rename Files", command=self.rename_files)
        rename_btn.pack()

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.selected_dir = directory
            self.dir_label.config(text=directory)

            # Load and sort files using natural sorting (ignoring subdirectories)
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            files.sort(key=natural_key)
            self.files_sorted = files

            # Prepare preview text for first, second, and last file names
            preview_text = ""
            if not files:
                preview_text = "No files found in the selected directory."
            else:
                preview_text = f"Sorted order preview:\nFirst file: {files[0]}"
                if len(files) >= 2:
                    preview_text += f"\nSecond file: {files[1]}"
                if len(files) >= 3:
                    preview_text += f"\nLast file: {files[-1]}"
                elif len(files) == 2:
                    preview_text += f"\nLast file: {files[-1]}"
            self.preview_label.config(text=preview_text)

    def rename_files(self):
        if not self.selected_dir:
            messagebox.showerror("Error", "Please select a directory first.")
            return

        # Read the new file names (ignoring blank lines)
        new_names = [line.strip() for line in self.text_area.get("1.0", tk.END).splitlines() if line.strip()]
        if not new_names:
            messagebox.showerror("Error", "Please enter at least one new file name.")
            return

        files = self.files_sorted
        if len(new_names) != len(files):
            messagebox.showerror("Error", f"Number of new file names ({len(new_names)}) does not match number of files ({len(files)}).")
            return

        # Attempt to rename each file, preserving original extension
        for old_name, new_name in zip(files, new_names):
            old_path = os.path.join(self.selected_dir, old_name)
            # Get the original file's extension
            _, ext = os.path.splitext(old_name)
            # Use only the base part of the new name provided by the user
            new_base = os.path.splitext(new_name)[0]
            new_filename = new_base + ext
            new_path = os.path.join(self.selected_dir, new_filename)
            try:
                os.rename(old_path, new_path)
            except Exception as e:
                messagebox.showerror("Error", f"Error renaming '{old_name}' to '{new_filename}': {str(e)}")
                return

        messagebox.showinfo("Success", "Files renamed successfully!")
        # Optionally, refresh the preview after renaming
        self.select_directory()

if __name__ == "__main__":
    app = FileRenamerApp()
    app.mainloop()
