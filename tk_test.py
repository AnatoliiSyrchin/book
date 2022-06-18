"""Nothing interesting. It's a test module"""

import tkinter as tk
from tkinter.messagebox import showinfo


class MyGui(tk.Frame):
    """gui without entry"""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text='press', command=self.reply)
        button.pack()

    @staticmethod
    def reply():
        """show window with message"""
        showinfo(message='text')


class MyGuiEnt(tk.Frame):
    """gui with entry"""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='whazzup').pack()
        self.ent = tk.Entry(self)
        self.ent.pack()
        btn = tk.Button(self, text='wzzbtn', command=self.reply)
        btn.pack()

    def reply(self):
        """show window with message from entry"""
        new_window = tk.Toplevel()
        wzz = self.ent.get()
        for i in range(1, 10):
            tk.Label(new_window, text=wzz * 2 * i).pack()
        new_window.tk.mainloop()


if __name__ == '__main__':
    main_win = tk.Tk()
    tk.Label(main_win, text=__name__).pack()
    popup = tk.Toplevel()
    tk.Label(popup, text='attach').pack()
    MyGuiEnt(popup).pack()
    main_win.mainloop()
