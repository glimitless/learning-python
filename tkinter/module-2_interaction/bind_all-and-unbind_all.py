import tkinter as tk
from tkinter import messagebox

def label_clicked(event=None):
    messagebox.showinfo('Message', f'You clicked the label at {event.x}, {event.y}!')

def destroy_interaction(event=None):
    window.unbind_all('<Button-1>')
    label_1.config(text='Click destroyed')
    label_2.config(text='Click destroyed')
    destroy_interaction_button.config(text='Interaction destroyed')

window = tk.Tk()

label_1 = tk.Label(window, height=4, text='Click here')
label_2 = tk.Label(window, height=4, text='Click here')
destroy_interaction_button = tk.Button(window, text='Destroy interaction')

window.bind_all('<Button-1>', label_clicked)
destroy_interaction_button.unbind('<Button-1>')
destroy_interaction_button.bind('<Button-1>', destroy_interaction)

label_1.pack(fill=tk.X)
label_2.pack(fill=tk.X)
destroy_interaction_button.pack()

window.mainloop()