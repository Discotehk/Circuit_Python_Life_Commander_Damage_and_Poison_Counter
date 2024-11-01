import board
import busio
import displayio
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306
import adafruit_imageload
import digitalio
from digitalio import DigitalInOut
from adafruit_debouncer import Debouncer

displayio.release_displays()

i2c = busio.I2C(board.GP15, board.GP14)
display_bus = I2CDisplayBus(i2c, device_address=0x3c)

WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

bitmap, palette = adafruit_imageload.load("/sprite_sheet.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

tile_grid = displayio.TileGrid(bitmap,
                               pixel_shader=palette,
                               width=4,
                               height=2,
                               tile_width=32,
                               tile_height=32)

#  health and poison icons
tile_grid[0] = 10
tile_grid[4] = 11

#  life tens display
grid_num1 = 4
tile_grid[1] = grid_num1

#  life ones display
grid_num2 = 0
tile_grid[2] = grid_num2

#  poison tens display
grid_num5 = 4
tile_grid[1] = grid_num5

#  poison ones display
grid_num6 = 0
tile_grid[2] = grid_num6

#  selection display
grid_num3 = 12
tile_grid[3] = grid_num3

grid_num4 = 13
tile_grid[7] = grid_num4

selection = 1

group = displayio.Group(scale=1)

group.append(tile_grid)

display.root_group = group

group.x = 0
group.y = 0

switch1 = DigitalInOut(board.GP21)
switch1.switch_to_input(pull=digitalio.Pull.UP)
deb_switch1 = Debouncer(switch1)

switch2 = DigitalInOut(board.GP20)
switch2.switch_to_input(pull=digitalio.Pull.UP)
deb_switch2 = Debouncer(switch2)

switch3 = DigitalInOut(board.GP18)
switch3.switch_to_input(pull=digitalio.Pull.UP)
deb_switch3 = Debouncer(switch3)

switch4 = DigitalInOut(board.GP19)
switch4.switch_to_input(pull=digitalio.Pull.UP)
deb_switch4 = Debouncer(switch4)

switch5 = DigitalInOut(board.GP17)
switch5.switch_to_input(pull=digitalio.Pull.UP)
deb_switch5 = Debouncer(switch5)

switch6 = DigitalInOut(board.GP16)
switch6.switch_to_input(pull=digitalio.Pull.UP)
deb_switch6 = Debouncer(switch6)

lifetotalhun = 0
lifetotalten = 4
lifetotalone = 0
lifetotalupdate = 0

poisontotalhun = 0
poisontotalten = 0
poisontotalone = 0
poisontotalupdate = 0

while True:
    while selection == 1:
        deb_switch1.update()
        if deb_switch1.fell:
            lifetotalone = lifetotalone + 1
            lifetotalupdate = 1
            print("key 1 press")

        deb_switch2.update()
        if deb_switch2.fell:
            lifetotalone = lifetotalone - 1
            lifetotalupdate = 1
            print("key 2 press")

        deb_switch3.update()
        if deb_switch3.fell:
            lifetotalten = lifetotalten + 1
            lifetotalupdate = 1
            print("key 3 press")

        deb_switch4.update()
        if deb_switch4.fell:
            lifetotalten = lifetotalten - 1
            lifetotalupdate = 1
            print("key 4 press")

        deb_switch5.update()
        if deb_switch5.fell:
            selection = selection * -1
            print("key 5 press")

        deb_switch6.update()
        if deb_switch6.fell:
            lifetotalhun = 0
            lifetotalten = 4
            lifetotalone = 0
            lifetotalupdate = 1
            print("key 6 press")

        if lifetotalone >= 10:
            lifetotalone = 0
            lifetotalten = lifetotalten + 1
            lifetotalupdate = 1

        if lifetotalone <= -1:
            lifetotalone = 9
            lifetotalten = lifetotalten - 1
            lifetotalupdate = 1

        if lifetotalten >= 10:
            lifetotalten = 0
            lifetotalhun = lifetotalhun + 1
            lifetotalupdate = 1

        if lifetotalten <= -1:
            lifetotalten = 9
            lifetotalhun = lifetotalhun - 1
            lifetotalupdate = 1

        if lifetotalhun <= -1:
            lifetotalhun = 0
            lifetotalten = 0
            lifetotalone = 0
            lifetotalupdate = 1

        lifetotal = lifetotalhun, lifetotalten, lifetotalone

        if lifetotalupdate == 1:
            grid_num1 = lifetotalten
            tile_grid[1] = grid_num1
            grid_num2 = lifetotalone
            tile_grid[2] = grid_num2
            print(lifetotal)
            lifetotalupdate = 0

        if selection == 1:
            grid_num3 = 12
            grid_num4 = 13
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4

        if selection == -1:
            grid_num3 = 13
            grid_num4 = 12
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4

    while selection == -1:
        deb_switch1.update()
        if deb_switch1.fell:
            poisontotalone = poisontotalone + 1
            poisontotalupdate = 1
            print("key 1 press")

        deb_switch2.update()
        if deb_switch2.fell:
            poisontotalone = poisontotalone - 1
            poisontotalupdate = 1
            print("key 2 press")

        deb_switch3.update()
        if deb_switch3.fell:
            poisontotalone = poisontotalone + 5
            poisontotalupdate = 1
            print("key 3 press")

        deb_switch4.update()
        if deb_switch4.fell:
            poisontotalone = poisontotalone - 5
            poisontotalupdate = 1
            print("key 4 press")

        deb_switch5.update()
        if deb_switch5.fell:
            selection = selection * -1
            print("key 5 press")

        deb_switch6.update()
        if deb_switch6.fell:
            poisontotalhun = 0
            poisontotalten = 0
            poisontotalone = 0
            poisontotalupdate = 1
            print("key 6 press")

        if poisontotalone >= 10:
            poisontotalone = 0
            poisontotalten = poisontotalten + 1
            poisontotalupdate = 1

        if poisontotalone <= -1:
            poisontotalone = 9
            poisontotalten = poisontotalten - 1
            poisontotalupdate = 1

        if poisontotalten >= 10:
            poisontotalten = 0
            poisontotalhun = poisontotalhun + 1
            poisontotalupdate = 1

        if poisontotalten <= -1:
            poisontotalten = 9
            poisontotalhun = poisontotalhun - 1
            poisontotalupdate = 1

        if poisontotalhun <= -1:
            poisontotalhun = 0
            poisontotalten = 0
            poisontotalone = 0
            poisontotalupdate = 1

        poisontotal = poisontotalhun, poisontotalten, poisontotalone

        if poisontotalupdate == 1:
            grid_num5 = poisontotalten
            tile_grid[5] = grid_num5
            grid_num6 = poisontotalone
            tile_grid[6] = grid_num6
            print(poisontotal)
            poisontotalupdate = 0

        if selection == 1:
            grid_num3 = 12
            grid_num4 = 13
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4

        if selection == -1:
            grid_num3 = 13
            grid_num4 = 12
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
