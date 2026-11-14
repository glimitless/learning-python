import tkinter as tk

window = tk.Tk()
window.title('Chance Game')
label = tk.Label(window, text='Start your chance game.')
frame = tk.Frame(window, height=20, width=20, bg='black' )
chance = tk.Button(window, text='CHANCE', bg='black', activebackground='yellow', fg='yellow', activeforeground='black')
reroll = tk.Button(window, text='REROLL', bg='black', activebackground='green', fg='green', activeforeground='black')

frame.pack()
label.pack()
chance.pack(fill=tk.X)
reroll.pack(fill=tk.X)

window.mainloop()
