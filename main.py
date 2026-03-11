# import (module)tkinter for creating GUI(graphical user interface) apps
# module - single file in which functions , classes or variables
# library means collection of module
import tkinter as tk
# Import submodule filedialog for open/save dialogs and submodule messagebox for popups
from tkinter import filedialog, messagebox

# -------------------- MAIN WINDOW --------------------
# Create main application window
root = tk.Tk()

# Set window title
root.title("Text Editor")

# Set window size
root.geometry("800x600")

# -------------------- TEXT EDITOR AREA --------------------

# create text editor area
text=tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12)
)
# Make text area fill the entire window
text.pack(expand=True, fill=tk.BOTH)

# -------------------- FILE FUNCTIONS --------------------

# function1 to create a new file (clear all text)
def new_file():
    # Delete all text from the text box (from start to end)
    text.delete(1.0, tk.END)

# function2 to open a existing text file
def open_file():
    # Open file dialog to select a text file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    # Check if a file is selected
    if file_path:
        # Open the selected file in read mode
        with open(file_path, "r")as file:
            # clear old text
            text.delete(1.0, tk.END)
            # Insert file content into the text editor
            text.insert(tk.END, file.read())

# function3 to save the current text to a file
def save_file():
    # open save file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    # Check if file path is selected
    if file_path:
        # Open file in write mode
        with open(file_path, "w")as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully!")

# -------------------- MENU BAR --------------------

# create menu bar
menu = tk.Menu(root)

# Attach menu bar to the window
root.config(menu=menu)

# Create File menu
# Dropdown under File which has options like New, Open, Save, Exit
file_menu = tk.Menu(menu)


# add file menu to menu bar
menu.add_cascade(label="File", menu = file_menu)

# Add New option to File menu
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
# Add Open option to File menu
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
# Add Save option to File menu
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
# Add a separator line in menu
file_menu.add_separator()
# Add Exit option to close the application
file_menu.add_command(label="Exit", command=root.quit)


# Shortcut Binding
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())


# -------------------- RUN APPLICATION --------------------

# Run the application continuously
# Starts and keeps the window open

root.mainloop()