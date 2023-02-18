import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My GUI")

# Create label widget first
label = tk.Label(root, text="Hello, World!")

# And then lay out label using the pack() geometry manager
label.pack()

# Run it forever
root.mainloop()
