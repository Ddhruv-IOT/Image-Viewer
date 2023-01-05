# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:28:37 2022

@author: ACER
"""

import glob
import tkinter as tk
from PIL import ImageTk, Image


img_list_raw = []
img_list = []

index = []
index.append(0)
idx = index

window = tk.Tk()
window.geometry("800x400")


def img_finder():
    """ Function to find images on Device """

    for file in glob.glob("*.jpg"):
        img_list_raw.append(file)

    for file in glob.glob("*.png"):
        img_list_raw.append(file)

    for file in glob.glob("*.jpeg"):
        img_list_raw.append(file)

    for file in glob.glob("*.ico"):
        img_list_raw.append(file)

    for file in glob.glob("*.jfif"):
        img_list_raw.append(file)

    if img_list_raw:
        return len(img_list_raw)

    return None


total = img_finder()
img_list = img_list_raw


def img_loader():
    """ Function to load the images on GUI"""

    img = Image.open(img_list[idx[0]])
    img = img.resize((300, 205), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    return img


def img_update(img):
    """ Function to change the images based on user input """

    label.config(image=img)
    label.photo = img


def im_nxt():
    """ Function for next Image """

    if (idx[0] + 1) > total - 1:
        pass
    else:
        idx[0] += 1
        img_update(img_loader())


def im_prev():
    """ Function for previous Image """

    if (idx[0] - 1) < 0:
        pass
    else:
        idx[0] -= 1
        img_update(img_loader())


frame = tk.Frame(window, width=600, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

current_img = img_loader()
label = tk.Label(frame, image=current_img)
label.pack()

B1 = tk.Button(window, text="Nxt", command=im_nxt)
B1.pack()
B1.place(anchor='e', relx=0.8, rely=0.5)

B2 = tk.Button(window, text="Prev", command=im_prev)
B2.pack()
B2.place(anchor='w', relx=0.2, rely=0.5)

window.mainloop()
