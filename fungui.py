from tkinter import *
import random
fontsize = 30
colors = ['red', 'green', 'blue', 'yellow']


def on_spam():
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack(fill=BOTH)
    main_label.config(fg=color)

def on_flip():
    main_label.config(fg=random.choice(colors))
    main.after(250, on_flip)

def on_grow():
    global fontsize
    fontsize += 5
    main_label.config(font=('arial', fontsize, 'italic'))
    main.after(100, on_grow)


main = Tk()
main_label = Label(main, text='Fun Gui', relief=RAISED)
main_label.config(font=('arial', fontsize, 'italic'), fg='cyan', bg='navy')
main_label.pack(side=TOP, expand=YES, fill=BOTH)
Button(main, text='spam', command=on_spam).pack(fill=X)
Button(main, text='flip', command=on_flip).pack(fill=X)
Button(main, text='grow', command=on_grow).pack(fill=X)
main.mainloop()
