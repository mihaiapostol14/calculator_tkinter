import tkinter as tk


def add_digits(digit):
    value = calculator_input_filed.get()+str(digit)
    if value[0] =='0':
        value=value[1:]
    calculator_input_filed.delete(0, tk.END)
    calculator_input_filed.insert(0,value+digit)


def add_operation(operation):
    value = calculator_input_filed.get()
    if value[-1] =='+-*/':
        value=value[:-1]
    calculator_input_filed.delete(0, tk.END)
    calculator_input_filed.insert(0, value+operation)

    if value[0] =='0':
        value=value[:-1]
        calculator_input_filed.insert(0,value)

def make_button_digits(digit):
    return tk.Button(text=digit,bd=5, font=('Arial', 14), command=lambda: add_digits(digit))


def make_button_operation(operation):
    return tk.Button(text=operation,bd=5, font=('Arial', 14), command=lambda: add_digits(operation))


main_window = tk.Tk()
main_window.title('Calculator')
main_window.geometry('270x280+100+200')
main_window['bg'] = '#00ffff'
main_window.resizable(False, False)

calculator_input_filed = tk.Entry(main_window, bd=5,font=('Arial', 16), justify=tk.RIGHT)
calculator_input_filed.insert(0, '0')
calculator_input_filed.grid(row=0, column=0, columnspan=4, sticky="we", padx=5)

make_button_digits(digit=1).grid(row=1,column=0,sticky="wens",padx=5,pady=5)
make_button_digits(digit=2).grid(row=1,column=1,sticky="wens",padx=5,pady=5)
make_button_digits(digit=3).grid(row=1,column=2,sticky="wens",padx=5,pady=5)
make_button_digits(digit=4).grid(row=2,column=0,sticky="wens",padx=5,pady=5)
make_button_digits(digit=5).grid(row=2,column=1,sticky="wens",padx=5,pady=5)
make_button_digits(digit=6).grid(row=2,column=2,sticky="wens",padx=5,pady=5)
make_button_digits(digit=7).grid(row=3,column=0,sticky="wens",padx=5,pady=5)
make_button_digits(digit=8).grid(row=3,column=1,sticky="wens",padx=5,pady=5)
make_button_digits(digit=9).grid(row=3,column=2,sticky="wens",padx=5,pady=5)
make_button_digits(digit=0).grid(row=4,column=0,sticky="wens",padx=5,pady=5)

make_button_operation(operation='+').grid(row=1,column=3,sticky="wens",padx=5,pady=5)
make_button_operation(operation='-').grid(row=2,column=3,sticky="wens",padx=5,pady=5)
make_button_operation(operation='*').grid(row=3,column=3,sticky="wens",padx=5,pady=5)
make_button_operation(operation='/').grid(row=4,column=3,sticky="wens",padx=5,pady=5)

main_window.columnconfigure(0,minsize=60)
main_window.columnconfigure(1,minsize=60)
main_window.columnconfigure(2,minsize=60)
main_window.columnconfigure(3,minsize=60)

main_window.rowconfigure(1,minsize=60)
main_window.rowconfigure(2,minsize=60)
main_window.rowconfigure(3,minsize=60)
main_window.rowconfigure(4,minsize=60)

main_window.mainloop()
