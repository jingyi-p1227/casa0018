import cv2
import numpy as np
from picamera2 import Picamera2
from edge_impulse_linux.image import ImageImpulseRunner

# REFINED ATTEMPT: Synchronous capture to avoid driver deadlock
MODEL_PATH = "/home/morn/casa0018_model.eim"

def main():
    runner = ImageImpulseRunner(MODEL_PATH)
    runner.init()
    
    # Switch to Picamera2: The native camera library for Raspberry Pi 5
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
    picam2.configure(config)
    picam2.start()

    print("System ready. Monitoring fatigue via synchronous capture...")

    try:
        while True:
            # Capturing raw array to bypass GStreamer pipeline issues
            frame = picam2.capture_array()
            
            # Pre-processing: Resize to model input (96x96) and Convert to Grayscale
            img = cv2.resize(frame, (96, 96))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            
            # CRITICAL FIX: Convert NumPy array to a flat Python List 
            # to resolve memory alignment/deadlock issues on Pi 5.
            features = img.flatten().tolist()
            
            res = runner.classify(features)
            print(res)
    finally:
        picam2.stop()
        runner.stop()

if __name__ == "__main__":
    main()