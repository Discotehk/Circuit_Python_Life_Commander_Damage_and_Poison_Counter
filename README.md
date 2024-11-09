This is a pretty simple Life, Commander Damage, and Poison Counter for Magic the Gathering.

When turned on it will display two icons, one for life and one for commander 1, a starting total for each, and a basic cursor to show selection.

I put the starting total at 40 for EDH/Commander default. To change this you'll need to edit the Life total counter as well as the reset under deb_switch6. Change "lifeten = 4" "to = 2" for standard 20 life.

The code counts up and down by ones and tens in life and commander mode and ones and fives in poison mode when the corresponding button is pressed. For the dpad buttons on the left, up is +1, down is -1, right is +10/5, left is -10/5.

The upper right button, or A button, is for scrolling through the various counters. Life will always be displayed and is the starting position for the cursor. The first press moves the cursor to the Commander and poison selection position. Additional presses cycle through the options as displayed by the icons on the left until you return to the life counter position. 

The lower right button, or B button, is for resetting the selected field. This will put life back to 40, and all other fields to 0. As an added feature, if you have the poison field selected, you can scroll through additional sprite sheets. 

	-Up 	+1
 	-Down 	-1
  	-Right 	+10/+5
   	-Left 	-10/-5
    -A 	Select counter
    -B 	Reset counter 	*When on poison counter, also cycles art
    
![PXL_20241109_075218074](https://github.com/user-attachments/assets/3d458073-2643-490d-8104-15a901abe026)
![PXL_20241109_075238923](https://github.com/user-attachments/assets/f93ba74c-57a1-4d9a-bb2d-b4d3a700b145)
![PXL_20241109_075144995](https://github.com/user-attachments/assets/b7e1b326-8456-4908-a650-7942d18fa2a7)

As the code counts, it pulls the corresponding tile from the selected Sprite(x).bmp.
I did this so I could easily stylize or change the numbers and icons as I feel. 
The starter sheet was drawn by mouse in Asperite and is 32 x 544 pixels for 17 32x32 tiles.

Sprites need to be placed in a folder named "Sprite Sheets". The folder itself should be in the root.
Currently the code will cycle through Sprite1.bmp, Sprite2.bmp, and Sprite3.bmp. 

The eventual goal is to have the microcontroller scan and populate the .bpm options itself so you don't have to edit the code to use new art.

The code should run on any microcontroller running Adafruit's Circuit Python 9. I have it running on both a Pi Pico (RP2040) and Pi Pico 2 (RP2350). 

The display I'm using is an i2c SSD1306 128 X 64. It breaks down to a 4 x 2 grid of 32x32 resolution tiles. 

The necessary libraries are from the adafruit-circuitpython-bundle-9.x-mpy-20240730 bundle and are as follows:

	-adafruit_bus_device
 	-adafruit_display_text
	-adafruit_displayio_layout
	-adafruit_imageload
	-adafruit_debouncer.mpy
	-adafruit_displayio_ssd1306.mpy
	-adafruit_ticks.mpy

Short usage video: https://youtube.com/shorts/-RFBCQj1ZtM?si=uCUZgVwuXs6LkOWH
