This is a pretty simple Life and Poison Counter for Magic the Gathering.

When turned on it will display two icons for life and poison, a starting total for each, and a basic cursor to show selection.

I put the starting total at 40 as I only ever play commander anymore.

The code counts up and down by ones and tens in life mode and ones and fives in poison mode when the corresponding button is pressed. 
This accounts for four off the buttons. 
The other two buttons are for selecting which value to adjust and a basic reset. 

As the code counts, it pulls the corresponding number from sprite_sheet.bmp.
I did this so I could easily stylize or change the numbers as I feel like it. 
The starter sheet was drawn by mouse in Asperite and is 32 x 448 pixels for 14 32x32 tiles.

The code should run on any microcontroller running Adafruit's Circuit Python 9. I have it running on both a Pi Pico and Pi Pico 2. 

The necessary libraries are from the adafruit-circuitpython-bundle-9.x-mpy-20240730 bundle and are as follows:

	-adafruit_bus_device
 	-adafruit_display_text
	-adafruit_displayio_layout
	-adafruit_imageload
	-adafruit_debouncer.mpy
	-adafruit_displayio_ssd1306.mpy
	-adafruit_ticks.mpy
