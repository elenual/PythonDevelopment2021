import tkinter as tk

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
        buttons = []
        for i in range (15):
            buttons.append(tk.Button(self, text=str(i+1)))
            buttons[-1].grid(row=i//4, column=i%4, sticky="SEWN")

app = Application()
app.master.title('App')
app.mainloop()