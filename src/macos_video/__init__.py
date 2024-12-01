import cv2

class MacosVideoProcessor:
    def __init__(self, source=0, resolution=(640, 480), framerate=30):
        self.source = source
        self.resolution = resolution
        self.framerate = framerate
        self.cap = cv2.VideoCapture(source)

    def get_ret_frame(self):
        ret, frame = self.cap.read()
        return ret, frame

    def loop_frame_process(self, func = lambda x:x):
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Error: Could not read frame.")
                    break
                
                # processes the frames
                processed_frame = func(frame)

                # Process the frame here (e.g., display, save, etc.)
                cv2.imshow("Frame", frame)

                # Break the loop if 'q' is pressed
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            # Release the capture when done
            self.cap.release()
            cv2.destroyAllWindows()