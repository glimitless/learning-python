import tkinter as tk
from tkinter import messagebox

def send_response():
    messagebox.showinfo('Message', 'Greetings young padawan.')

window = tk.Tk()
window.title('Greetings from the North Side.')

say_hello = tk.Button(
    window, 
    text='Say hello',
    command=send_response,
    bg='black',
    fg='green',
    activebackground='green',
    activeforeground='black'
)
say_hello.pack()

close_window = tk.Button(
    window, 
    text='Close window',
    command=window.destroy,
    bg='black',
    fg='red',
    activebackground='red',
    activeforeground='black',
)
close_window.pack()

window.mainloop()
