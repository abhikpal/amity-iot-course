from gpiozero import LED
from time import sleep

led = LED(17)

led.blink(on_time=0.5, off_time=0.5)
sleep(10)

led.off()

