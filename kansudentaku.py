import tkinter as tk
import math

# 関数電卓のクラス
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("関数電卓")
        self.root.geometry("400x600")
        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.input_field = self.create_input_field()
        self.buttons_frame = self.create_buttons_frame()

        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root, height=50, bd=0, bg="light gray")
        frame.pack(side=tk.TOP)
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=0, bg="white", justify=tk.RIGHT)
        input_field.grid(row=0, column=0, ipady=10)
        return input_field

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack()
        return frame

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '÷', '√',
            '4', '5', '6', '×', '^',
            '1', '2', '3', '-', 'C',
            '0', '.', '=', '+', 'π'
        ]

        row_val = 0
        col_val = 0

        for button in buttons:
            command = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=8, height=3, bd=0, bg="white", cursor="hand2", command=command).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = self.expression.replace('×', '*').replace('÷', '/').replace('√', 'math.sqrt').replace('^', '**').replace('π', 'math.pi')
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("エラー")
                self.expression = ""
        elif char == 'C':
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
