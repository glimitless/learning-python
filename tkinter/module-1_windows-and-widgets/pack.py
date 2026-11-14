import tkinter as tk

window = tk.Tk()
chance = tk.Button(window, text='CHANCE')
reroll = tk.Button(window, text='REROLL')
chance.pack(side=tk.TOP, fill=tk.X)
reroll.pack(side=tk.TOP, fill=tk.X)
window.mainloop()