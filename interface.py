#!/usr/bin/python3

from tkinter import *
from PIL import Image, ImageTk
from donnees import getCoefficient, getMovement


root = Tk()
  
# Adjust size 
root.geometry("450x590")

  




images = []  # to hold the newly created image

def create_rectangle(x1, y1, x2, y2, **kwargs):
    if 'alpha' in kwargs:
        alpha = int(kwargs.pop('alpha') * 255)
        fill = kwargs.pop('fill')
        fill = root.winfo_rgb(fill) + (alpha,)
        image = Image.new('RGBA', (x2-x1, y2-y1), fill)
        images.append(ImageTk.PhotoImage(image))
        canvas.create_image(x1, y1, image=images[-1], anchor='nw')
    canvas.create_rectangle(x1, y1, x2, y2, **kwargs)

canvas = Canvas(width=450, height=590)
image = ImageTk.PhotoImage(file = "images/fond.png")
canvas.create_image(0, 0, image = image, anchor = NW)











x=getCoefficient()


create_rectangle(0, x, 450, 590, fill='blue', alpha=.5)


mov = getMovement()

if mov=="RISING":
    image2 = ImageTk.PhotoImage(file = "images/arrow-up.png")
if mov=="FALLING":
    image2 = ImageTk.PhotoImage(file = "images/arrow-down.png")
if mov=="HIGH TIDE":
    image2 = ImageTk.PhotoImage(file = "images/maree-haute.png")
if mov=="LOW TIDE":
    image2 = ImageTk.PhotoImage(file = "images/maree-basse.png")



canvas.create_image(10, 10, image = image2, anchor = NW)


canvas.pack()






root.resizable(False, False) 

# Execute tkinter
root.mainloop()