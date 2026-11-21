import tkinter as tk

def change_focus():
    if window.focus_get() is chance_btn:
        reroll_btn.focus_set()
    else:
        chance_btn.focus_set()
    window.after(777, change_focus)


window = tk.Tk()
window.title('CHANCE FOREVER')
window.geometry('160x320')

chance_btn = tk.Button(window, text='CHANCE', bg='green', fg='white')
chance_btn.place(x=50, y=100)

reroll_btn = tk.Button(window, text='REROLL', bg='green', fg='white')
reroll_btn.place(x=50, y=200)
window.after(777, change_focus)

window.mainloop()