import tkinter as tk

window = tk.Tk()
window.title('Chance Game')

chance_select = tk.IntVar()
chance_select.set(0)
roll_select = tk.IntVar()
roll_select.set(0)

chance = tk.Checkbutton(window, text='CHANCE', variable=chance_select)
chance.pack()

reroll = tk.Radiobutton(window, text='REROLL', variable=roll_select, value=0)
reroll.pack()

single = tk.Radiobutton(window, text='SINGLE', variable=roll_select, value=1)
single.pack()

double = tk.Radiobutton(window, text='DOUBLE', variable=roll_select, value=2)
double.pack()

triple = tk.Radiobutton(window, text='TRIPLE', variable=roll_select, value=3)
triple.pack()
window.mainloop()