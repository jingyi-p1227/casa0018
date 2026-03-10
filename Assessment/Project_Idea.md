# Project Idea: Edge-Based Multimodal Driver Fatigue Monitoring System

## 1. Problem Domain
[cite_start]The problem domain I am working on is Driver Safety and In-Cabin Sensing[cite: 71]. [cite_start]Driver fatigue is a leading cause of traffic accidents[cite: 72]. [cite_start]However, existing solutions often rely on cloud computing[cite: 72]. [cite_start]Sending a live video feed of a driver's face to the cloud raises massive privacy concerns and suffers from latency issues—for example, losing connection in a tunnel[cite: 73]. [cite_start]Therefore, my goal is to build a completely offline, privacy-preserving driver monitoring system that runs entirely on the edge[cite: 74].


## 2. Physical Platforms
* [cite_start]**Edge Computing Node:** For the physical platform, I will use a Raspberry Pi 5 as my core edge computing node[cite: 77]. 
* [cite_start]**Sensor Input:** I will use a standard USB camera (or Pi Camera) to capture the real-time video stream of the driver's face[cite: 78].
* [cite_start]**Actuator Output:** I will use the Raspberry Pi's GPIO pins to trigger a physical alert—such as a buzzer and a flashing red LED—the moment severe fatigue is detected[cite: 79].

## 3. Planned Techniques & Architecture
[cite_start]Technically, I will use MediaPipe, which runs highly optimized TensorFlow Lite models under the hood[cite: 82]. 

### Vision Pipeline (Raspberry Pi 5)
[cite_start]The vision pipeline utilizes Python, OpenCV, and MediaPipe (TensorFlow Lite) to calculate the EAR[cite: 99]:
* [cite_start]**OpenCV:** Used to capture every raw image frame from the video stream[cite: 104].
* [cite_start]**MediaPipe (Face Mesh Model):** Used to extract 468 facial landmarks in real-time[cite: 105, 107]. 
* [cite_start]**EAR Calculation:** Instead of a heavy object detection model, I will use 6 specific landmarks around the eyes [cite: 108] [cite_start]to mathematically calculate the Eye Aspect Ratio (EAR) in real-time[cite: 83, 84, 109]. [cite_start]By analyzing this ratio over a time-series window, the system can distinguish between a normal, fast blink and a dangerous microsleep[cite: 85].


> [cite_start]**Note on Tool Selection:** MediaPipe is an open-source, cross-platform framework developed by Google[cite: 106]. [cite_start]Because it is powered by TensorFlow Lite and specifically optimized for CPU inference, it allows my driver fatigue detection system to run smoothly and entirely offline on a Raspberry Pi, without needing a heavy GPU[cite: 106].

## 4. Data Collection Strategy
[cite_start]Instead of downloading a generic dataset from the internet, I will construct a custom calibration and testing dataset[cite: 88]. [cite_start]I will record my own face under various conditions to calibrate the EAR threshold[cite: 89]. 

[cite_start]More importantly, I will collect data focusing on edge cases—such as recording in low-light environments, wearing glasses, and wearing masks[cite: 90]. [cite_start]This self-collected dataset will allow me to test the system's robustness and mathematically define the exact threshold where 'drowsiness' begins[cite: 91].

### [cite_start]Calibrated Thresholds [cite: 100]
* [cite_start]**Baseline:** Normal forward gaze, normal blinking (正常看前方，正常眨眼)[cite: 101].
* [cite_start]**Drowsy:** Frequent blinking, slowed blink rate (频繁眨眼，眨眼速度变慢)[cite: 102].
* [cite_start]**Sleeping:** Eyes closed for more than two seconds, head drooping (闭眼超过两秒，头部下垂)[cite: 103].

## 5. Future Work & Scalability
[cite_start]Finally, while this MVP focuses purely on offline visual detection, the architecture is highly scalable[cite: 95]. [cite_start]In the future, I plan to integrate an Arduino Nano for audio detection (listening for yawns), and eventually pass these multimodal triggers to build a comprehensive system[cite: 96].

### Proposed Audio Pipeline
* [cite_start]**Hardware:** Arduino Nano[cite: 96, 110].
* [cite_start]**Software:** Edge Impulse -> audio classifier targeting "Yawn" sounds[cite: 110].

---

## References
* Soukupová, T., & Čech, J. (2016). [cite_start]Real-Time Eye Blink Detection using Facial Landmarks[cite: 112]. [cite_start]*In 21st Computer Vision Winter Workshop (CVWW2016)* (pp. 1-8)[cite: 113].
* [cite_start]Grishchenko, I., Bazarevsky, V., Zanfir, A., Tkachenka, P., ... & Matsoka, M. (2020)[cite: 114]. [cite_start]Attention Mesh: High-fidelity Face Mesh Prediction in Real-time[cite: 115]. [cite_start]*arXiv preprint arXiv:2006.10962*[cite: 115].
* Warden, P., & Situnayake, D. (2019). *TinyML: Machine Learning with TensorFlow Lite on Arduino and Ultra-Low-Power Microcontrollers*. [cite_start]O'Reilly Media[cite: 116].
