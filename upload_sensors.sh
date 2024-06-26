#!/bin/bash

##########################################################
# UPLOADS CURRENT FIRMWARE.HEX FILE TO SENSORS
# - If this fails, check the USB connections and the
#   current virtual teensy states in ~/teensy_ws/gpio
##########################################################

cd ~/teensy_ws/gpio
python3 toggle_on_sensors.py
python3 toggle_off_control.py
python3 program_sensors.py

cd ~/teensy_ws/sensors/.pio/build/teensy41
tycmd upload firmware.hex

cd ~/teensy_ws/gpio
python3 toggle_on_control.py
