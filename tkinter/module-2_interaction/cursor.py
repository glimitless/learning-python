import tkinter as tk

window = tk.Tk()
label = tk.Label(window, text="REROLL", cursor="watch")
label.pack(fill=tk.X)
button = tk.Button(window, text="CHANCE", cursor="hand2")
button.pack(fill=tk.X)
window.mainloop()