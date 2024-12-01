# try:
from picamera2 import Picamera2, Preview
# except ImportError:
#     NO_PICAMERA = True
#     print("picamera not installed!!")
import cv2
import numpy as np
import time
import threading
from icecream import ic

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

        self.net = cv2.dnn.readNetFromDarknet("BattleMath/models/yolov3.cfg", "BattleMath/models/yolov3.weights")
        self.net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


    def start_pure_video(self):
        self.picam2.start()
        time.sleep(1)  # Warm-up time
        try:
            while True:

                cv2.imshow("Raw Video", self.picam2.capture_array())

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            self.picam2.stop()

    def start_processing(self):
        self.picam2.start()
        time.sleep(2)  # Warm-up time

        try:
            while True:
                # Capture frame
                frame = self.picam2.capture_array()
                
                # Basic image processing
                # processed_frame = self._process_frame(frame)
                processed_frame = self._process_frame_tinyyolo(frame)
                
                
                # Display processed frame
                cv2.imshow("Processed Video", processed_frame)
                
                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        
        finally:
            self.picam2.stop()
            cv2.destroyAllWindows()

    def _process_frame_black_white_edges(self, frame):
        # Example processing: grayscale conversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Optional: Simple edge detection
        edges = cv2.Canny(gray, 50, 150)
        
        return edges
    
    def _process_frame_black_white(self, frame):
        # Example processing: grayscale conversion
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Optional: Simple edge detection
        edges = cv2.Canny(gray, 50, 150)

        # Optional: Apply a color map for better visualization
        color_edges = cv2.applyColorMap(edges, cv2.COLORMAP_JET)

        return color_edges
    
    def _process_frame_tinyyolo(self, frame):
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        self.net.setInput(blob)
        detections = self.net.forward()
        ic(detections)

        return self._parse_detections(detections, frame)
    
    def _parse_detections(self, detections, frame) -> list:
        height, width = frame.shape[:2]
        confidence_threshold = 0.5
        nms_threshold = 0.4
        
        class_ids = []
        confidences = []
        boxes = []

        # YOLO detection parsing
        for detection in detections[0, 0, :, :]:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            
            if confidence > confidence_threshold:
                # Bounding box coordinates
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

        # Non-maximum suppression to remove overlapping boxes
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_threshold)
        
        # Draw detected objects
        detected_objects = []
        for i in indexes:
            x, y, w, h = boxes[i]
            label = str(self.classes[class_ids[i]])
            confidence = confidences[i]
            
            detected_objects.append({
                'class': label,
                'confidence': confidence,
                'box': (x, y, w, h)
            })
        
        return detected_objects

    
    def draw_detections(self, frame, detections):
        for obj in detections:
            x, y, w, h = obj['box']
            label = f"{obj['class']}: {obj['confidence']:.2f}"
            
            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Draw label
            cv2.putText(
                frame, 
                label, 
                (x, y-10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.5, 
                (0, 255, 0), 
                2
            )
        return frame
