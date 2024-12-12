# P6: Hand-Controlled Media Player Using OpenCV and MediaPipe

# Importing required libraries
import cv2  # For video capturing and image processing
import mediapipe as mp  # For hand tracking and landmark detection
import pyautogui  # For simulating keyboard inputs to control media playback

# Initialize MediaPipe drawing utilities and hand solutions
mp_drawing = mp.solutions.drawing_utils  # For drawing landmarks and connections on the image
mp_hands = mp.solutions.hands  # MediaPipe hands solution for hand tracking

# IDs of fingertip landmarks as defined in MediaPipe's hand model
tipIds = [4, 8, 12, 16, 20]

# Variables to store the current gesture state and control actions
state = None  # Tracks the current playback state (e.g., Play or Pause)
Gesture = None  # Placeholder for gesture recognition (not used in this code)

# Set camera resolution
wCam, hCam = 720, 640

# Function to extract the positions of hand landmarks
def fingerPosition(image, handNo=0):
    """
    Returns a list of landmarks for a detected hand.
    Each landmark includes an ID and its x, y pixel coordinates on the image.

    Parameters:
        image: The captured frame from the webcam
        handNo: Index of the hand to process (default is 0 for the first detected hand)

    Returns:
        lmList: A list of [id, x, y] for each landmark
    """
    lmList = []
    if results.multi_hand_landmarks:  # Check if any hands are detected
        myHand = results.multi_hand_landmarks[handNo]  # Get the first hand
        for id, lm in enumerate(myHand.landmark):  # Iterate through landmarks
            h, w, c = image.shape  # Get image dimensions
            cx, cy = int(lm.x * w), int(lm.y * h)  # Convert normalized coordinates to pixels
            lmList.append([id, cx, cy])  # Append the landmark to the list
    return lmList

# Start webcam capture and set resolution
cap = cv2.VideoCapture(1)  # Use camera index 1 (change if needed)
cap.set(3, wCam)  # Set width of the webcam feed
cap.set(4, hCam)  # Set height of the webcam feed

# Initialize MediaPipe Hands with confidence thresholds
with mp_hands.Hands(
    min_detection_confidence=0.8,  # Minimum confidence for hand detection
    min_tracking_confidence=0.5  # Minimum confidence for hand tracking
) as hands:
    while cap.isOpened():  # Continue while the webcam is open
        success, image = cap.read()  # Read a frame from the webcam
        if not success:  # Skip if the frame is empty
            print("Ignoring empty camera frame.")
            continue

        # Process the frame for hand tracking
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)  # Flip and convert BGR to RGB
        image.flags.writeable = False  # Optimize the frame for processing
        results = hands.process(image)  # Detect hands in the frame

        # Draw hand landmarks on the image
        image.flags.writeable = True  # Make the frame writeable again
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB back to BGR for display
        if results.multi_hand_landmarks:  # If hands are detected
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS  # Draw landmarks and connections
                )

        # Get the positions of hand landmarks
        lmList = fingerPosition(image)
        if len(lmList) != 0:  # If landmarks are detected
            fingers = []
            # Check the positions of the fingers (except the thumb)
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:  # Finger is up
                    fingers.append(1)
                else:  # Finger is down
                    fingers.append(0)

            # Count how many fingers are up
            totalFingers = fingers.count(1)
            print(totalFingers)

            # Media control actions based on finger count and position
            if totalFingers == 4:  # All fingers up
                state = "Play"
            if totalFingers == 0 and state == "Play":  # All fingers down
                state = "Pause"
                pyautogui.press('space')  # Simulate space key to pause/play
                print("Space")
            if totalFingers == 1:  # One finger up
                if lmList[8][1] < 300:  # Finger points left
                    print("left")
                    pyautogui.press('left')  # Simulate left arrow key
                if lmList[8][1] > 400:  # Finger points right
                    print("Right")
                    pyautogui.press('right')  # Simulate right arrow key
            if totalFingers == 2:  # Two fingers up
                if lmList[9][2] < 210:  # Fingers point up
                    print("Up")
                    pyautogui.press('up')  # Simulate up arrow key
                if lmList[9][2] > 230:  # Fingers point down
                    print("Down")
                    pyautogui.press('down')  # Simulate down arrow key

        # Display the webcam feed with annotations
        cv2.imshow("Media Controller", image)

        # Exit the loop if the 'q' key is pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

# Release resources and close windows
cv2.destroyAllWindows()
