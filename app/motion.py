import RPi.GPIO as GPIO
import time

GPIO_MOTION_SENSOR = 23
DETECTION_TIMEOUT = 5  # number of seconds for 

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_MOTION_SENSOR, GPIO.IN) #PIR

detector_enabled = True


def detector_on(cbk_fn, *args):
    detector_enabled = True
    try:
        time.sleep(2) # to stabilize sensor
        while detector_enabled:
            if GPIO.input(GPIO_MOTION_SENSOR):
                cbk_fn(*args)
                time.sleep(DETECTION_TIMEOUT) #to avoid multiple detection
            time.sleep(0.1) #loop delay, should be less than detection delay

    except:
        GPIO.cleanup()


def detector_off():
    detector_enabled = False
