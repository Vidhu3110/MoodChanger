import cv2
from fer import FER

class EmotionRecognizer:
    def __init__(self):
        # Initialize the FER detector with MTCNN for face detection.
        self.detector = FER(mtcnn=True)

    def predict_emotion(self, frame):
        # Convert frame from BGR (OpenCV) to RGB (expected by FER)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.detector.detect_emotions(rgb_frame)

        if results:
            # Take the first detected face and return the top emotion.
            emotions = results[0]['emotions']
            top_emotion = max(emotions, key=emotions.get)
            return top_emotion
        else:
            return "neutral"