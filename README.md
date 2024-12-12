# P6-Hand-Controlled-Media-Player-Using-OpenCV-and-MediaPipe

This project is an innovative system for controlling media playback using hand gestures, built with Python and leveraging the power of OpenCV, MediaPipe, and PyAutoGUI.

🔧  Technologies and Tools Used
- Python 3: The primary programming language used to develop the project.
- MediaPipe: A machine learning framework used to detect and track hand landmarks in real time.
- OpenCV: A library for computer vision, used for displaying the UI and visual feedback.
- PyAutoGUI: A Python library that automates GUI interactions, enabling the system to simulate media control actions like play, pause, or adjust volume.

💡 How it works:
1. Hand Tracking with MediaPipe:
- MediaPipe's pre-trained hand tracking model identifies and tracks the landmarks of the user's hand. These landmarks correspond to specific points on the fingers and palm.
2. Gesture Interpretation:
- The positions of the hand landmarks are analyzed to recognize specific gestures. For example:
- A thumbs-up gesture might trigger play/pause.
- A swipe gesture could skip tracks.
3. Action Execution with PyAutoGUI:
- Based on the recognized gesture, PyAutoGUI simulates the corresponding media control actions, such as:
- Playing or pausing a video.
- Increasing or decreasing volume.
- Skipping or rewinding tracks.

📋 Step-by-Step Workflow
1. The camera captures the user's hand movements in real time.
2. MediaPipe processes the camera feed and detects hand landmarks.
3. OpenCV displays visual feedback, such as highlighting gestures or tracking the hand's movements.
4. Gesture recognition logic determines which gesture is being performed.
5. PyAutoGUI executes the associated media control command.

✨ Key Features
1. Real-Time Gesture Recognition:
The system processes and responds to gestures instantly, ensuring a smooth user experience.
2. Media Playback Control:
It integrates seamlessly with common media player functions, allowing users to control playback without physical remotes or keyboards.
3. Visual Feedback:
OpenCV provides a simple but effective UI, showing the recognized gestures and improving user interaction.

✨ Feel free to share your thoughts in the comments or message me directly. Together, we can explore new possibilities for AI-powered applications!

<img src="https://github.com/iamramzan/P6-Hand-Controlled-Media-Player-Using-OpenCV-and-MediaPipe/blob/main/Hand-Controlled%20Mediaplayer.png">
