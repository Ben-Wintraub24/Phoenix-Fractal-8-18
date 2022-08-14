from tkinter import Tk, Label
from PIL import ImageTk


def show_fractal(image):
    root = Tk()
    label = Label(root)
    label.pack()

    image_tk = ImageTk.PhotoImage(image)
    label.config(image=image_tk)
    root.update()
    root.mainloop()
