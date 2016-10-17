from gpiozero import LED
from time import sleep

sleep_interval = 0.25

led = LED(17)

while True:
    led.on()
    sleep(sleep_interval)
    led.off()
    sleep(sleep_interval)
