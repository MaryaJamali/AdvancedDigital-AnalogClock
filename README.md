## Description
This project is a Tkinter based application that displays digital and analog clock. 🕰 Allows users to change the background color of the clock interface through the menu.
## Attributes
 ⭐ Digital clock : Current time as HH:MM Displays AM/PM.<br>
 ⭐ Analog Clock : Analog clock displays hour, minute and second hands.<br>
 ⭐ Ability to change the background : users can change the background color of the clock interface to black, light blue or light green.<br>
 ⭐ Background Image : Displays a background image on the canvas.<br>
## Installation
1. Simulate your repository : ``` git clone https://github.com/MaryaJamali/AdvancedDigital-AnalogClock.git```
2. Move to the project directory : ```cd AdvancedDigital-AnalogClock```
3. Install required libraries : ```pip install tkinter pillow```
4. Add background image : 👉 Place a background image named background.jpg in the project directory. The image will be resized to fit the canvas.
5. Run the program
## Code review
```update_time```Updates the digital clock every second and calls the analog ```draw_clock``` function.<br>
```draw_clock```Draws an analog clock with the current time.<br>
```change_bg_color```Changes the background color of the clock interface.<br>
```Main program```Creates the Tkinter window, sets the canvas, labels, and menus, and starts the main loop.<br>
## Author
Maryam Jamali 💞
