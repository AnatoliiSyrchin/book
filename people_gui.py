from tkinter import *
from tkinter import messagebox
import shelve
shelvename = 'shelve-persone'
fildnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global enteries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    enteries = {}
    for (ix, label) in enumerate(('key',) + fildnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        enteries[label] = ent
    Button(window, text='Fetch', comand=fetch_record).pack(side=LEFT)
    Button(window, text='Update', comand=update_record).pack(side=LEFT)
    Button(window, text='Quit', comand=window.quit).pack(side=RIGHT)
    return window


def fetch_record():
    key = enteries['key'].get()
    try:
        record = db['key']
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            enteries[field].delete(0, END)
            enteries[field].insert(0, repr(getattr(record, field)))

def update_record():
    key = enteries['key'].get()
    if key in db:
        record = db['key']
    else:
        from person import Person
        record = Person(name='?', age='?')

    for field in fieldnames:
        setattr(record, field, eval(enteries[field].get()))

    db[key] = record


db = shelve.open(shelvename)
window = make_widgets()
window.mainloop()
db.close()
