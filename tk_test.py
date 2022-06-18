import tkinter as tk
from tkinter.messagebox import showinfo

class MyGui(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text='press', command=self.reply)
        button.pack()
    def reply(self):
        showinfo(message='text')

class MyGuiEnt(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        tk.Label(self, text='whazzup').pack()
        self.ent = tk.Entry(self)
        self.ent.pack()
        btn = tk.Button(self, text='wzzbtn', command=self.reply).pack()
        temp = 5
    def reply(self):
        #temp_2 = self.temp
        new_window = tk.Toplevel()
        wzz = self.ent.get()
        for i in range(1, 10):
            tk.Label(new_window, text=wzz * 2 * i).pack()
        new_window.tk.mainloop()

if __name__ == '__main__':
    mainwin = tk.Tk()
    tk.Label(mainwin, text=__name__).pack()
    popup = tk.Toplevel()
    tk.Label(popup, text='attach').pack()
    MyGuiEnt(popup).pack()
    mainwin.mainloop()
    #window = MyGui()
    #window.pack()
    #window.tk.mainloop()
