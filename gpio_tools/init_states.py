##########################################################
# INITS PINS AND SETS CURRENT POWER STATES TO "ON"
# - The docker container runs this script on startup!
#   Be careful editing or moving it
##########################################################

import time
import gpiod

# import gpio_id from the same directory
from gpio_def import *

# open the GPIO chip
chip = gpiod.Chip('/dev/gpiochip4')
control_power_line = chip.get_line(CONTROL_POWER_PIN)
sensors_power_line = chip.get_line(SENSORS_POWER_PIN)
control_prog_line = chip.get_line(CONTROL_PROGRAM_PIN)
sensors_prog_line = chip.get_line(SENSORS_PROGRAM_PIN)

control_power_line.request(consumer="CONTROL_POWER", type=gpiod.LINE_REQ_DIR_OUT)
sensors_power_line.request(consumer="SENSORS_POWER", type=gpiod.LINE_REQ_DIR_OUT)
control_prog_line.request(consumer="CONTROL_PROG", type=gpiod.LINE_REQ_DIR_OUT)
sensors_prog_line.request(consumer="SENSORS_PROG", type=gpiod.LINE_REQ_DIR_OUT)

print("Initializing GPIO pins...")

# set the GPIO pins high
control_power_line.set_value(1)
sensors_power_line.set_value(1)
control_prog_line.set_value(1)
sensors_prog_line.set_value(1)

# turn the Teensy boards on
time.sleep(5)
control_power_line.set_value(0)
sensors_power_line.set_value(0)
print(". . .")
time.sleep(5)
control_power_line.set_value(1)
sensors_power_line.set_value(1)

print("COMPLETE: GPIO pins initialized")
control_power_line.release()
sensors_power_line.release()
control_prog_line.release()
sensors_prog_line.release()
