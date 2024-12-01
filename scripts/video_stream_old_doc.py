from time import sleep
from picamera import PiCamera
import cv2
import io

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
sleep(2)

camera.capture('foo.jpg')