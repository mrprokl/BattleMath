try:
    from raspberry_video import RaspberryPiVideoProcessor
except ImportError:
    RASPBERRY = False
    from macos_video import MacosVideoProcessor
    print("picamera not installed!!")


def main():
    if RASPBERRY:
        processor = RaspberryPiVideoProcessor()
        processor.start_pure_video()

        

        processor.draw_detections(frame, detections)

    else:
        processor = MacosVideoProcessor()
        processor.loop_frame_process()
        # processor.start_processing()

if __name__ == "__main__":
    main()