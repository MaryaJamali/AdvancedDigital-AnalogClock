import time
import math
import tkinter as tk
from PIL import Image, ImageTk


def update_time():
    current_time = time.strftime('%H:%M:%S %p')  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)  # Set the label text to the current time
    draw_clock()  # call analog clock drawing function
    clock_label.after(1000, update_time)  # update every 1000 milliseconds (1 second)


def draw_clock():
    canvas.delete("all")  # Delete all elements from the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_photo)  # Set the background image

    width = 300  # Canvas width
    height = 200  # canvas height
    center_x = width // 2  # Horizontal center of the canvas
    center_y = height // 2  # The vertical center of the canvas
    radius = 80  # The radius of the clock circle

    # Draw the outer circle of the clock
    canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="white",
                       width=2)

    # Draw the outer circle of the clock
    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)  # Calculate the angle of each number
        x = center_x + (radius - 20) * math.cos(angle)  # Calculate the horizontal position of the number
        y = center_y + (radius - 20) * math.sin(angle)  # Calculate the vertical position of the number
        canvas.create_text(x, y, text=str(i), fill="white", font=('calibri', 12, 'bold'))  # draw the number

    # Get the current time
    now = time.localtime()
    seconds = now.tm_sec  # Current seconds
    minutes = now.tm_min  # current minutes
    hours = now.tm_hour % 12  # Current hours (in 12-hour format)

    # Calculate the position of the clock hands
    second_angle = math.radians(seconds * 6 - 90)  # Second hand angle
    minute_angle = math.radians(minutes * 6 - 90)  # Minute hand angle
    hour_angle = math.radians(hours * 30 + minutes * 0.5 - 90)  # hour hand angle

    second_hand_length = radius - 10  # The length of the second hand
    minute_hand_length = radius - 20  # The length of the minute hand
    hour_hand_length = radius - 30  # The length of the hour hand

    # Draw the second hand
    canvas.create_line(center_x, center_y, center_x + second_hand_length * math.cos(second_angle),
                       center_y + second_hand_length * math.sin(second_angle), fill="white", width=1)

    # Draw the minute hand
    canvas.create_line(center_x, center_y, center_x + minute_hand_length * math.cos(minute_angle),
                       center_y + minute_hand_length * math.sin(minute_angle), fill="white", width=1)

    # Draw the hour hand
    canvas.create_line(center_x, center_y, center_x + hour_hand_length * math.cos(hour_angle),
                       center_y + hour_hand_length * math.sin(hour_angle), fill="white", width=3)


# Create the main window
root = tk.Tk()
root.title("Advanced Digital Clock")  # Set window title

# Load background image
bg_image = Image.open("background.jpg")
bg_image = bg_image.resize((300, 400), Image.ANTIALIAS)  # Change the size of the background image
bg_photo = ImageTk.PhotoImage(bg_image)  # Convert the image to a suitable format for tkinter


# Settings to change the background
def change_bg_color(color):
    clock_label.config(background=color)  # Change the background color of the clock label
    canvas.config(background=color)  # Change the background color of the canvas


# Create a canvas to draw an analog clock
canvas = tk.Canvas(root, width=300, height=400)
canvas.pack()  # Add a canvas to the window

# Create a label to display the digital clock
clock_label = tk.Label(root, font=('calibri', 15, 'bold'), background='white', foreground='white')
clock_label.pack(anchor='center')  # Add a label to the window

# Create a menu to change the background color
menu = tk.Menu(root)
root.config(menu=menu)

bg_menu = tk.Menu(menu)
menu.add_cascade(label="Change Background", menu=bg_menu)
bg_menu.add_command(label="Black", command=lambda: change_bg_color('black'))
bg_menu.add_command(label="Light Blue", command=lambda: change_bg_color('lightblue'))
bg_menu.add_command(label="Light Green", command=lambda: change_bg_color('lightgreen'))


# Create a menu to change the background color
update_time()
# Create a menu to change the background color
root.mainloop()

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
