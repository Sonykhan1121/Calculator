from tkinter import *


class Calculator:
    def __init__(self, master):
        master.title("Calculator")
        window_width = 520
        window_height = 550

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        master.geometry(str(window_width)+"x"+str(window_height)+"+"+str(x)+"+"+str(y))
        master.config(bg='gray')
        master.resizable(False, False)
        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=25, bg='#ccddff', font=('Arial Bold', 30), textvariable=self.equation).grid(row=0, column=0, columnspan=5)
        padx_value = 5  # Adjust this value to change the gap between columns
        pady_value = 5  # Adjust this value to change the gap between rows

        Button(width=11, height=5, text='(', relief='flat', bg='white', command=lambda: self.show('(')).grid(row=1, column=0, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text=')', relief='flat', bg='white', command=lambda: self.show(')')).grid(row=1, column=1, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='%', relief='flat', bg='white', command=lambda: self.show('%')).grid(row=1, column=2, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='1', relief='flat', bg='white', command=lambda: self.show(1)).grid(row=2, column=0, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='2', relief='flat', bg='white', command=lambda: self.show(2)).grid(row=2, column=1, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='3', relief='flat', bg='white', command=lambda: self.show(3)).grid(row=2, column=2, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='4', relief='flat', bg='white', command=lambda: self.show(4)).grid(row=3, column=0, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='5', relief='flat', bg='white', command=lambda: self.show(5)).grid(row=3, column=1, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='6', relief='flat', bg='white', command=lambda: self.show(6)).grid(row=3, column=2, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='7', relief='flat', bg='white', command=lambda: self.show(7)).grid(row=4, column=0, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='8', relief='flat', bg='white', command=lambda: self.show(8)).grid(row=4, column=2, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='9', relief='flat', bg='white', command=lambda: self.show(9)).grid(row=4, column=1, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='0', relief='flat', bg='white', command=lambda: self.show(0)).grid(row=5, column=1, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='.', relief='flat', bg='white', command=lambda: self.show('.')).grid(row=5, column=2, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='+', relief='flat', bg='white', command=lambda: self.show('+')).grid(row=2, column=3, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='-', relief='flat', bg='white', command=lambda: self.show('-')).grid(row=3, column=3, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='/', relief='flat', bg='white', command=lambda: self.show('/')).grid(row=1, column=3, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='*', relief='flat', bg='white', command=lambda: self.show('*')).grid(row=4, column=3, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='=', relief='flat', bg='white', command=self.solve).grid(row=5, column=3, padx=padx_value, pady=pady_value)
        Button(width=11, height=5, text='C', relief='flat', bg='white', command=self.clear).grid(row=5, column=0, padx=padx_value, pady=pady_value)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)


root = Tk()
calculator = Calculator(root)
root.mainloop()
