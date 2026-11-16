import tkinter as tk

game_state = True
def on_click():
    global game_state
    if game_state:
        computer_message.config(text='The computer says: Goodbye.')
        respond_to_message.config(text='Goodbye!', bg='red')
    else:
        computer_message.config(text='The computer says: Hello.')
        respond_to_message.config(text='Hello!', bg='green')
    game_state = not game_state

window = tk.Tk()
window.title('Chatbox Lite')

computer_message = tk.Label(text='The computer says: Hello.', height=2)
respond_to_message = tk.Button(window, text='Hello!', height=2, bg='green', fg='white', command=on_click)

computer_message.pack(fill=tk.X)
respond_to_message.pack(fill=tk.X)

window.mainloop()