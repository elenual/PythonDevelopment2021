import tkinter as tk
from random import shuffle

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for i in range(4):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        self.rowconfigure(4, weight=1)
        self.ExitButton = tk.Button(self, text='Exit', command = self.quit , background="white")
        self.ExitButton.grid(row = 0, column = 2, columnspan = 2, sticky="NSEW")
        self.NewButton = tk.Button(self, text='New', command = self.quit , background="white")
        self.NewButton.grid(row = 0, column = 0, columnspan = 2, sticky="NSEW")
        buttons = []
        numbers = list(range(15))
        shuffle(numbers)
        for i, j in enumerate(numbers):
            buttons.append(tk.Button(self, text=str(j+1)))
            buttons[-1].grid(row=i//4+1, column=i%4, sticky="SEWN")

app = Application()
app.master.title('15')
app.mainloop()