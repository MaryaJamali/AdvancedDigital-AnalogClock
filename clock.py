import time
import math
import tkinter as tk
from PIL import Image, ImageTk


def update_time():
    current_time = time.strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)  # Set the label text to the current time
    draw_clock()  # call analog clock drawing function
    clock_label.after(1000, update_time)  # update every 1000 milliseconds (1 second)
  
# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
