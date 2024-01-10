import wiringpi
from wiringpi import GPIO
import time
import sys


class GpioConnector:
    def __init__(self):
        self.zoomer1_pin = 3
        self.zoomer2_pin = 4
        self.lamp_pin = 10
        self.servo_pin = 6
        self.__servo_value = 500

        wiringpi.wiringPiSetup()

        wiringpi.pinMode(self.lamp_pin, GPIO.OUTPUT)
        wiringpi.softServoSetup(self.servo_pin, -1, -1, -1, -1, -1, -1, -1)
        wiringpi.softToneCreate(self.zoomer1_pin)
        wiringpi.softToneCreate(self.zoomer2_pin)
        time.sleep(1)
        self.blink()


    def set_tone(self, frequency):
        wiringpi.softToneWrite(self.zoomer1_pin, frequency)
        wiringpi.softToneWrite(self.zoomer2_pin, frequency)


    def blink(self):
        wiringpi.digitalWrite(self.lamp_pin, GPIO.HIGH)
        time.sleep(1)
        wiringpi.digitalWrite(self.lamp_pin, GPIO.LOW)


    def make_noise(self):
        self.set_tone(2000)
        wiringpi.digitalWrite(self.lamp_pin, GPIO.HIGH)


    def stop_noise(self):
        self.set_tone(0)
        wiringpi.digitalWrite(self.lamp_pin, GPIO.LOW)


    def set_servo_value(self, value):
        self.__servo_value = value
        wiringpi.softServoWrite(self.servo_pin, self.__servo_value)
    

    def rotate_right(self):
        self.set_servo_value(self.__servo_value + 250)


    def rotate_left(self):
        self.set_servo_value(self.__servo_value - 250)
