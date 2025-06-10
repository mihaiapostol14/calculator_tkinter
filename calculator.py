import customtkinter as ctk
from tkinter.messagebox import showinfo

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("320x420")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.configure(bg="#f5f6fa")
        self.resizable(False, False)
        self.iconbitmap(bitmap='calculator.ico')

        # Entry field
        self.entry_var = ctk.StringVar(value="0")
        self.entry = ctk.CTkEntry(
            self,
            textvariable=self.entry_var,
            font=("Arial", 28),
            width=280,
            height=60,
            corner_radius=10,
            fg_color="#f5f6fa",
            bg_color="#f5f6fa",
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=20, pady=(20, 10), sticky="nsew")

        # Button frame
        btn_frame = ctk.CTkFrame(self, fg_color="#dff9fb", corner_radius=15)
        btn_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

        self.create_buttons(btn_frame)
        self.bind('<Key>', self.press_key)

    def create_buttons(self, frame):
        btn_cfg = {"width": 60, "height": 60, "corner_radius": 10, "font": ("Arial", 20)}
        digits = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        for (text, r, c) in digits:
            if text.isdigit():
                cmd = lambda x=text: self.add_digit(x)
                color = "#2c9bf6"
            elif text in "+-*/":
                cmd = lambda x=text: self.add_operation(x)
                color = "#686de0"
            elif text == "C":
                cmd = self.clear
                color = "#eb4d4b"
            else:  # '='
                cmd = self.calculate
                color = "#6ab04c"
            b = ctk.CTkButton(
                frame, text=text, command=cmd, fg_color=color, hover_color="#4be682", **btn_cfg
            )
            b.grid(row=r, column=c, padx=8, pady=8, sticky="nsew")

        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(1, 5):
            frame.grid_rowconfigure(i, weight=1)

    def add_digit(self, digit):
        value = self.entry_var.get()
        if value == "0":
            value = digit
        else:
            value += digit
        self.entry_var.set(value)

    def add_operation(self, op):
        value = self.entry_var.get()
        if value[-1] in "+-*/":
            value = value[:-1]
        self.entry_var.set(value + op)

    def clear(self):
        self.entry_var.set("0")

    def calculate(self):
        value = self.entry_var.get()
        try:
            if value[-1] in "+-*/":
                value = value[:-1]
            result = eval(value)
            self.entry_var.set(str(result))
        except Exception:
            showinfo("ERROR", "Invalid Input")
            self.entry_var.set("0")

    def press_key(self, event):
        if event.char.isdigit():
            self.add_digit(event.char)
        elif event.char in "+-*/":
            self.add_operation(event.char)
        elif event.char == "\r":
            self.calculate()
        elif event.char.lower() == 'c':
            self.clear()

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()