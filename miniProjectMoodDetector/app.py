import cv2
from emotion_recognizer import EmotionRecognizer
from music_generator import MusicGenerator


def main():

    emotion_recognizer = EmotionRecognizer()
    music_gen = MusicGenerator()

    # Open webcam (or use a video file by changing the argument to VideoCapture)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect emotion
        emotion = emotion_recognizer.predict_emotion(frame)
        print(f"[INFO] Detected emotion: {emotion}")

        # Generate or update music based on emotion.
        # This returns the filename of the generated MIDI.
        midi_file = music_gen.generate_music(emotion)
        print(f"[MUSIC] Generated MIDI for {emotion}: {midi_file}")

        # Display the webcam feed
        cv2.imshow("Mood-Adaptive Composer (Press 'q' to quit)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()