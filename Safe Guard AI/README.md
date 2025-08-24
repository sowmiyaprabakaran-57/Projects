# 🛡️ Safeguard AI - AI-Powered CCTV Harassment Detection System

Safeguard AI is an AI-based safety solution designed to protect women in workplace and public environments. By using gesture recognition with CCTV feeds, it automatically detects distress signals (like an open palm gesture) and triggers real-time alerts, video streaming, and emergency responses.

---

## 🎯 Features

- 🖐️ **Open Palm Gesture Detection** via MediaPipe
- 🎥 **Live CCTV Streaming** (30-second triggered stream)
- 🚨 **Real-Time Alert System** to Control Room & Police
- 📍 **Live Location Tracking** during emergencies
- 🎦 **Automatic Video Evidence Recording**
- 📱 **Admin Dashboard for Monitoring**
- 🔐 **Privacy-Aware AI Design**

---

## 🛠️ Tech Stack

| Component     | Technology                     |
|---------------|--------------------------------|
| 👁️ Gesture Detection | MediaPipe, OpenCV              |
| 🧠 AI Model         | TensorFlow / PyTorch (custom) |
| 🧵 Backend          | Flask / Node.js               |
| 🗃️ Database         | MongoDB / Firebase            |
| 🔁 Streaming        | IP Webcam / RTSP + OpenCV     |
| 🔔 Alerts           | Socket.IO, Email/SMS API      |
| 🌐 Dashboard        | HTML, Tailwind, JavaScript    |

---

## 🗂️ Project Folder Structure

```

safeguard-ai/
├── backend/
│   ├── app.py
│   ├── gesture\_detector.py
│   ├── video\_streamer.py
│   └── utils/
├── frontend/
│   ├── index.html
│   ├── styles/
│   └── scripts/
├── models/
│   └── open\_palm\_model.tflite
├── requirements.txt
└── README.md

````

---

## 🚀 How It Works

1. 📹 **Camera Feed** is continuously monitored.
2. 🖐️ **Open palm gesture** is detected using MediaPipe.
3. 🔁 **30-second video stream** is triggered via IP cam.
4. 🚨 **Alert sent** to control room and police with location.
5. 🎦 **Video evidence** is captured and stored securely.
6. 📍 **Live location** is shared to nearest police station.

---

## 🧪 Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/thiyaneshwars/safeguard-ai.git
cd safeguard-ai
````

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Backend Server

```bash
cd backend
python app.py
```

### 4. Launch Frontend Dashboard

Open `frontend/index.html` in your browser

---

## 🧠 Gesture Detection Overview

Safeguard AI uses MediaPipe to recognize a specific **open palm gesture** to signify distress. Upon detection:

* Live stream is activated
* Control room is notified
* Police are alerted with live location
* Evidence is recorded

---

## 📈 Future Scope

* 🔐 Face authentication before gesture detection
* 🌍 Multilingual speech-based SOS
* 🤖 ML-enhanced threat-level estimation
* ☁️ Cloud sync and log visualization

---

## 🧑‍💻 Contributors

* **Sowmiya P**
  👨‍🎓 AIML Student | AI Enthusiast
  📧 [sowmiya1157@gmail.com](mailto:sowmiya1157@g.mail.com)
 
---

## 📄 License

This project is under development and open-sourced for academic and non-commercial use only.

