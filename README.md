#Webcam face detection and recognizing gestures (OpenCV)

I want to be proficient in ML field so I decided to combine Java and Python. This app will be a web application with web cam that can detect faces and recognize gestures.I've seen this apps all over the social media and thought that it'll be a great project to learn computer vision. For a fun part, this programm will recognize certain patterns and return some images when a user shows gesture that resembles a stock photo (meme)

To be honest, I'm not profficient yet so I do not know if i can finish this project, but I'll certainly try.

### Architecture and Technology Stack
1. **Backend API (Java / Spring Boot)**: Manages user accounts, stores gesture history and score logs, and exposes REST endpoints.
2. **Computer Vision Service (Python / OpenCV / MediaPipe)**: Captures frames, extracts landmarks, classifies gestures, and returns meme match predictions.
3. **Frontend**: Simple web client to stream the webcam and display the resulting meme overlays.

### Planned Features
1. Real-time webcam streaming and face detection.
2. Hand gesture classification (e.g., peace sign, thumbs up, pointing).
3. Meme image matching algorithm based on detected gesture patterns.
4. History log saving successful detections to a database.