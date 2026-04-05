# Raspberry Pi 5 Deployment Technical Retrospective

## 1. Project Objective
The goal was to deploy a real-time driver fatigue detection model (Eye-State Classification) locally on a **Raspberry Pi 5** using the **IMX708 Camera Module**.

## 2. The Core Challenge: Driver-Inference Deadlock
While the model achieved high accuracy in WebAssembly (Mobile/Web) environments, deployment on the Raspberry Pi 5 hardware encountered a critical system-level hang. 

### Technical Analysis:
* **Architecture Shift**: Raspberry Pi 5 introduces the new **PiSP (Image Signal Processor)**, moving away from the legacy V4L2 drivers. 
* **SDK Incompatibility**: The Edge Impulse Linux SDK utilizes `GStreamer` with `v4l2src`, which fails to negotiate memory buffers with the new Pi 5 kernel (Bookworm).
* **Resource Contention**: Initializing the AI Inference engine (`runner.init()`) locks hardware interrupts that the camera driver requires, causing a permanent block during image capture.

## 3. Iterative Debugging Process
* **v1 (Standard SDK)**: Failed. Standard GStreamer pipeline cannot find the camera device on Pi 5.
* **Stable (Synchronous Capture)**: Attempted to use native `Picamera2` with manual memory flattening (`tolist()`). Successfully bypassed some memory issues but remained blocked by low-level driver locks.
* **Final Gate (Pipe Bypass)**: Decoupled camera and AI processes using a Linux pipe. This proved the hardware was functional, though real-time alignment with the SDK remained unstable.

## 4. Conclusion & Learning Synthesis
The logic and dataset of the fatigue detection system were fully validated via **Mobile/Web Browser platforms**. The Raspberry Pi 5 deployment phase provided significant insight into **Embedded Linux Driver architectures** and the challenges of deploying AI on cutting-edge hardware platforms.
