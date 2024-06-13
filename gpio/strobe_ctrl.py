import gpiod
import time
import sys
import threading

LED_PIN = 15 #RX pin of pi
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)

def blink_func(toggle):
    if toggle == 1:
        try:
            while toggle == 1:
                led_line.set_value(1)
                time.sleep(1)
                led_line.set_value(0)
                time.sleep(1)
        finally:
            led_line.release()
    else:
        toggle = 0

toggle = sys.argv[0]
if toggle == 1:
    x = threading.Thread(target=blink_func, args = toggle)
    x.start()
    x.join()
else:
    toggle = 0

