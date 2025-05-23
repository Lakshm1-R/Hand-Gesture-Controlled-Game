#  command to install required libraries
#  !pip install cvzone opencv-python pyautogui mediapipe


import cv2
import cvzone
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# Initialize webcam
cap = cv2.VideoCapture(0)  # Use default webcam
cap.set(3, 640)  # Width (optimize for low RAM)
cap.set(4, 480)  # Height

# Initialize hand detector
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1,
                        detectionCon=0.6, minTrackCon=0.5)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=True, flipType=True)  # Flip OFF for correct left/right

    action = ""  # To store action text

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Show finger state on screen (0 or 1)
        for i, finger in enumerate(fingers):
            cv2.putText(img, f'{finger}', (50 + i * 50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Gesture Detection
        if fingers == [1, 0, 0, 0, 0]:
            action = "Move Left"
            pyautogui.press('left')

        elif fingers == [0, 0, 0, 0, 1]:
            action = "Move Right"
            pyautogui.press('right')

        elif fingers == [1, 1, 1, 1, 1]:
            action = "Jump"
            pyautogui.press('up')

        elif fingers == [0, 0, 0, 0, 0]:
            action = "Skid"
            pyautogui.press('down')

        elif fingers == [0, 1, 0, 0, 0]:
            action = "Idle (Do Nothing)"  # No key press


    # Show the action label on the webcam feed
    if action:
        cv2.putText(img, action, (50, 420),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

    # Display webcam image
    cv2.imshow("Hand Gesture Control", img)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
