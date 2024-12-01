from picamera2 import Picamera2, Preview
import cv2
import numpy as np
import time

class RaspberryPiVideoProcessor:
    def __init__(self, resolution=(640, 480), framerate=30):
        self.picam2 = Picamera2()
        
        # Lightweight configuration for 2GB RAM
        config = self.picam2.create_video_configuration(
            main={"size": resolution},
            lores={"size": resolution},
            encode="lores"
        )
        self.picam2.configure(config)

    def start_processing(self):
        self.picam2.start()
        time.sleep(2)  # Warm-up time

        try:
            while True:
                # Capture frame
                frame = self.picam2.capture_array()
                
                # Basic image processing
                processed_frame = self._process_frame(frame)
                
                # Display processed frame
                cv2.imshow("Processed Video", processed_frame)
                
                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        finally:
            self.picam2.stop()
            cv2.destroyAllWindows()

    def _process_frame(self, frame):
        # Example processing: grayscale conversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Optional: Simple edge detection
        edges = cv2.Canny(gray, 50, 150)
        
        return edges

def main():
    processor = RaspberryPiVideoProcessor()
    processor.start_processing()

if __name__ == "__main__":
    main()
