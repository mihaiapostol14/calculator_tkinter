import tkinter as tk


def insert_digits(digits):
    value = calculator_input_filed.get() + str(digits)
    if value[0]=='0':
        value=value[1:]
    calculator_input_filed.delete(0, tk.END)
    calculator_input_filed.insert(0, value+str(digits))


def clear():
    calculator_input_filed.delete(0, tk.END)
    return calculator_input_filed.insert(0, str(0))


def operation(operation):
    value = calculator_input_filed.get()
    if value[-1] in "+-/*":
        value=value[:-1]
        calculator_input_filed.delete(0, tk.END)
        calculator_input_filed.insert(0, value+operation)

def button_digits(text, row, column, font, function):
    return tk.Button(text=text, bd=5, font=font, command=function).grid(row=row, column=column, sticky="wens", padx=5,
                                                                        pady=5)


def operation_button(operation, row, column, font, function):
    return tk.Button(text=operation, bd=5, font=font, command=function).grid(row=row, column=column, sticky="wens",
                                                                             padx=5, pady=5)


def button_clear(text, row, column, font, function):
    return tk.Button(text=text, bd=5, font=font, command=function).grid(row=row, column=column, sticky="wens", padx=5,
                                                                        pady=5)


def button_clear_all(text, row, column, font, function):
    return tk.Button(text=text, bd=5, font=font, command=function).grid(row=row, column=column, sticky="wens", padx=5,
                                                                        pady=5)


main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry(f"260x270+100+200")
main_window["bg"] = "#00ffff"
main_window.resizable(False, False)

calculator_input_filed = tk.Entry(main_window, font=15, justify=tk.RIGHT, bd=5, width=22)
calculator_input_filed.insert(0, "0")
calculator_input_filed.grid(row=0, column=0, columnspan=4, sticky="we", padx=5)

button_digits(text="1", row=1, column=0, font=("Arial", 16), function=lambda: insert_digits(1))
button_digits(text="2", row=1, column=1, font=("Arial", 16), function=lambda: insert_digits(2))
button_digits(text="3", row=1, column=2, font=("Arial", 16), function=lambda: insert_digits(3))
button_digits(text="4", row=2, column=0, font=("Arial", 16), function=lambda: insert_digits(4))
button_digits(text="5", row=2, column=1, font=("Arial", 16), function=lambda: insert_digits(5))
button_digits(text="6", row=2, column=2, font=("Arial", 16), function=lambda: insert_digits(6))
button_digits(text="7", row=3, column=0, font=("Arial", 16), function=lambda: insert_digits(7))
button_digits(text="8", row=3, column=1, font=("Arial", 16), function=lambda: insert_digits(8))
button_digits(text="9", row=3, column=2, font=("Arial", 16), function=lambda: insert_digits(9))
button_digits(text="0", row=4, column=0, font=("Arial", 16), function=lambda: insert_digits(0))

operation_button(operation="+", row=1, column=3, font=("Arial", 16), function=lambda: operation("+"))
operation_button(operation="-", row=2, column=3, font=("Arial", 16), function=lambda: operation("-"))
operation_button(operation="x", row=3, column=3, font=("Arial", 16), function=lambda: operation("*"))
operation_button(operation="÷", row=4, column=3, font=("Arial", 16), function=lambda: operation("/"))

# operation_button(text="=", row=1, column=3, font=("Arial", 16), function=lambda: insert_digits("/"))

button_clear(text="C", row=4, column=1, font=("Arial", 16), function=lambda: clear())
# operation_button(text="-", row=2, column=3, font=("Arial", 16), function=lambda: insert_digits("-"))


main_window.grid_columnconfigure(0, minsize=60)
main_window.grid_columnconfigure(1, minsize=60)
main_window.grid_columnconfigure(2, minsize=60)
main_window.grid_columnconfigure(3, minsize=60)

main_window.rowconfigure(1, minsize=60)
main_window.rowconfigure(2, minsize=60)
main_window.rowconfigure(3, minsize=60)
main_window.rowconfigure(4, minsize=60)

main_window.mainloop()
