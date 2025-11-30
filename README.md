# VisionARM
**VisionARM: A Vision Based Hand Gesture Controlled Robotic Arm System**

> **University of Florida | Artificial Intelligence System Project**

VisionARM is an intelligent hand gesture controlled robotic arm system, that uses computer vision and machine learning to interpret hand gestures in real-time.
The system leverages Google MediaPipe for precise hand landmark detection and a custom-trained Support Vector Machine (SVM) classifier to recognize 8 distint hand gesture labels with 98.5% accuracy. Build with accessibility and usability in mind, VisionARM features a complete User interface powered by Gradio, secure user authentication, real-time performance monitoring with Prometheus, and seamleass Arduino integration for physical robotic arm deployment.
From introducing customization in industrial setting to being an assistive technology, VisionARM demonstrates the potential of vision-based interfaces in creating more natural and accessible human-robot interaction systems. The entire pipeline—from gesture detection to command execution—operates in real-time with an average latency of just ~20ms, making it suitable for practical applications requiring responsive control.
Key Achievement: 98.5% gesture classification accuracy with sub-20ms latency on a dataset of 2,000 hand gesture samples.

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [System Architecture](#️-system-architecture)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Quick Set up and Usage Guide](#quick-set-up-and-usage-guide)
- [Dataset](#-dataset)
- [Hardware Integration](#-hardware-integration)
- [Performance Monitoring](#-performance-monitoring)
- [Technologies Used](#️-technologies-used)
- [Future Enhancements](#-future-enhancements)
- [Acknowledgments](#-acknowledgments)
- [Contact](#-contact)

---

## ✨ Features

### 🎯 Core Capabilities
- **Real-Time Hand Gesture Recognition**: Detects and classifies 8 different hand gestures using MediaPipe and SVM
- **High Accuracy**: Achieves **98.5%** classification accuracy on test data
- **Low Latency**: Average processing time of ~20ms per frame for real-time responsiveness
- **Web-Based Interface**: Intuitive Gradio UI accessible from any browser

### 🔐 User Management
- Secure user registration and authentication system
- Password hashing with SHA-256 encryption
- User feedback collection and storage
- Session management with persistent login state

### 📊 Performance Monitoring
- Real-time FPS and latency tracking
- System resource monitoring (CPU, Memory, GPU)
- Prometheus metrics integration
- Live performance visualization with Plotly graphs
- Historical performance data logging

### 🤖 Hardware Integration
- Arduino serial communication for robotic arm control
- Real-time command transmission
- Configurable serial port settings
- Hardware connection status monitoring

### 🎨 User Interface Features
- Live webcam feed with hand landmark visualization
- Real-time gesture prediction display
- Confidence score visualization
- System status indicators
- Interactive performance dashboards
- User feedback system

---

## Demo

<p align="center">
  <img src="./Project_UI_Demo_Video.gif" width="800">
</p>

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     VisionARM System                        │
└─────────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼─────┐      ┌─────▼──────┐     ┌─────▼──────┐
   │  Camera  │      │  Gradio    │     │  Arduino   │
   │  Input   │      │  Web UI    │     │  Hardware  │
   └────┬─────┘      └─────┬──────┘     └─────▲──────┘
        │                  │                  │
        │           ┌──────▼──────┐           │
        │           │    User     │           │
        │           │ Management  │           │
        │           └─────────────┘           │
        │                                     │
   ┌────▼─────────────────────────────────────┴──────────┐
   │           Hand Gesture Processing Pipeline          │
   ├─────────────────────────────────────────────────────┤
   │  1. MediaPipe Hand Detection                        │
   │  2. Feature Extraction (10D Binary Vector Encoding) │
   │  3. SVM Classification (8 Gesture Classes)          │
   │  4. Command Mapping & Transmission                  │
   └─────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   ┌────▼──────┐     ┌─────▼──────┐     ┌─────▼──────┐
   │Performance│     │  Gesture   │     │  Database  │
   │Monitoring │     │ Prediction │     │  Storage   │
   └───────────┘     └────────────┘     └────────────┘
```
VisionARM implements an end-to-end computer vision and machine learning pipeline for real-time hand gesture recognition and robotic arm control. The system achieves **98.5% accuracy** with **~20ms latency**, making it suitable for responsive real-time applications.

### Model Layers

```
┌───────────────────────────────────────────────────────────────────┐
│                    VisionARM System Stack                         │
├───────────────────────────────────────────────────────────────────┤
│  Layer 1: Input Processing     │  Webcam → OpenCV → MediaPipe     │
│  Layer 2: Feature Extraction   │  Hand Landmarks → Binary Encoding│
│  Layer 3: Classification       │  SVM (RBF Kernel)                │
│  Layer 4: Command Translation  │  Gesture → Arduino Commands      │
│  Layer 5: Monitoring           │  Prometheus Metrics              │
│  Layer 6: User Interface       │  Gradio Web UI                   │
└───────────────────────────────────────────────────────────────────┘
```

---
## 🚀 Installation

### Prerequisites

- **Python**: 3.11 or higher
- **Webcam**: Built-in or USB camera
- **Operating System**: Windows, macOS, or Linux
- **Arduino**: For hardware integration

### Step 1: Clone the Repository

```bash
git clone https://github.com/Shiva-a1/VisionARM.git
cd visionarm
```

### Step 2: Create Virtual Environment

```bash
# Using conda (recommended)
conda create -n visionarm python=3.11
conda activate visionarm

# Or using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Core dependencies
pip install mediapipe opencv-python numpy pandas
pip install scikit-learn joblib

# Web interface
pip install gradio

# Hardware communication
pip install pyserial

# Monitoring and visualization
pip install prometheus-client psutil plotly
```
---

## 📁 Project Structure

```
visionarm/
│
├── main.ipynb                          # Main application notebook
├── Classifcation_Model_Training.ipynb  # Model training pipeline
├── user_manager.py                     # User authentication system
├── README.md                           # Project documentation
├── VisionARM.code-workspace            # VS Code workspace
├── metadata.json                       # Dataset metadata
│
├── Data/
│   ├── visionarm_dataset_v01_01.csv   # Training dataset
│   └──users_database.csv             # User credentials
│
├── SVM_Models/
│   └── best_label_classification_model.pkl         # Trained SVM model
│
├──trial.ipynb                       # trial notebook for rough work
└── arduino_code.txt                 # Text file containing Arduino code
```
---
## Quick Set up and Usage Guide
1. **Clone the Repository**
- Clone the VisionARM repository from the link provided above.

2. **Open the project Folder**
- Open the Project Folder in you local IDE (VS Code Prefered).

3. **Install Arduino Extension**
- Install the PlatformIO Extension in VSCode. One installed created a new project and then navigate to ```main.cpp``` file present inside ```src``` folder. 
- From our ```VisionARM``` folder, go to ```arduino_code.txt``` and copy the Arduino code from there and paste it in ```main.cpp``` file of the Arduino project folder. Once done, do make sure that you Arduino Hardware is properly connected to the local system (laptop), and all the port labels in the Arduino code matches correctly with you Arduino board. 
- Once done press the ✅ button at the bottom left and press the ➡️ next to it. This will over write the Arduino code in the Arduino board's memory.

4. **Integrating Arduino with VisionARM project**
- Navigate to ```main.ipynb``` file inside our ```VisionARM``` project folder and go to ```8. Arduino Serial Communication``` section and edit the Serial Port value to the one you are using to connect Arduino Hardware to your local device.

5. **Launch the AI System**
- Navigate to ```user_manager.py``` file and run it.
- If it runs successfully, then navigate to ```main.ipynb``` file and run all the cells.
- If every cell runs without any error, directly navigate to the last cell, which displays our system's UI.

6. **Accessing the User Interface**
- Register/Login to access the system and then press `Start Detection' button. Then your system's camera would turn on, where you will perform hand gestures, based on which the Arduino system would perform operations, and metrics plots on the UI would keep on updating.

---

## 📊 Dataset

### Dataset Overview

- **Name**: `visionarm_dataset_v01_01.csv`
- **Version**: v01_01
- **Creation Date**: October 19, 2025
- **Total Samples**: 2,000
- **Features**: 10 (binary finger states)
- **Classes**: 8 gesture types

### Feature Description

Each sample contains 10 binary features representing finger states:

| Feature | Description |
|---------|-------------|
| `left_thumb` | Left hand thumb (1=raised, 0=closed) |
| `left_index` | Left hand index finger |
| `left_middle` | Left hand middle finger |
| `left_ring` | Left hand ring finger |
| `left_pinky` | Left hand pinky finger |
| `right_thumb` | Right hand thumb |
| `right_index` | Right hand index finger |
| `right_middle` | Right hand middle finger |
| `right_ring` | Right hand ring finger |
| `right_pinky` | Right hand pinky finger |

### Class Distribution

```
stop     : 200 samples
grab     : 200 samples
drop     : 200 samples
up       : 200 samples
down     : 200 samples
left     : 200 samples
right    : 200 samples
invalid  : 600 samples
```

### Data Sources

The dataset combines:
1. **Synthetic Data**: Manually created binary patterns for gesture classes
2. **Real Data**: MediaPipe-encoded hand landmark data from real-time captures

---

## 🔌 Hardware Integration

### Arduino Setup

#### Hardware Requirements
- Arduino Uno/Mega/Nano
- Servo motors (typically 4-6 for robotic arm)
- Power supply (5V/12V depending on servos)
- USB cable for serial communication

#### Arduino Code:
- Copy paste the Arduino code present in ```arduino.txt``` to ```main.cpp``` file in ```src``` folder present in Arduino project we created in PlatformIO extension in VS Code.
- Download all the required libraries and edit the port serial numbers for each servo-motor based on your hardware device.
- Once done press the ✅ button at the bottom left and press the ➡️ next to it. This will over write the Arduino code in the Arduino board's memory.

### Serial Communication

#### Python Configuration

```python
import serial
import time

arduino = serial.Serial('/dev/tty.usbserial-10', 9600)  # Change based on your system
time.sleep(2) 

def send_label(label):
    message = label + '\n'
    arduino.write(message.encode())
    print(label)
```

#### Port Detection

**Windows**: COM3, COM4, etc.
**macOS**: /dev/tty.usbserial-*
**Linux**: /dev/ttyUSB0, /dev/ttyACM0

---

## 📈 Performance Monitoring

### Metrics Tracked

#### System Metrics
- **FPS (Frames Per Second)**: Real-time frame processing rate
- **Latency**: Average processing time per frame
- **CPU Usage**: Percentage of CPU utilization
- **Memory Usage**: RAM consumption

#### Application Metrics
- **Total Frames Processed**: Cumulative frame count
- **Gesture Distribution**: Count of each gesture detected
- **Session Duration**: Active detection time

### Prometheus Integration

The system exposes metrics on port 8000:

```bash
# Access metrics endpoint
curl http://localhost:8000
```

**Available Metrics**:
- `gesture_predictions_total`: Counter for each gesture type
- `prediction_latency_seconds`: Histogram of processing times
- `cpu_usage_percent`: Current CPU usage
- `memory_usage_percent`: Current memory usage

### Visualization

Real-time plots include:
- **FPS Over Time**: Line graph of frame rate
- **Latency Distribution**: Histogram of processing times
- **Resource Usage**: CPU and Memory usage over time
- **Gesture Frequency**: Bar chart of detected gestures

---

## 🛠️ Technologies Used

### Computer Vision & ML
- **MediaPipe** (v0.10.0+): Hand landmark detection and tracking
- **OpenCV** (v4.8.0+): Image processing and video capture
- **scikit-learn** (v1.3.0+): SVM classifier and model evaluation
- **NumPy** (v1.24.0+): Numerical computations
- **Pandas** (v2.0.0+): Data manipulation and analysis

### Web Interface
- **Gradio** (v4.0.0+): Interactive web UI framework
- **Plotly** (v5.17.0+): Interactive visualizations

### System & Monitoring
- **Prometheus Client**: Metrics collection and exposure
- **psutil**: System resource monitoring
- **Threading**: Concurrent processing

### Hardware Communication
- **PySerial** (v3.5+): Arduino serial communication

### Security
- **hashlib**: Password hashing (SHA-256)

---

## 🔮 Future Enhancements

### Planned Features

- [ ] **Drift Detection**: Drift detection using NannyML.
- [ ] **Enhanced Gesture Set**: Support for 20+ gestures including custom gestures
- [ ] **Multi-Hand Tracking**: Independent control with two hands
- [ ] **Mobile App**: Native iOS/Android applications
- [ ] **Gesture Recording**: Save and replay gesture sequences
- [ ] **Cloud Integration**: Remote control and monitoring
- [ ] **Gesture Customization**: User-defined gesture mapping
- [ ] **Multi-User Support**: Collaborative control modes

### Research Directions

- **Adaptive Learning**: Online learning from user corrections
- **Context-Aware Recognition**: Environment and task-specific gestures
- **Robustness Improvements**: Better performance in varied lighting
- **Latency Optimization**: Sub-10ms processing pipeline
- **Energy Efficiency**: Optimizations for embedded systems

---

## 🤝 Acknowledgments

### Frameworks
- **Google MediaPipe Team**: For the excellent hand tracking solution

### University Support
- **University of Florida**: For project support and resources

### Inspiration
This project was inspired by the growing need for intuitive human-robot interaction systems and the potential of computer vision in creating accessible control interfaces.

### Special Thanks
- **Professor Andrea Ramirez Salgado** for her support in providing all the required hardware resources, her valuable guidance and feedback.

---

## 📞 Contact

### Project Author

**VisionARM Developer**
- 📧 Email: shivansh.ade@ufl.edu
- 🌐 Website: [visionarm-project.github.io](https://github.com/Shiva-a1/VisionARM)

---