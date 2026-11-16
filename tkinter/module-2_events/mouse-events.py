import tkinter as tk
from tkinter import messagebox

def on_click(event=None):
    title = 'Message'
    if event is None:
        messagebox.showinfo(title, 'This widget is clickable.')
    else:
        message = f'You clicked with mouse button {event.num}, at coordinates {event.x}, {event.y}.'
        messagebox.showinfo(title, message)
        
window = tk.Tk()
label = tk.Label(window, text='Click Button Below', height=2)
button = tk.Button(
    window,
    command=on_click, 
    text='Click Here', 
    height=2, 
    bg='green', 
    activebackground='white', 
    fg='white', 
    activeforeground='green'
)
button.bind('<Button-1>', on_click)
label.pack(fill=tk.X)
button.pack(fill=tk.X)

window.mainloop()