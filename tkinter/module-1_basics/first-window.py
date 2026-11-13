import tkinter as tk
from tkinter import messagebox

def close_window(): 
    response = messagebox.askquestion('Question', 'Do you really want to?')
    if response == 'yes':
        window.destroy()

window = tk.Tk()
window.title('Imageworks2D')
button = tk.Button(window, text='Close', command=close_window)
button.place(x=7, y=7, width=140, height=45)
window.mainloop()