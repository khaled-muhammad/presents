import os
import tkinter 
from tkinter import font as tkFont
tkinter.Frame().destroy()  # Enough to initialize resources

def width_and_height_calculator_in_pixel(txt, fontname, fontsize):
    arial36b = tkFont.Font(family=fontname, size=fontsize, weight='normal')
    width = arial36b.measure(txt)
    return width

def Title(title, icon, color):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/title.html', 'r') as Template:
        template = Template.read()

    template = template.replace('{title}', title)
    #32pt
    fntSize = 5
    fatherWidth = 170

    while width_and_height_calculator_in_pixel(title, 'Do Hyeon', int(fntSize)) < fatherWidth:
        fntSize += 0.5

    template = template.replace('{fntSize}', str(fntSize))
    template = template.replace('{icon}', icon)
    template = template.replace('{color}', color)

    return template