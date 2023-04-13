import tkinter as tk
# import main

# the notes here are to print the results from main.py but idk how :'D
def show_text():
    note_label.config(text="Note 1\tNote 2\tNote 3\tNote 4\tNote 5")

# Create the main window
root = tk.Tk()
root.title("Music Tuner")
root.geometry("900x450")

# Create the calculate button
title_label = tk.Label(root, text="MUSIC NOTE DETECTION\n\n\n\n")
title_label.pack()

note_label = tk.Label(root, text="")
note_label.pack()

space_label = tk.Label(root, text="\n\n\n")
space_label.pack()

record_label = tk.Button(root, text="Start Recording", command=show_text)
record_label.pack(pady=30)

exit_label = tk.Button(root, text="Exit", command=lambda: root.quit())
exit_label.pack()

# Start the main loop
root.mainloop()
