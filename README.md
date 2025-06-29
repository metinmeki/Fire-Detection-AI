# Fire Detection AI 🔥
[![Python](https://img.shields.io/badge/python-3.2-blue.svg)]
[![GitHub issues](https://img.shields.io/github/issues/metinmeki/Fire-Detection-AI)](https://github.com/metinmeki/Fire-Detection-AI/issues)

---

## 🚀 Project Overview

**Fire Detection AI** is a real-time fire detection system leveraging the power of the **YOLO (You Only Look Once)** algorithm. It analyzes video streams or images to detect fire quickly and accurately, enabling timely alerts to help prevent fire-related disasters.

---

## ⚙️ Key Features

- Real-time fire detection using state-of-the-art YOLO object detection  
- Supports live webcam streams and video file inputs  
- Trained on a custom fire dataset for improved accuracy ([Dataset link](https://www.kaggle.com/datasets/metinmekiabullrahman/fire-detection))  
- Highlights fire regions with clear bounding boxes  
- Designed for easy integration with alerting or logging systems  

---

## 🛠️ Technologies & Tools

- Python 3.2  
- OpenCV for image and video processing  
- YOLO (Darknet / YOLOv5 / YOLOv8 — specify your version)  
- PyTorch or TensorFlow depending on YOLO implementation  
- NumPy for numerical operations  

---

## 📁 Project Structure

Fire-Detection-AI/
├── main.py # Main script to execute fire detection
└── model/ # YOLO trained weights and configuration files

yaml
Copy
Edit
 
---

## 📖 How It Works

1. Loads the YOLO model from the `model/` directory  
2. Captures frames from the webcam or video file specified by the user  
3. Runs inference on each frame to detect fire regions  
4. Draws bounding boxes around detected fire areas in real-time  
5. (Optional) Can be extended to trigger alerts or notifications  

---

## 🔮 Future Improvements

- Integrate alert and notification system (email, SMS, push notifications)  
- Support for multi-camera and network video streams  
- Optimize model for deployment on embedded and edge devices  

---

## 📄 License

This project is released under the **MIT License**, which means you are free to use, modify, and distribute it — even commercially — as long as you include this original license and attribution.

Feel free to use this project however you like!  
If you make improvements or fixes, contributions are always welcome but not required.

---

© 2025 Metin Amedi

---

## 📬 Contact

Developed by **Metin Amedi**  
Email: [Metinmeki99@gmail.com]

---

⭐ If you find this project useful, please consider starring the repository!
