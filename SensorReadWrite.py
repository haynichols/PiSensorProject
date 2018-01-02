import time
# import sys
import RPi.GPIO as GPIO  # "includes" RPi GPIO module
GPIO.setmode(GPIO.BOARD)  # Specify number system as board numbering scheme
import Adafruit_DHT

# ------VARIABLES------
# DHT setup
DHT22_pin = 21
DHT = Adafruit_DHT.DHT22


DS18B_pin = 22

# LED Pins
redPin = 11
GPIO.setup(redPin,GPIO.OUT)
greenPin = 13
GPIO.setup(greenPin,GPIO.OUT)

# General
error = False


def get_sensor_data():
    humidity, temp = Adafruit_DHT.read_retry(DHT,DHT22_pin)
    write_data(humidity,temp)


def write_data(h, t):
    if h is not None and t is not None:
        # Write hum and temp to file
        print('Temp={0:0.1f}degC  Humidity={1:0.1f}%').format(T,H)
        GPIO.output(redPin, GPIO.LOW)
        GPIO.output(greenPin, GPIO.HIGH)
    else:
        print('Failed to get/display reading.')
        GPIO.output(greenPin, GPIO.LOW)
        GPIO.output(redPin, GPIO.HIGH)


print('Getting ready to read...')
GPIO.output(redPin, GPIO.HIGH)
GPIO.output(greenPin, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(redPin, GPIO.LOW)
GPIO.output(greenPin, GPIO.LOW)
oldTime = time.clock()


while error is False:  # loop
    if (time.clock()-oldTime) > 2:
        get_sensor_data()

