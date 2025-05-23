# Hand-Gesture-Controlled-Game
Control keyboard games using real-time hand gestures and webcam.

# 🖐️ Hand Gesture Controlled Game 🎮

A fun and interactive Python project that lets you control any keyboard-based game using hand gestures detected via your webcam! This uses computer vision with OpenCV and MediaPipe (via cvzone) and sends keystrokes using PyAutoGUI.

---

## 🎯 Features

- 👋 Detects hand gestures in real-time
- 🎮 Maps specific gestures to game controls:
  - **Thumb Up** → Move Left ⬅️
  - **Pinky Up** → Move Right ➡️
  - **All Fingers Up** → Jump ⬆️
  - **Fist (No Fingers Up)** → Skid ⬇️
- 💻 Works with simple keyboard-based games like the Chrome Dinosaur Game
- 🧠 Uses cvzone’s hand tracking for accurate detection

---

## 🛠️ Technologies Used

| Library         | Purpose                                 |
|------------------|-----------------------------------------|
| `cv2` (OpenCV)   | Webcam access, real-time video display  |
| `cvzone`         | Simplifies OpenCV tasks, hand tracking  |
| `pyautogui`      | Sends simulated keystrokes              |
| `HandTrackingModule` | Detects hand landmarks & finger positions |

---


## 🚀 How to Run

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/your-username/Hand-Gesture-Controlled-Game.git
cd Hand-Gesture-Controlled-Game
