import tkinter as tk

def font_switch(font:str):
    text_display['font'] = (font, 60, 'bold')

window = tk.Tk()
window.geometry('400x400')

text_display = tk.Label(window, text='TEXT', font=('Times', '60', 'bold'))
text_display.grid(column=2, row=1, rowspan=3)

times_btn = tk.Button(window, text='Times', font=('Times', '20'), command=lambda: font_switch('Times'))
times_btn.grid(column=1, row=1)

arial_btn = tk.Button(window, text='Arial', font=('Arial', '20'), command=lambda: font_switch('Arial'))
arial_btn.grid(column=1, row=2)

calibri_btn = tk.Button(window, text='Calibri', font=('Calibri', '20'), command=lambda: font_switch('Calibri'))
calibri_btn.grid(column=1, row=3)

window.mainloop()

