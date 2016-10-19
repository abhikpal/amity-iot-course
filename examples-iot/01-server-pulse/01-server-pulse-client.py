from gpiozero import PWMLED
from time import sleep
import requests

led = PWMLED(17)

while True:
    r = requests.get("http://192.168.1.8:5000/")
    if r.text == '1':
        led.pulse()
    if r.text == '0':
        led.off()
    sleep(2)

