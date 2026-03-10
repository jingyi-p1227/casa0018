# Project Idea: Edge-Based Multimodal Driver Fatigue Monitoring System

## 1. Problem Domain
The problem domain I am working on is **Driver Safety and In-Cabin Sensing**. Driver fatigue is a leading cause of traffic accidents. However, existing solutions often rely on cloud computing. Sending a live video feed of a driver's face to the cloud raises massive privacy concerns and suffers from latency issues (e.g., losing connection in a tunnel). Therefore, my goal is to build a completely offline, privacy-preserving driver monitoring system that runs entirely on the edge.

## 2. Physical Platforms
* **Edge Computing Node:** Raspberry Pi 5.
* **Sensor Input:** Standard USB camera (or Pi Camera) to capture the real-time video stream of the driver's face.
* **Actuator Output:** Raspberry Pi's GPIO pins to trigger a physical alert (e.g., a buzzer and a flashing red LED) the moment severe fatigue is detected.

## 3. Planned Techniques & Architecture
Technically, I will use **MediaPipe**, which runs highly optimized TensorFlow Lite models under the hood [1]. 

### Vision Pipeline (Raspberry Pi 5)
* **OpenCV:** To capture raw image frames from the video stream.
* **MediaPipe Face Mesh:** To extract 468 facial landmarks in real-time [2].
* **EAR Calculation:** Using 6 specific landmarks around the eyes, I will mathematically calculate the Eye Aspect Ratio (EAR) in real-time [3]. By analyzing this ratio over a time-series window, the system can distinguish between a normal blink and a dangerous microsleep.

## 4. Data Collection Strategy
Instead of downloading a generic dataset, I will construct a **custom calibration and testing dataset**. I will record my own face under various conditions to calibrate the EAR threshold, specifically focusing on edge cases such as low-light environments, wearing glasses, and wearing masks.

### Calibrated Thresholds
* **Baseline:** Normal forward gaze, normal blinking rate.
* **Drowsy:** Frequent blinking, significantly slowed blink rate.
* **Sleeping:** Eyes closed for >2 seconds, head drooping.

## 5. Future Work & Scalability
While this MVP focuses purely on offline visual detection, the architecture is highly scalable. In the future, I plan to integrate an **Arduino Nano** for audio detection (listening for yawns via an Edge Impulse audio classifier).

---

## References
[1] Warden, P., & Situnayake, D. (2019). *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*. O'Reilly Media.

[2] Grishchenko, I., Bazarevsky, V., Zanfir, A., Tkachenka, P., et al. (2020). Attention Mesh: High-fidelity Face Mesh Prediction in Real-time. *arXiv preprint arXiv:2006.10962*.

[3] Soukupová, T., & Čech, J. (2016). Real-Time Eye Blink Detection using Facial Landmarks. *21st Computer Vision Winter Workshop (CVWW2016)*, 1-8.
