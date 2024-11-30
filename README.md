# Object Detection Tank

## Description
This project implements an Object Detection Tank using YOLO (You Only Look Once) and OpenCV on a Raspberry Pi 4 with a camera. The tank is capable of detecting and following objects in real-time, making it an exciting application of computer vision and robotics.

## Features
- Real-time object detection using YOLO
- Object following capabilities
- Compatible with Raspberry Pi 4
- Utilizes OpenCV for image processing
- Easy setup and configuration

## Requirements
- Raspberry Pi 4 (2GB RAM recommended)
- Raspberry Pi Camera Module
- Python 3.x
- OpenCV
- YOLO weights and configuration files

## Installation

1. **Set up your Raspberry Pi:**
   - Install the latest version of Raspberry Pi OS.
   - Ensure your Raspberry Pi is connected to the internet.

2. **Install Python and OpenCV:**
   ```bash
   sudo apt update
   sudo apt install python3-opencv
   ```

3. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/object-detection-tank.git
   cd object-detection-tank
   ```

4. **Download YOLO weights:**
   - Download the YOLO weights and configuration files from the official YOLO website and place them in the project directory.

5. **Run the application:**
   ```bash
   python3 main.py
   ```

## Usage
- Once the application is running, the tank will start detecting objects in its field of view.
- The tank will follow the detected object based on the programmed logic.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- [YOLO](https://pjreddie.com/darknet/yolo/)
- [OpenCV](https://opencv.org/)

# Authors 
Thomas & Matteo
