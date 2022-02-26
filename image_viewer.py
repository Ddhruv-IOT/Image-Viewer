# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:28:37 2022

@author: ACER
"""

import glob
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("800x400")

lis = []

for file in glob.glob("*.jpg"):
    lis.append(file)


total = len(lis)
index = 0

def im_nxt():
    global index

    if (index+1) > total-1:
        pass
    else:
        index +=1
        print("next")
        img = ImageTk.PhotoImage(Image.open(lis[index]))
        label.config(image=img)
        label.photo = img
        print(index)

def im_prev():
    global index

    if (index-1) < 0:
        pass
    else:
        index -=1
        print("previous")
        img = ImageTk.PhotoImage(Image.open(lis[index]))
        label.config(image=img)
        label.photo = img
        print(index)

frame = tk.Frame(window, width=600, height=600)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

img = ImageTk.PhotoImage(Image.open(lis[index]))
label = tk.Label(frame, image=img)
label.pack()

B1 = tk.Button(window, text ="Nxt", command = im_nxt)
B1.pack()
B1.place(anchor='e', relx=0.8, rely=0.5)

B2 = tk.Button(window, text ="Prev", command = im_prev)
B2.pack()
B2.place(anchor='w', relx=0.2, rely=0.5)

window.mainloop()
