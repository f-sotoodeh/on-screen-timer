import tkinter as tk
from sys import argv

BG = '#fab4af'
FG = '#4d110d'

root = tk.Tk()
root.geometry('500x200+1000+700')
root.wm_attributes('-type', 'splash')
root.wm_attributes('-topmost', True)
root.config(bg=BG)
root.bind('<Double-1>', lambda e: root.destroy())

label = tk.Label(root)
label.place(x=10, y=5)
label.config(font=('Monospace', 120), bg=BG, fg=FG)
label['text'] = 'HELLO'

def countdown(seconds):
    m = seconds // 60
    s = seconds % 60
    text = ''
    if seconds > 0:
        text = f'{m:02d}:{s:02d}'
    elif seconds > -2:
        text = 'OVER!'
    else:
        root.destroy()
        exit()
    label['text'] = text
    root.after(1000, countdown, seconds-1)

if len(argv) > 1:
    n = int(argv[1])
else:
    n = int(input('? '))

countdown(n)
root.mainloop()
