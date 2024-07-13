"""
Create a simple calculator app
"""
import tkinter as tk


class Calculator(tk.Tk):

    def __init__(self):

        super().__init__()

        self.current_operation = ''

        # noinspection PyTypeChecker
        self.label = tk.Label(bg='green', text="Hi!!!", font=('Rockwell', 25, 'normal', 'underline'))
        self.label.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.2)

        self.add_button = tk.Button(self, text='add', fg='black',
                                    font=('courier new', 16, 'bold'), command=self.button_add)
        self.add_button.place(relx=0.1, rely=0.5, relwidth=0.2, relheight=0.1)

        self.subtract_button = tk.Button(self, text='subtract', fg='black',
                                         font=('courier new', 16, 'bold'), command=self.button_subtract)
        self.subtract_button.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.1)

        self.multiply_button = tk.Button(self, text='multiply', fg='blue',
                                         font=('courier new', 16, 'bold'), command=self.button_multiply)
        self.multiply_button.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1)

        self.division_button = tk.Button(self, text='divide', fg='blue',
                                         font=('courier new', 16, 'bold'), command=self.button_divide)
        self.division_button.place(relx=0.7, rely=0.5, relwidth=0.2, relheight=0.1)

        self.square_root_button = tk.Button(self, text='subtract', fg='black',
                                            font=('courier new', 16, 'bold'), command=self.button_root)
        self.square_root_button.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.1)

        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.6, relwidth=0.3, height=18)

        self.text_field2 = tk.Entry(self)
        self.text_field2.place(relx=0.4, rely=0.6, relwidth=0.3, height=18)

    def button_add(self):
        self.current_operation = 'add'
        print('add')
        print(self.current_operation)
        Calculator.update_textfile(self)

    def button_subtract(self):
        self.current_operation = 'subtract'
        Calculator.update_textfile(self)

    def button_multiply(self):
        self.current_operation = 'multiply'
        Calculator.update_textfile(self)

    def button_divide(self):
        self.current_operation = 'divide'
        Calculator.update_textfile(self)

    def button_root(self):
        self.current_operation = 'square root'
        Calculator.update_textfile(self)

    def calculate_add(self, num1, num2):
        final_res = int(num1) + int(num2)
        return final_res

    def calculate_subtract(self, num1, num2):
        final_res = int(num1) - int(num2)
        return final_res

    def calculate_multiples(self, num1, num2):
        final_res = int(num1) * int(num2)
        return final_res

    def calculate_divide(self, num1, num2):
        final_res = int(num1) / int(num2)
        return final_res

    def calculate_root(self, num1, num2):
        final_res= num1
        for i in range(num2):
            final_res /= int(num1) / int(num1)
        return final_res

    def update_textfile(self):
        text_in_text_field = self.text_field.get()
        text_in_text_field2 = self.text_field2.get()
        if self.current_operation == 'add':
            final_res = Calculator.calculate_add(self, text_in_text_field, text_in_text_field2)
            self.label.config(text=final_res)
        elif self.current_operation == 'subtract':
            final_res = Calculator.calculate_subtract(self, text_in_text_field, text_in_text_field2)
            self.label.config(text=final_res)
        elif self.current_operation == 'multiply':
            final_res = Calculator.calculate_multiples(self, text_in_text_field, text_in_text_field2)
            self.label.config(text=final_res)
        elif self.current_operation == 'divide':
            final_res = Calculator.calculate_divide(self, text_in_text_field, text_in_text_field2)
            self.label.config(text=final_res)
        elif self.current_operation == 'square root':
            final_res = Calculator.calculate_divide(self, text_in_text_field, text_in_text_field2)
            self.label.config(text=final_res)


if __name__ == '__main__':
    app = Calculator()
    app.title('Calculator')
    app.geometry('1000x800')
    app.mainloop()


# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
