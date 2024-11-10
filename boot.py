import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.GP17)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

readstate = True

if switch.value == True:
    readstate = False

storage.remount("/", readonly=readstate)
