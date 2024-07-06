"""
Create a simple calculator app
"""
import tkinter as tk


class Calculator:

    def __init__(self):
        self.current_operation = ''

        self.label = tk.Label(self, bg='green', font=('Rockwell', 25, 'normal', 'underline'))
        self.label.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.3)

        self.add_button = tk.Button(self, text='add', fg='black',
                                    font=('courier new', 16, 'bold'), command=self.button_add)
        self.add_button.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.2)

        self.subtract_button = tk.Button(self, text='subtract', fg='black',
                                         font=('courier new', 16, 'bold'), command=self.button_subtract)
        self.subtract_button.place(relx=0.3, rely=0.5, relwidth=0.8, relheight=0.2)

        self.multiply_button = tk.Button(self, text='multiply', fg='blue',
                                         font=('courier new', 16, 'bold'), command=self.button_multiply)
        self.multiply_button.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.2)

        self.division_button = tk.Button(self, text='divide', fg='blue',
                                         font=('courier new', 16, 'bold'), command=self.button_divide)
        self.division_button_button.place(relx=0.7, rely=0.5, relwidth=0.8, relheight=0.2)

        self.text_field = tk.Entry(self)
        self.text_field.place(relx=0.1, rely=0.6, relwidth=0.8, height=18)

        self.text_field2 = tk.Entry(self)
        self.text_field2.place(relx=0.3, rely=0.6, relwidth=0.8, height=18)

    def button_add(self):
        self.current_operation = 'add'

    def button_subtract(self):
        self.current_operation = 'subtract'

    def button_multiply(self):
        self.current_operation = 'multiply'

    def button_divide(self):
        self.current_operation = 'divide'

    def update_textfile(self):
        pass

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label
