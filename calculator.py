from tkinter import *


class Window(Frame):
    def __init__(self, window):
        super().__init__(window)

        self.calculator_input_filed = Entry(window, bd=5, font=('Arial', 16), justify=RIGHT)
        self.calculator_input_filed.insert(0, '0')
        self.calculator_input_filed.grid(row=0, column=0, columnspan=4, sticky="we", padx=5)
        self.buttons()



    def add_digits(self, digit):
        self.value = self.calculator_input_filed.get() + str(digit)
        if self.value[0] == '0':
            self.value = self.value[1:]
        self.calculator_input_filed.delete(0, END)
        self.calculator_input_filed.insert(0, self.value + digit)

    def add_operation(self,operation):
        self.value = self.calculator_input_filed.get()
        if  self.value[-1] == '+-*/':
            self.value =  self.value[:-1]
        self.calculator_input_filed.delete(0, END)
        self.calculator_input_filed.insert(0,  self.value + operation)

        if  self.value[0] == '0':
            self.value =  self.value[:-1]
            self.calculator_input_filed.insert(0,  self.value)


    def make_button_digits(self,digit):
        return Button(text=digit, bd=5, font=('Arial', 14), command=lambda: self.add_digits(digit))

    def make_button_operation(self,operation):
        return Button(text=operation, bd=5, font=('Arial', 14), command=lambda: self.add_digits(operation))

    def buttons(self):

        self.make_button_digits(digit=1).grid(row=1, column=0, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=2).grid(row=1, column=1, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=3).grid(row=1, column=2, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=4).grid(row=2, column=0, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=5).grid(row=2, column=1, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=6).grid(row=2, column=2, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=7).grid(row=3, column=0, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=8).grid(row=3, column=1, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=9).grid(row=3, column=2, sticky="wens", padx=5, pady=5)
        self.make_button_digits(digit=0).grid(row=4, column=0, sticky="wens", padx=5, pady=5)

        self.make_button_operation(operation='+').grid(row=1, column=3, sticky="wens", padx=5, pady=5)
        self.make_button_operation(operation='-').grid(row=2, column=3, sticky="wens", padx=5, pady=5)
        self.make_button_operation(operation='*').grid(row=3, column=3, sticky="wens", padx=5, pady=5)
        self.make_button_operation(operation='/').grid(row=4, column=3, sticky="wens", padx=5, pady=5)


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title('Calculator')
        self.geometry('270x280+100+200')
        self['bg'] = '#00ffff'
        self.resizable(False, False)

        self.columnconfigure(0, minsize=60)
        self.columnconfigure(1, minsize=60)
        self.columnconfigure(2, minsize=60)
        self.columnconfigure(3, minsize=60)

        self.rowconfigure(1, minsize=60)
        self.rowconfigure(2, minsize=60)
        self.rowconfigure(3, minsize=60)
        self.rowconfigure(4, minsize=60)

if __name__ == '__main__':
    app = App()
    window = Window(app)
    app.mainloop()
