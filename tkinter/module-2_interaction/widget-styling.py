import tkinter as tk

window = tk.Tk();

fire_btn = tk.Button(window, padx=5, text='Fire', borderwidth=5)
fire_btn.pack()

ice_btn = tk.Button(window, padx=10, text='Ice', underline=2)
ice_btn.pack()

earth_button = tk.Button(window, pady=10, padx=14, text='Earth', wraplength=1)
earth_button.pack()

air_button = tk.Button(window, highlightthickness=10, highlightcolor='yellow', text='Air')
air_button.pack()
window.mainloop()