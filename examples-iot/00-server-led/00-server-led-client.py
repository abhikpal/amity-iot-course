from gpiozero import LED
import requests
from time import sleep

led = LED(17)

while True:
    r = requests.get("http://192.168.1.8:5000/")
    if r.text == '1':
        led.on()
    if r.text == '0':
        led.off()
    sleep(1)

