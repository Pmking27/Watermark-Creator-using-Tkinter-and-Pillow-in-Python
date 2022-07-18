import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def add_watermark():
    
    image = filedialog.askopenfilename(initialdir="Pictures", title="Select an Image:")
    opened_image = Image.open(image)

    wm_text = text.get(1.0, "end-1c")

    image_width, image_height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(image_width / 6)

    font = ImageFont.truetype('arial.ttf',font_size)

    x, y= int(image_width/2) , int(image_height/1.75)

    draw.text((x,y),wm_text, font=font, fill='#FFF',stroke_width=5, stroke_fill='#222', anchor='ms')

    opened_image.show()

window = Tk()
window.title("Watermark Creator")
window.minsize(width=200, height=50)
window.resizable(0,0)
window.config(bg="SkyBlue1", padx=20, pady=20)


label = tk.Label(text="Enter Your Watermark Text 👇",font=("Arial", 15))
label.config(background="SkyBlue1")
label.grid(row=0, column=0, padx= 10, pady= 10)

text = Text(window, height=1, width=30)
text.grid(row=1, column=0, padx= 10, pady= 10)

button = tk.Button(window, text='Open The Image',command=add_watermark)
button.config(padx=15,pady=5)
button.grid(row=2, column=0, padx= 10, pady= 10)

window.mainloop()