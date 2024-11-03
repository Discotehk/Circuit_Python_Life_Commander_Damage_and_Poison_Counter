This is a pretty simple Life, Commander Damage, and Poison Counter for Magic the Gathering.

When turned on it will display two icons for life and commander 1, a starting total for each, and a basic cursor to show selection.

I put the starting total at 40 as I only ever play commander anymore. To change this you'll need to edit the Life total tracker as well as the reset under deb_switch6.

The code counts up and down by ones and tens in life and commander mode and ones and fives in poison mode when the corresponding button is pressed. For the dpad buttons on the left, up is +1, down is -1, right is +10/5, left is -10/5.

The other two buttons on the right are for selecting which value to adjust and trigger a reset for the selected field. 

Changing the selection keeps your life total at the top while the bottom scrolls through Commander 1 -> 2 -> 3 -> Poison as indicated by the icons on the left. 

As the code counts, it pulls the corresponding number from sprite_sheet.bmp.
I did this so I could easily stylize or change the numbers as I feel like it. 
The starter sheet was drawn by mouse in Asperite and is 32 x 544 pixels for 17 32x32 tiles.

The code should run on any microcontroller running Adafruit's Circuit Python 9. I have it running on both a Pi Pico (RP2040) and Pi Pico 2 (RP2350). 

The necessary libraries are from the adafruit-circuitpython-bundle-9.x-mpy-20240730 bundle and are as follows:

	-adafruit_bus_device
 	-adafruit_display_text
	-adafruit_displayio_layout
	-adafruit_imageload
	-adafruit_debouncer.mpy
	-adafruit_displayio_ssd1306.mpy
	-adafruit_ticks.mpy
