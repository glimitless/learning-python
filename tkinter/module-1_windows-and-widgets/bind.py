import tkinter as tk
from tkinter import messagebox

def on_click(event=None):
    messagebox.showinfo('Message', 'Wassup my g.')

window = tk.Tk()
frame = tk.Frame(window, width=70, height=45, bg='blue')
frame.bind('<Button-1>', on_click)
frame.pack()

window.mainloop()
