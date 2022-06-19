from tkinter import *
from functools import partial
from tkinter import messagebox
import shelve


shelve_name = 'shelve-persone'
fieldnames = ('name', 'age', 'pay', 'job')


def make_widgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetch_record).pack(side=LEFT)
    Button(window, text='Update', command=update_record).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    Button(window, text='Show All', command=show_all).pack(side=RIGHT)
    return window


def fetch_record():
    key = entries['key'].get()
    try:
        record = db[key]
    except KeyError:
        messagebox.showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update_record():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from person import Person
        record = Person(name='?', age='?')

    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))

    db[key] = record

def show_all():
    show_all_window = Tk()
    for num, i in enumerate(db):
        Label(show_all_window, text='key: ' + i + '....').grid(row=num, column=0)
        for num1, field in enumerate(fieldnames):
            one_str = repr(getattr(db[i], field))
            Label(show_all_window, text=field + ': ' + one_str).grid(row=num, column=num1 + 1)
        Button(show_all_window, text='Delete' + i, command=partial(del_from_db, i)).grid(row=num, column=num1 + 2)
    show_all_window.mainloop()

def del_from_db(key):
    del db[key]

db = shelve.open(shelve_name)
window = make_widgets()
window.mainloop()
db.close()
