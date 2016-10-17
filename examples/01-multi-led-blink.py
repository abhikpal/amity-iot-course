from gpiozero import LED
from time import sleep

leds = [LED(17), LED(18)]

while True:
    for led in leds:
        led.on()
        sleep(0.25)
        led.off()
        sleep(0.1)

