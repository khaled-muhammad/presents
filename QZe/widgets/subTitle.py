import os
import tkinter 
from tkinter import font as tkFont
tkinter.Frame().destroy()  # Enough to initialize resources

def width_and_height_calculator_in_pixel(txt, fontname, fontsize):
    arial36b = tkFont.Font(family=fontname, size=fontsize, weight='normal')
    width = arial36b.measure(txt)
    return width

def subTitle(title, color):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/subTitle.html', 'r') as Template:
        template = Template.read()

    template = template.replace('{title}', title)

    fntSize = 22


    template = template.replace('{fntSize}', str(fntSize))
    #template = template.replace('{color}', color)
    #template = template.replace('{width}', str(fatherWidth+200))
    return template