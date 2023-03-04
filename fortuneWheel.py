import random

import numpy as np
import cv2
import tkinter as tk
from tkinter import *
import PIL as pil
from PIL import ImageTk, Image

class fortuneWheel():

    def saveImage(self, img, file_name):
        # Create a folder called 'availabilityTimeImg' if it doesn't exist
        if not os.path.exists('availabilityTimeImg'):
            os.makedirs('availabilityTimeImg')

        # Save the image in the 'availabilityTimeImg' folder
        file_path = 'availabilityTimeImg/' + file_name + '.png'
        cv2.imwrite(file_path, img)

    def showImg(self, img):
        # Show image with wait statement

        cv2.imshow('window', img)

        cv2.setWindowProperty('window', cv2.WND_PROP_TOPMOST, 1)

        cv2.waitKey()

    def createWindow(self):

        def decrease():
            num = int(count['text'])
            num -= 1
            count['text'] = str(num)

        def increase():
            num = int(count['text'])
            num += 1
            count['text'] = str(num)

        window = tk.Tk()

        window.rowconfigure(0, weight=1, minsize=50)
        window.columnconfigure([0,1,2], weight=1, minsize=75)

        buttonInc = tk.Button(master=window, text='-', command=decrease)
        buttonInc.grid(row=0, column=0, sticky='nsew')

        count = tk.Label(master=window, text='0')
        count.grid(row=0, column=1)

        buttonDec = tk.Button(master=window, text='+', command=increase)
        buttonDec.grid(row=0, column=2, sticky='nsew')

        window.mainloop()

    def rollDice(self):

        def roll():
            roll = random.randint(0,7)

            rollLabel['text'] = str(roll)

        window = tk.Tk()

        window.rowconfigure(0, weight=1)
        window.columnconfigure([0,1], weight=1)

        rollBtn = tk.Button(master=window, text='Roll', command=roll)
        rollBtn.grid(row=0, column=0)
        rollLabel = tk.Label(master=window, text='0')
        rollLabel.grid(row=1, column=0)

        window.mainloop()

    def calculateNewDimension(self, newWidth, newHeight, width, height):
        ratio = min(newWidth/width, newHeight/height)

        return (int(width*ratio), int(height*ratio))


    def displayWheel(self):

        window = tk.Tk()

        canvas = Canvas(window, width=600, height=700)
        canvas.configure(background="#242424")

        canvas.pack()

        img = Image.open('img/wheel_element/choicer.png')
        choicerDimensions = (552, 811)
        wheelDimensions = (3386, 3386)

        imgAntiAliased = img.resize(self.calculateNewDimension(600, 500, choicerDimensions[0], choicerDimensions[1]),
                                    resample=Image.LANCZOS)

        pic = ImageTk.PhotoImage(imgAntiAliased)

        canvas.create_image(20, 20, anchor=NW, image=pic)

        window.mainloop()