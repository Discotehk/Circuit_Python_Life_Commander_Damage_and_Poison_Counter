import board
import busio
import displayio
from i2cdisplaybus import I2CDisplayBus
import adafruit_displayio_ssd1306
import adafruit_imageload
import digitalio
from digitalio import DigitalInOut
from adafruit_debouncer import Debouncer

#  Display setup
displayio.release_displays()

i2c = busio.I2C(board.GP15, board.GP14)
display_bus = I2CDisplayBus(i2c, device_address=0x3c)

WIDTH = 128
HEIGHT = 64
BORDER = 5

display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

#  Tile Setup
bitmap, palette = adafruit_imageload.load("/sprite_sheet.bmp",
                                          bitmap=displayio.Bitmap,
                                          palette=displayio.Palette)

tile_grid = displayio.TileGrid(bitmap,
                               pixel_shader=palette,
                               width=4,
                               height=2,
                               tile_width=32,
                               tile_height=32)

#  life icon
tile_grid[0] = 10

#  commander and poison icon
tile_grid[4] = 14

#  life tens display
grid_num1 = 4
tile_grid[1] = grid_num1

#  life ones display
grid_num2 = 0
tile_grid[2] = grid_num2

#  commander and poison tens display
grid_num5 = 4
tile_grid[1] = grid_num5

#  commander and poison ones display
grid_num6 = 0
tile_grid[2] = grid_num6

#  selection display
grid_num3 = 12
grid_num4 = 13
tile_grid[3] = grid_num3
tile_grid[7] = grid_num4

#  Initial Selection
selection = 1

#  I don't remember
group = displayio.Group(scale=1)

group.append(tile_grid)

display.root_group = group

group.x = 0
group.y = 0

#  Button to pin assignments and debouncing
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

#  Life total tracker
lifetotalhun = 0
lifetotalten = 4
lifetotalone = 0
lifetotalupdate = 0

#  Commander 1 tracker
commander1hun = 0
commander1ten = 0
commander1one = 0
commander1update = 0

#  Commander 2 tracker
commander2hun = 0
commander2ten = 0
commander2one = 0
commander2update = 0

#  Commander 3 tracker
commander3hun = 0
commander3ten = 0
commander3one = 0
commander3update = 0

#  Poison tracker
poisontotalhun = 0
poisontotalten = 0
poisontotalone = 0
poisontotalupdate = 0

while True:
    #  Life Count
    while selection == 1:
        #  Increment the ones field by 1
        deb_switch1.update()
        if deb_switch1.fell:
            lifetotalone = lifetotalone + 1
            lifetotalupdate = 1
            print("key 1 press")

        #  Decrement the ones field by -1
        deb_switch2.update()
        if deb_switch2.fell:
            lifetotalone = lifetotalone - 1
            lifetotalupdate = 1
            print("key 2 press")

        #  Increment the tens field by 1
        deb_switch3.update()
        if deb_switch3.fell:
            lifetotalten = lifetotalten + 1
            lifetotalupdate = 1
            print("key 3 press")

        #  Decrement the tens field by -1
        deb_switch4.update()
        if deb_switch4.fell:
            lifetotalten = lifetotalten - 1
            lifetotalupdate = 1
            print("key 4 press")

        #  Move Selection
        deb_switch5.update()
        if deb_switch5.fell:
            selection = 2
            print("key 5 press")

        #  Reset
        deb_switch6.update()
        if deb_switch6.fell:
            lifetotalhun = 0
            lifetotalten = 4
            lifetotalone = 0
            lifetotalupdate = 1
            print("key 6 press")

        #  Math
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

        #  Floor to stop from going negative
        if lifetotalhun <= -1:
            lifetotalhun = 0
            lifetotalten = 0
            lifetotalone = 0
            lifetotalupdate = 1

        #  For debug printing
        lifetotal = lifetotalhun, lifetotalten, lifetotalone

        #  Update function
        if lifetotalupdate == 1:
            grid_num1 = lifetotalten
            tile_grid[1] = grid_num1
            grid_num2 = lifetotalone
            tile_grid[2] = grid_num2
            print(lifetotal)
            lifetotalupdate = 0

        #  Move Cursor on display
        if selection == 2:
            grid_num3 = 13
            grid_num4 = 12
            grid_num5 = 14
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
            tile_grid[4] = grid_num5
            commander1update = 1

        commander1 = commander1hun, commander1ten, commander1one

        if commander1update == 1:
            grid_num5 = commander1ten
            tile_grid[5] = grid_num5
            grid_num6 = commander1one
            tile_grid[6] = grid_num6
            print(commander1)
            commander1update = 0

    #  Commander 1 Damage Tracker
    while selection == 2:
        deb_switch1.update()
        if deb_switch1.fell:
            commander1one = commander1one + 1
            commander1update = 1
            print("key 1 press")

        deb_switch2.update()
        if deb_switch2.fell:
            commander1one = commander1one - 1
            commander1update = 1
            print("key 2 press")

        deb_switch3.update()
        if deb_switch3.fell:
            commander1ten = commander1ten + 1
            commander1update = 1
            print("key 3 press")

        deb_switch4.update()
        if deb_switch4.fell:
            commander1ten = commander1ten - 1
            commander1update = 1
            print("key 4 press")

        deb_switch5.update()
        if deb_switch5.fell:
            selection = 3
            print("key 5 press")

        deb_switch6.update()
        if deb_switch6.fell:
            commander1hun = 0
            commander1ten = 0
            commander1one = 0
            commander1update = 1
            print("key 6 press")

        if commander1one >= 10:
            commander1one = 0
            commander1ten = commander1ten + 1
            commander1update = 1

        if commander1one <= -1:
            commander1one = 9
            commander1ten = commander1ten - 1
            commander1update = 1

        if commander1ten >= 10:
            commander1ten = 0
            commander1hun = commander1hun + 1
            commander1update = 1

        if commander1ten <= -1:
            commander1ten = 9
            commander1hun = commander1hun - 1
            commander1update = 1

        if commander1hun <= -1:
            commander1hun = 0
            commander1ten = 0
            commander1one = 0
            commander1update = 1

        commander1 = commander1hun, commander1ten, commander1one

        if commander1update == 1:
            grid_num5 = commander1ten
            tile_grid[5] = grid_num5
            grid_num6 = commander1one
            tile_grid[6] = grid_num6
            print(commander1)
            commander1update = 0

        if selection == 3:
            grid_num3 = 13
            grid_num4 = 12
            grid_num5 = 15
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
            tile_grid[4] = grid_num5
            commander2update = 1

        commander2 = commander2hun, commander2ten, commander2one

        if commander2update == 1:
            grid_num5 = commander2ten
            tile_grid[5] = grid_num5
            grid_num6 = commander2one
            tile_grid[6] = grid_num6
            print(commander2)
            commander2update = 0

    #  Commander 2 Damage Tracker
    while selection == 3:
        deb_switch1.update()
        if deb_switch1.fell:
            commander2one = commander2one + 1
            commander2update = 1
            print("key 1 press")

        deb_switch2.update()
        if deb_switch2.fell:
            commander2one = commander2one - 1
            commander2update = 1
            print("key 2 press")

        deb_switch3.update()
        if deb_switch3.fell:
            commander2ten = commander2ten + 1
            commander2update = 1
            print("key 3 press")

        deb_switch4.update()
        if deb_switch4.fell:
            commander2ten = commander2ten - 1
            commander2update = 1
            print("key 4 press")

        deb_switch5.update()
        if deb_switch5.fell:
            selection = 4
            print("key 5 press")

        deb_switch6.update()
        if deb_switch6.fell:
            commander2hun = 0
            commander2ten = 0
            commander2one = 0
            commander2update = 1
            print("key 6 press")

        if commander2one >= 10:
            commander2one = 0
            commander2ten = commander2ten + 1
            commander2update = 1

        if commander2one <= -1:
            commander2one = 9
            commander2ten = commander2ten - 1
            commander2update = 1

        if commander2ten >= 10:
            commander2ten = 0
            commander2hun = commander2hun + 1
            commander2update = 1

        if commander2ten <= -1:
            commander2ten = 9
            commander2hun = commander2hun - 1
            commander2update = 1

        if commander2hun <= -1:
            commander2hun = 0
            commander2ten = 0
            commander2one = 0
            commander2update = 1

        commander2 = commander2hun, commander2ten, commander2one

        if commander2update == 1:
            grid_num5 = commander2ten
            tile_grid[5] = grid_num5
            grid_num6 = commander2one
            tile_grid[6] = grid_num6
            print(commander2)
            commander2update = 0

        if selection == 4:
            grid_num3 = 13
            grid_num4 = 12
            grid_num5 = 16
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
            tile_grid[4] = grid_num5
            commander3update = 1

        commander3 = commander3hun, commander3ten, commander3one

        if commander3update == 1:
            grid_num5 = commander3ten
            tile_grid[5] = grid_num5
            grid_num6 = commander3one
            tile_grid[6] = grid_num6
            print(commander3)
            commander3update = 0
      
    #  Commander 3 Damage Tracker
    while selection == 4:
        deb_switch1.update()
        if deb_switch1.fell:
            commander3one = commander3one + 1
            commander3update = 1
            print("key 1 press")

        deb_switch2.update()
        if deb_switch2.fell:
            commander3one = commander3one - 1
            commander3update = 1
            print("key 2 press")

        deb_switch3.update()
        if deb_switch3.fell:
            commander3ten = commander3ten + 1
            commander3update = 1
            print("key 3 press")

        deb_switch4.update()
        if deb_switch4.fell:
            commander3ten = commander3ten - 1
            commander3update = 1
            print("key 4 press")

        deb_switch5.update()
        if deb_switch5.fell:
            selection = 5
            print("key 5 press")

        deb_switch6.update()
        if deb_switch6.fell:
            commander3hun = 0
            commander3ten = 0
            commander3one = 0
            commander3update = 1
            print("key 6 press")

        if commander3one >= 10:
            commander3one = 0
            commander3ten = commander3ten + 1
            commander3update = 1

        if commander3one <= -1:
            commander3one = 9
            commander3ten = commander3ten - 1
            commander3update = 1

        if commander3ten >= 10:
            commander3ten = 0
            commander3hun = commander3hun + 1
            commander3update = 1

        if commander3ten <= -1:
            commander3ten = 9
            commander3hun = commander3hun - 1
            commander3update = 1

        if commander3hun <= -1:
            commander3hun = 0
            commander3ten = 0
            commander3one = 0
            commander3update = 1

        commander3 = commander3hun, commander3ten, commander3one

        if commander3update == 1:
            grid_num5 = commander3ten
            tile_grid[5] = grid_num5
            grid_num6 = commander3one
            tile_grid[6] = grid_num6
            print(commander3)
            commander3update = 0

        if selection == 5:
            grid_num3 = 13
            grid_num4 = 12
            grid_num5 = 11
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
            tile_grid[4] = grid_num5
            poisontotalupdate = 1

        poisontotal = poisontotalhun, poisontotalten, poisontotalone

        if poisontotalupdate == 1:
            grid_num5 = poisontotalten
            tile_grid[5] = grid_num5
            grid_num6 = poisontotalone
            tile_grid[6] = grid_num6
            print(poisontotal)
            poisontotalupdate = 0

    #  poison counters
    while selection == 5:
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
            selection = 1
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
            grid_num5 = 14
            tile_grid[3] = grid_num3
            tile_grid[7] = grid_num4
            tile_grid[4] = grid_num5
            commander1update = 1

        commander1 = commander1hun, commander1ten, commander1one

        if commander1update == 1:
            grid_num5 = commander1ten
            tile_grid[5] = grid_num5
            grid_num6 = commander1one
            tile_grid[6] = grid_num6
            print(commander1)
            commander1update = 0
