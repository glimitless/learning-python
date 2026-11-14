import tkinter as tk

window = tk.Tk()
window.title('Chance')
chance = tk.Button(window, text='CHANCE', bg='black', activebackground='yellow', fg='yellow', activeforeground='black')
reroll = tk.Button(window, text='REROLL', bg='black', activebackground='green', fg='green', activeforeground='black')

chance.pack(fill=tk.X)
reroll.pack(fill=tk.X)

window.mainloop()
