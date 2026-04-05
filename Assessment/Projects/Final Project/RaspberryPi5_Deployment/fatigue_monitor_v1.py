import cv2
import os
from edge_impulse_linux.image import ImageImpulseRunner

# INITIAL ATTEMPT: Standard implementation following official documentation
MODEL_PATH = "/home/morn/casa0018_model.eim"

def main():
    # Initialize the runner with the exported .eim model
    runner = ImageImpulseRunner(MODEL_PATH)
    model_info = runner.init()
    print("AI Engine initialized. Project Name: " + model_info['project']['name'])
    
    print("Starting camera stream via standard SDK...")
    
    # FAILURE POINT: The Raspberry Pi 5 architecture (PiSP) is incompatible 
    # with the GStreamer/v4l2src pipeline used in this default method.
    for res, img in runner.classifier():
        if "classification" in res:
            print(res['classification'])

if __name__ == "__main__":
    main()