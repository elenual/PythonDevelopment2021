import tkinter as tk
from random import shuffle
from tkinter import messagebox

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
        self.ExitButton.grid(row = 0, column = 2, columnspan = 2, sticky="SEWN")
        self.NewButton = tk.Button(self, text='New', command = self.new_game , background="white")
        self.NewButton.grid(row = 0, column = 0, columnspan = 2, sticky="SEWN")
        self.buttons = []
        self.numbers = list(range(15))
        shuffle(self.numbers)
        for position, number in enumerate(self.numbers):
            self.buttons.append(tk.Button(self, text=str(number+1), command = lambda x=position: self.move(x)))
            self.buttons[-1].grid(row=position//4+1, column=position%4, sticky="SEWN")
        self.empty_cell = 15
    
    def new_game(self):
        for i in self.buttons:
            i.destroy()
        self.createWidgets()

    def move(self, cell_number):
        start_row = self.buttons[cell_number].grid_info()['row']
        start_column = self.buttons[cell_number].grid_info()['column']
        new_row = self.empty_cell//4+1
        new_column = self.empty_cell%4
        if ((abs(new_row-start_row) == 1) and (new_column == start_column)) or ((abs(new_column-start_column) == 1) and (new_row == start_row)):
            self.buttons[cell_number].grid(row=new_row, column=new_column, sticky="SEWN")
            self.empty_cell = (start_row-1)*4 + start_column    
            self.check()

    def check(self):
        result = 0
        for i in range(15):
            cell_position = (self.buttons[i].grid_info()['row'] - 1) * 4 + self.buttons[i].grid_info()['column']
            result += int(str(cell_position+1) == self.buttons[i].cget('text'))
        if result == 15: 
            messagebox.showinfo('', 'You win!')
            self.new_game()



app = Application()
app.master.title('15')
app.mainloop()