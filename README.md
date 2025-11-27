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
- [System Architecture](#-system-architecture)
- [Demo](#-demo)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Guide](#-usage-guide)
- [Dataset](#-dataset)
- [Model Training](#-model-training)
- [Gesture Commands](#-gesture-commands)
- [Hardware Integration](#-hardware-integration)
- [Performance Monitoring](#-performance-monitoring)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [Future Enhancements](#-future-enhancements)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

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