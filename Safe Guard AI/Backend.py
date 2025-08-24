from flask import Flask, render_template, Response
from flask_socketio import SocketIO, emit
import cv2
import mediapipe as mp
import threading
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# List of IP camera URLs
IP_CAMERA_URLS = [
    "http://192.168.196.248:8080/video",
]

# Global variables for managing streaming
streaming_camera = None
streaming_priority = {}  # {camera_index: timestamp}
streaming_lock = threading.Lock()

def is_help_gesture(hand_landmarks):
    """Detects the 'help' gesture: open palm with thumb folded."""
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    fingers_extended = (
        index_tip.y < index_mcp.y and
        middle_tip.y < index_mcp.y and
        ring_tip.y < index_mcp.y and
        pinky_tip.y < index_mcp.y
    )
    thumb_folded = thumb_tip.y > index_mcp.y and thumb_ip.y > index_mcp.y

    return fingers_extended and thumb_folded

def detect_gesture(camera_index):
    global streaming_camera, streaming_priority
    cap = cv2.VideoCapture(IP_CAMERA_URLS[camera_index])

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"Failed to fetch video stream from camera {camera_index}.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                if is_help_gesture(hand_landmarks):
                    print(f"HELP Gesture Detected on camera {camera_index}!")
                    with streaming_lock:
                        streaming_priority[camera_index] = time.time()
                        streaming_camera = max(streaming_priority, key=streaming_priority.get)
                    socketio.emit("update_stream", {"camera_index": streaming_camera})
                    break

    cap.release()

def generate_frames():
    global streaming_camera
    current_camera = None
    cap = None

    while True:
        with streaming_lock:
            if streaming_camera != current_camera:
                if cap:
                    cap.release()
                current_camera = streaming_camera
                if current_camera is not None:
                    cap = cv2.VideoCapture(IP_CAMERA_URLS[current_camera])

        if cap and current_camera is not None:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (700, 450))
            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + b'\r\n')

@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/")
def index():
    return render_template("index.html", camera_count=len(IP_CAMERA_URLS))

if __name__ == "__main__":
    for i in range(len(IP_CAMERA_URLS)):
        socketio.start_background_task(detect_gesture, i)
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
