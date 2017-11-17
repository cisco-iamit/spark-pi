import RPi.GPIO as GPIO
import time
from config import config

detection_timeout = 5  # number of seconds for
sensor_poll_timeout = 0.1

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.gpio_motion_sensor, GPIO.IN) #PIR

detector_enabled = True


def detector_on(cbk_fn, *args):
    detector_enabled = True
    try:
        time.sleep(2) # to stabilize sensor
        while detector_enabled:
            if GPIO.input(config.gpio_motion_sensor):
                cbk_fn(*args)
                time.sleep(detection_timeout) #to avoid multiple detection
            time.sleep(sensor_poll_timeout) #loop delay, should be less than detection delay

    except:
        GPIO.cleanup()


def detector_off():
    detector_enabled = False
