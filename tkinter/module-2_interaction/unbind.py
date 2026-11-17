import tkinter as tk
from tkinter import messagebox

def switch_label():
    global label_activated
    if label_activated:
        activate_label_button.config(text='Activate label', bg='green')
        label.config(bg='white', fg='black', text='Deactivated\nClicks will do nothing')
        label.unbind('<Button-1>')
    else:
        activate_label_button.config(text='Deactivate label', bg='red')
        label.config(bg='green', fg='white', text='Activated\nClicks will open dialogue box')
        label.bind('<Button-1>', on_click_label)
    label_activated = not label_activated

def on_click_label(event=None):
    messagebox.showinfo('Message', f'You clicked the label at x: {event.x}, y: {event.y}.')

window = tk.Tk()
label_activated = False

activate_label_button = tk.Button(window, text='Activate label', height=2, bg='green', fg='white', command=switch_label)
activate_label_button.pack(fill=tk.X)
label = tk.Label(window, text='Deactivated\nClicks will do nothing', height=4, bg='white', fg='black')
label.pack(fill=tk.X)

window.mainloop()