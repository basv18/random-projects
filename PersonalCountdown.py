#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 14:03:41 2024

@author: barbarasilva
"""
import python_settings as st
from tkinter import * 
from tkinter import ttk 
from tkinter import messagebox
from tkinter import StringVar as string
from PIL import ImageTk, Image
import time


win = Tk()  #Create an instance of tkinter frame or window

canvas1 = Canvas(win, width=400, height=200, relief='raised')
canvas1.pack(expand = YES, fill = BOTH)
imagein = Image.open("stars.jpeg")
imageout = imagein.resize((400,200), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imageout)
canvas1.create_image(0, 0, image = image, anchor = NW)


#Create a label
label=Label(win, text= "Welcome to Barb's countdown!", borderwidth=0, font=('Aerial 20 bold'), fg='HotPink4')
label.configure(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label)


label1 = ttk.Label(win, text='Time h/m/s:', borderwidth=0)
label1.config(font=('helvetica', 10))
canvas1.create_window(200, 50, window=label1)

second = StringVar()
second.set('00')

minute = StringVar()
minute.set('00')

hour = StringVar()
hour.set('00')


entry1 = ttk.Entry(win, width=3, font=("Arial",18,""), textvariable = second)
entry1.config(foreground='pink')
entry2 = ttk.Entry(win, width=3, font=("Arial",18,""), textvariable = minute)
entry2.config(foreground='pink')
entry3 = ttk.Entry(win, width=3, font=("Arial",18,""), textvariable = hour)
entry3.config(foreground='pink')

canvas1.create_window(260, 100, window=entry1)
canvas1.create_window(210, 100, window=entry2)
canvas1.create_window(160, 100, window=entry3)

def countdown():
   t = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
   
   
   while t >-1:
      mins, secs = divmod(t,60)
      hours = 0

      if mins > 60:
         hours, mins = divmod(mins, 60)

      second.set("{0:2d}".format(secs))
      minute.set("{0:2d}".format(mins))
      hour.set("{0:2d}".format(hours))
      
      win.update()
      time.sleep(1)

      if (t == 0):
          messagebox.showinfo("Time Countdown", "Time's up ")

      t -= 1
      

button2 = ttk.Button(win, text = 'Start', command=countdown)
canvas1.create_window(200, 180, window=button2)
win.mainloop()


   






   