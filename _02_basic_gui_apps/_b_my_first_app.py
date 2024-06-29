"""
My first Python app using Tkinter
"""
import tkinter as tk
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


# TODO 1) Make a new class and put tk.Tk in the parenthesis, for example:
#  FirstApp(tk.TK):
class FirstApp(tk.Tk):
    # TODO 2) Make a constructor
    def __init__(self):
        super().__init__()
        # TODO 3) Call the Tk class's constructor
        #  super().__init__()

        # TODO 4) Add a text label and pick a text message to display

        self.label = tk.Label(self, text="Hi!!!", bg='gold',
                              fg='blue', font=('Serif', 35, 'bold'), relief='solid')

        # TODO 5) Place the label somewhere on your app. You can use either
        #  x and y or relx and rely
        self.label.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

        # TODO 6) Create a member variable for the image using the
        #  create_image function. You can use the image provided in this
        #  folder or another image from the internet

        self.img = create_image('python.png', 200, 200)
        # self.label_image = tk.Label(self, image=self.img)

        # TODO 7) Create another label and attach to it the image object
        #  from the previous step

        self.other_label = tk.Label(self, text="Hi!!!", bg='gold', fg='blue', font=('Serif', 35, 'bold'), relief='solid')

        # TODO 8) Place the label somewhere on your app


# TODO 9) Create an if __name__ == '__main__': block

    # TODO 10) Create an object of your app class

    # TODO 11) Use the app object to set a title

    # TODO 12) Use the app object to set the window dimensions (width x height)

    # TODO 13) Run the app object's mainloop() method

