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
font, palette = adafruit_imageload.load("Sprite Sheets/Sprite1.bmp",
                                        bitmap=displayio.Bitmap,
                                        palette=displayio.Palette)

font_tile = displayio.TileGrid(font,
                               pixel_shader=palette,
                               width=4,
                               height=2,
                               tile_width=32,
                               tile_height=32)


#  Group setup
group = displayio.Group(scale=1)
group.append(font_tile)

#  Tile setup
grid_num0 = 10
grid_num4 = 14
grid_num1 = 4
grid_num2 = 0
grid_num5 = 0
grid_num6 = 0
grid_num3 = 12
grid_num7 = 13
font_tile[0] = grid_num0  # life icon
font_tile[4] = grid_num4  # commander and poison icon
font_tile[1] = grid_num1  # life tens display
font_tile[2] = grid_num2  # life ones display
font_tile[5] = grid_num5  # commander and poison tens display
font_tile[6] = grid_num6  # commander and poison ones display
font_tile[3] = grid_num3  # selection display
font_tile[7] = grid_num7  # selection display

#  Display screen
display.root_group = group
group.x = 0
group.y = 0

#  Initial Selection
selection = 1
font_selection = 1

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
lifehun = 0
lifeten = 4
lifeone = 0
life = lifehun, lifeten, lifeone

#  Commander 1 tracker
cmd1hun = 0
cmd1ten = 0
cmd1one = 0
cmd1 = cmd1hun, cmd1ten, cmd1one

#  Commander 2 tracker
cmd2hun = 0
cmd2ten = 0
cmd2one = 0
cmd2 = cmd2hun, cmd2ten, cmd2one

#  Commander 3 tracker
cmd3hun = 0
cmd3ten = 0
cmd3one = 0
cmd3 = cmd3hun, cmd3ten, cmd3one

#  Poison tracker
poisonhun = 0
poisonten = 0
poisonone = 0
poison = poisonhun, poisonten, poisonone

#  Move Cursor on display
def selection_update():
    global selection
    global grid_num0
    global grid_num4
    global grid_num1
    global grid_num2
    global grid_num5
    global grid_num6
    global grid_num3
    global grid_num7
    global font_tile
    selection = selection + 1
    if selection >= 6:
        selection = 1
    print("selection:", selection)

    if selection == 1:
        grid_num3 = 12
        grid_num7 = 13
        grid_num4 = 14
        font_tile[3] = grid_num3
        font_tile[7] = grid_num7
        font_tile[4] = grid_num4
        update_cmd1()

    if selection == 2:
        grid_num3 = 13
        grid_num7 = 12
        grid_num4 = 14
        font_tile[3] = grid_num3
        font_tile[7] = grid_num7
        font_tile[4] = grid_num4
        update_cmd1()

    if selection == 3:
        grid_num3 = 13
        grid_num7 = 12
        grid_num4 = 15
        font_tile[3] = grid_num3
        font_tile[7] = grid_num7
        font_tile[4] = grid_num4
        update_cmd2()

    if selection == 4:
        grid_num3 = 13
        grid_num7 = 12
        grid_num4 = 16
        font_tile[3] = grid_num3
        font_tile[7] = grid_num7
        font_tile[4] = grid_num4
        update_cmd3()

    if selection == 5:
        grid_num3 = 13
        grid_num7 = 12
        grid_num4 = 11
        font_tile[3] = grid_num3
        font_tile[7] = grid_num7
        font_tile[4] = grid_num4
        update_poison()

def update_life():
    grid_num1 = lifeten
    font_tile[1] = grid_num1
    grid_num2 = lifeone
    font_tile[2] = grid_num2
    life = lifehun, lifeten, lifeone  # For debug printing
    print("life", life)

def update_cmd1():
    grid_num5 = cmd1ten
    font_tile[5] = grid_num5
    grid_num6 = cmd1one
    font_tile[6] = grid_num6
    cmd1 = cmd1hun, cmd1ten, cmd1one
    print("cmd1", cmd1)

def update_cmd2():
    grid_num5 = cmd2ten
    font_tile[5] = grid_num5
    grid_num6 = cmd2one
    font_tile[6] = grid_num6
    cmd2 = cmd2hun, cmd2ten, cmd2one
    print("cmd2", cmd2)

def update_cmd3():
    grid_num5 = cmd3ten
    font_tile[5] = grid_num5
    grid_num6 = cmd3one
    font_tile[6] = grid_num6
    cmd3 = cmd3hun, cmd3ten, cmd3one
    print("cmd3", cmd3)

def update_poison():
    grid_num5 = poisonten
    font_tile[5] = grid_num5
    grid_num6 = poisonone
    font_tile[6] = grid_num6
    poison = poisonhun, poisonten, poisonone
    print("poison", poison)

def check_math(ones, tens, huns):
    global selection
    global lifeone
    global lifeten
    global lifehun
    global cmd1hun
    global cmd1ten
    global cmd1one
    global cmd2hun
    global cmd2ten
    global cmd2one
    global cmd3hun
    global cmd3ten
    global cmd3one
    global poisonone
    global poisonten
    global poisonhun
    ones = ones
    tens = tens
    huns = huns
    if ones >= 10:
        ones = ones - 10
        tens = tens + 1

    if ones <= -1:
        ones = ones + 10
        tens = tens - 1

    if tens >= 10:
        tens = tens - 10
        huns = huns + 1

    if tens <= -1:
        tens = tens + 10
        huns = huns - 1

    #  Floor to stop from going negative
    if huns <= -1:
        huns = 0
        tens = 0
        ones = 0

    if selection == 1:
        lifehun = huns
        lifeten = tens
        lifeone = ones

    if selection == 2:
        cmd1hun = huns
        cmd1ten = tens
        cmd1one = ones

    if selection == 3:
        cmd2hun = huns
        cmd2ten = tens
        cmd2one = ones

    if selection == 4:
        cmd3hun = huns
        cmd3ten = tens
        cmd3one = ones

    if selection == 5:
        poisonhun = huns
        poisonten = tens
        poisonone = ones

def font_swap():
    global font_selection
    global grid_num0
    global grid_num4
    global grid_num1
    global grid_num2
    global grid_num5
    global grid_num6
    global grid_num3
    global grid_num7
    global font_tile
    if font_selection == 1:
        font, palette = adafruit_imageload.load("Sprite Sheets/Sprite1.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)
    if font_selection == 2:
        font, palette = adafruit_imageload.load("Sprite Sheets/Sprite2.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

    if font_selection == 3:
        font, palette = adafruit_imageload.load("Sprite Sheets/Sprite3.bmp",
                                                bitmap=displayio.Bitmap,
                                                palette=displayio.Palette)

    font_tile = displayio.TileGrid(font,
                                   pixel_shader=palette,
                                   width=4,
                                   height=2,
                                   tile_width=32,
                                   tile_height=32)
    #  Group setup
    group = displayio.Group(scale=1)
    group.append(font_tile)

    #  Tile setup
    font_tile[0] = grid_num0  # life icon
    font_tile[4] = grid_num4  # commander and poison icon
    font_tile[1] = grid_num1  # life tens display
    font_tile[2] = grid_num2  # life ones display
    font_tile[5] = grid_num5  # commander and poison tens display
    font_tile[6] = grid_num6  # commander and poison ones display
    font_tile[3] = grid_num3  # selection display
    font_tile[7] = grid_num7  # selection display

    #  Display screen
    display.root_group = group
    group.x = 0
    group.y = 0

with open("/Sprite Sheets/Sprite Selection.txt", 'r') as f:
    font_selection = int(f.read())
    print("font_selection:", font_selection)
    f.close()
    font_swap()

while True:
    #  Increment the ones field by 1
    deb_switch1.update()
    if deb_switch1.fell:
        if selection == 1:
            lifeone = lifeone + 1
            check_math(lifeone, lifeten, lifehun)
            update_life()
        if selection == 2:
            cmd1one = cmd1one + 1
            check_math(cmd1one, cmd1ten, cmd1hun)
            update_cmd1()
        if selection == 3:
            cmd2one = cmd2one + 1
            check_math(cmd2one, cmd2ten, cmd2hun)
            update_cmd2()
        if selection == 4:
            cmd3one = cmd3one + 1
            check_math(cmd3one, cmd3ten, cmd3hun)
            update_cmd3()
        if selection == 5:
            poisonone = poisonone + 1
            check_math(poisonone, poisonten, poisonhun)
            update_poison()
        print("key 1 press")

    #  Decrement the ones field by -1
    deb_switch2.update()
    if deb_switch2.fell:
        if selection == 1:
            lifeone = lifeone - 1
            check_math(lifeone, lifeten, lifehun)
            update_life()
        if selection == 2:
            cmd1one = cmd1one - 1
            check_math(cmd1one, cmd1ten, cmd1hun)
            update_cmd1()
        if selection == 3:
            cmd2one = cmd2one - 1
            check_math(cmd2one, cmd2ten, cmd2hun)
            update_cmd2()
        if selection == 4:
            cmd3one = cmd3one - 1
            check_math(cmd3one, cmd3ten, cmd3hun)
            update_cmd3()
        if selection == 5:
            poisonone = poisonone - 1
            check_math(poisonone, poisonten, poisonhun)
            update_poison()
        print("key 2 press")

    #  Increment the tens field by 1
    deb_switch3.update()
    if deb_switch3.fell:
        if selection == 1:
            lifeten = lifeten + 1
            check_math(lifeone, lifeten, lifehun)
            update_life()
        if selection == 2:
            cmd1ten = cmd1ten + 1
            check_math(cmd1one, cmd1ten, cmd1hun)
            update_cmd1()
        if selection == 3:
            cmd2ten = cmd2ten + 1
            check_math(cmd2one, cmd2ten, cmd2hun)
            update_cmd2()
        if selection == 4:
            cmd3ten = cmd3ten + 1
            check_math(cmd3one, cmd3ten, cmd3hun)
            update_cmd3()
        if selection == 5:
            poisonone = poisonone + 5
            check_math(poisonone, poisonten, poisonhun)
            update_poison()
        print("key 3 press")

    #  Decrement the tens field by -1
    deb_switch4.update()
    if deb_switch4.fell:
        if selection == 1:
            lifeten = lifeten - 1
            check_math(lifeone, lifeten, lifehun)
            update_life()
        if selection == 2:
            cmd1ten = cmd1ten - 1
            check_math(cmd1one, cmd1ten, cmd1hun)
            update_cmd1()
        if selection == 3:
            cmd2ten = cmd2ten - 1
            check_math(cmd2one, cmd2ten, cmd2hun)
            update_cmd2()
        if selection == 4:
            cmd3ten = cmd3ten - 1
            check_math(cmd3one, cmd3ten, cmd3hun)
            update_cmd3()
        if selection == 5:
            poisonone = poisonone - 5
            check_math(poisonone, poisonten, poisonhun)
            update_poison()
        print("key 4 press")

    #  Move Selection
    deb_switch5.update()
    if deb_switch5.fell:
        selection_update()
        print("key 5 press")

    #  Reset
    deb_switch6.update()
    if deb_switch6.fell:
        if selection == 1:
            lifehun = 0
            lifeten = 4
            lifeone = 0
            update_life()
        if selection == 2:
            cmd1one = 0
            cmd1ten = 0
            cmd1hun = 0
            update_cmd1()
        if selection == 3:
            cmd2one = 0
            cmd2ten = 0
            cmd2hun = 0
            update_cmd2()
        if selection == 4:
            cmd3one = 0
            cmd3ten = 0
            cmd3hun = 0
            update_cmd3()
        if selection == 5:
            poisonone = 0
            poisonten = 0
            poisonhun = 0
            font_selection = font_selection + 1
            if font_selection >= 4:
                font_selection = 1
            print("font_selection:", font_selection)
            with open("/Sprite Sheets/Sprite Selection.txt", 'w') as f:
                f.write(str(font_selection))
                f.close()
            font_swap()
            update_life()
            update_poison()
        print("key 6 press")
