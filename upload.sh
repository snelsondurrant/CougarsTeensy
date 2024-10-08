#!/bin/bash

##########################################################
# UPLOADS HEX FILES TO THE RESPECTIVE TEENSY BOARDS
# - Specify a file in firmware_options using 'bash 
#   build.sh <file.hex>'
# - If this fails, check the USB connections and the
#   current teensy power states
##########################################################

case $1 in
    "")
        cd ~/teensy_ws/gpio_tools
        sudo python3 program_cougars.py

        cd ~/teensy_ws/cougars/.pio/build/teensy41
        tycmd upload firmware.hex
        ;;
    *)
        cd ~/teensy_ws/gpio_tools
        sudo python3 program_cougars.py

        cd ~/teensy_ws/firmware_options
        tycmd upload $1
        ;;
esac
