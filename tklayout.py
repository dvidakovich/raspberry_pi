import tkinter as tk

###############################################################################
# Grid layout example

# Create the main window (grid layout)
root = tk.Tk()
root.title("Grid")

# Create widgets
label_grid_1 = tk.Label(root, text="Widget 1", bg='red')
label_grid_2 = tk.Label(root, text="Widget 2", bg='green')
label_grid_3 = tk.Label(root, text="Widget 3", bg='blue')

# Lay out widgets in a grid
label_grid_1.grid(row=0, column=2)
label_grid_2.grid(row=1, column=1)
label_grid_3.grid(row=2, column=0)

###############################################################################
# Pack layout example

# Create another window for pack layout
window_pack = tk.Toplevel()
window_pack.title("Pack")

# Create widgets
label_pack_1 = tk.Label(window_pack, text="Widget 1", bg='red')
label_pack_2 = tk.Label(window_pack, text="Widget 2", bg='green')
label_pack_3 = tk.Label(window_pack, text="Widget 3", bg='blue')

# Lay out widgets with pack
label_pack_1.pack()
label_pack_2.pack()
label_pack_3.pack()

###############################################################################
# Place layout example

# Create another window for pack layout
window_place = tk.Toplevel()
window_place.title("Place")

# Create widgets
label_place_1 = tk.Label(window_place, text="Widget 1", bg='red')
label_place_2 = tk.Label(window_place, text="Widget 2", bg='green')
label_place_3 = tk.Label(window_place, text="Widget 3", bg='blue')

# Lay out widgets with pack
label_place_1.place(relx=0, rely=0.1)
label_place_2.place(relx=0.1, rely=0.2)
label_place_3.place(relx=0.7, rely=0.6)

###############################################################################
# Run!

root.mainloop()
