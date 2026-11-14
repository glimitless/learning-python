import tkinter as tk

def toggle_edit_mode():
    print('Edit value set to:', edit_value.get())

window = tk.Tk()
window.title('Imageworks2D')

edit_value = tk.IntVar()
edit_value.set(1)

edit_mode_button = tk.Checkbutton(window, text='EDIT', variable=edit_value, command=toggle_edit_mode)
edit_mode_button.pack()
window.mainloop()
