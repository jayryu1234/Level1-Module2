"""
Photo Quiz: Ask a question about a photo and guess the answer!
"""
import tkinter as tk
from tkinter import simpledialog, messagebox

from PIL import Image, ImageTk


def create_image(filename, width, height):
    image_obj = None

    try:
        image = Image.open(filename)
        image = image.resize((width, height), Image.ANTIALIAS)
        image_obj = ImageTk.PhotoImage(image=image)
    except FileNotFoundError as fnf:
        print("ERROR: Unable to find file " + filename)

    return image_obj

# ======================= DO NOT EDIT THE CODE ABOVE =========================

# TODO 0) Find at least 3 interesting photos (2 are provided if you want
#  to use those)

# TODO 1) Create a new tkinter class


class Picture:

    def __init__(self):

        # TODO 2) Create a constructor

        # TODO 3) call Tk's constructor
        super().__init__()
        # TODO 4) Create a member variable for a label and place it.
        #  You do not need to add any text or images to the label.
        self.label = tk.Label(self, text="Welcome!!!", bg='yellow',
                              fg='blue', font=('arial', 32, 'bold'), relief='solid')


class MyDialog:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)

        tk.Label(top, text="Value").pack()

        self.e = tk.Entry(top)
        self.e.pack(padx=5)

        b = tk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        print("value is", self.e.get())
        self.top.destroy()

root = tk()
d = MyDialog(root)

root.wait_window(d.top)


# TODO 5) Create an if __name__ == '__main__': block


if __name__ == '__main__':

    # TODO 6) Create an object of the tkinter class

    picture = Picture()

    # TODO 7) Set the app window width and height using geometry()

    picture.geometry('800x800')

    # TODO 8) Declare and initialize a score variable

    score = 0

    # TODO 9) Create an image object variable using the create_image function
    #  above and store it in a variable

    img = create_image('carrots.png', width=0.2, height=0.1)

    # TODO 10) Set the image onto the class's label using the configure method,
    #  for example:
    #  app.photo_label.configure(image=image_object)

    picture.label.configure(image='fossil.png')

    # TODO 11) Use a pop-up (simpledialog) to ask the user a question
    #  relating to the image and tell them if they get the right answer.



    # TODO 12) If the answer is correct, increase the score by 1

    # TODO 13) Repeat the steps to show a different photo and ask a different
    #  question

    # TODO 14) Display the score to the user after asking the last question
