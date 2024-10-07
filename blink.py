from gpiozero import LED
from time import sleep

led = LED(17) # Replace with your GPIO pin number

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
