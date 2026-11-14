import tkinter as tk

window = tk.Tk()
window.title('Seven')
chance = tk.Button(window, text='CHANCE')
chance.grid(column=0, row=1)
reroll = tk.Button(window, text='REROLL')
reroll.grid(column=1, row=0)
double = tk.Button(window, text='DOUBLE')
double.grid(column=2, row=1)
window.mainloop()


