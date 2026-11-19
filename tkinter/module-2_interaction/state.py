import tkinter as tk
from tkinter import messagebox
import random

def chance_click():
    if reroll_btn['state'] == tk.DISABLED:
        chance_btn.config(bg='red3', text='END CHANCE')
        reroll_btn.config(bg='green', fg='white', state=tk.NORMAL)
        reroll_btn.bind('<Enter>', enabled_btn_hover)
        reroll_btn.bind('<Leave>', enabled_btn_release)
        chance_roll()
        
    else:
        reroll_btn.config(bg='gray60', fg='black', state=tk.DISABLED)
        chance_btn.config(bg='green', text='CHANCE')
        reroll_btn.unbind('<Enter>')
        reroll_btn.unbind('<Leave>')
        
        

def chance_roll():
    roll_1 = random.randint(1, 10)
    roll_2 = random.randint(1, 10)
    roll_3 = random.randint(1, 10)

    message = f'JACKPOT!!!\nYou rolled {roll_1}, {roll_2}, {roll_3}' if (roll_1 == roll_2 and roll_2 == roll_3) else f'Better luck next time\nYou rolled {roll_1}, {roll_2}, {roll_3}'
    messagebox.showinfo('Result', message)

def reroll_click():
    chance_roll()

def enabled_btn_hover(event:tk.Event):
    if(reroll_btn['state'] == tk.NORMAL and (event.widget.cget('text') == 'END CHANCE' or event.widget.cget('text') == 'CHANCE')):
        event.widget.config(bg='red3')
    else:
        event.widget.config(bg='green4')

def enabled_btn_release(event:tk.Event):
    if(reroll_btn['state'] == tk.NORMAL and (event.widget.cget('text') == 'END CHANCE' or event.widget.cget('text') == 'CHANCE')):
        event.widget.config(bg='red4')
    else:
        event.widget.config(bg='green')

window = tk.Tk()

chance_btn = tk.Button(window, text='CHANCE', bg='green', fg='white', command=chance_click)
chance_btn.bind('<Enter>', enabled_btn_hover)
chance_btn.bind('<Leave>', enabled_btn_release)
reroll_btn = tk.Button(window, text='REROLL', bg='gray60', fg='black', state=tk.DISABLED, command=reroll_click)


chance_btn.pack(fill=tk.X)
reroll_btn.pack(fill=tk.X)
window.mainloop()