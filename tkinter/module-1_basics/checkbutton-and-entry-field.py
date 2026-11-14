import tkinter as tk

def toggle_edit_mode():
    print('Edit value set to:', edit_value.get())
def clear_entry():
    edit_entry.delete(0, tk.END)

window = tk.Tk()
window.title('Imageworks2D')

edit_value = tk.IntVar()
edit_value.set(1)
edit_entry = tk.Entry(window, width=70)
edit_submit = tk.Button(
    window, 
    text='SUBMIT',
    width=45,  
    bg='black',
    activebackground='green', 
    fg='green',
    activeforeground='black',
    command=clear_entry
)

edit_mode_button = tk.Checkbutton(window, text='EDIT', variable=edit_value, command=toggle_edit_mode)
edit_mode_button.pack()
edit_entry.pack()
edit_submit.pack()
window.mainloop()