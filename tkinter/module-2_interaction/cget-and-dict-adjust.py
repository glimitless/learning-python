import tkinter as tk

def switch():
    on_button['text'] = 'OFF' if on_button['text'] == 'ON' else 'ON'

window = tk.Tk()

on_button = tk.Button(window, text='ON', command=switch)
on_button.place(x=50, y=100, width=100)
print_button = tk.Button(window, text='PRINT', command=lambda: print(on_button.cget('text')))
print_button.place(x=50, y=50, width=100)

window.mainloop()