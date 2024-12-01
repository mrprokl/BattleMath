import picamera
import cv2
import io

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 25

def get_images():
    while True:
        # Capture frame-by-frame
        camera.capture('image.jpg')
        img = cv2.imread('image.jpg')
        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def generate_stream(format = "h264"):
    while True:
        # Capture frame-by-frame
        stream = io.BytesIO()
        camera.capture(stream, format=format, use_video_port=True)
        stream.seek(0)
        yield stream.read()


