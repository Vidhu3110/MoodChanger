import random

class MusicGenerator:
    def __init__(self):
        # Here you could load or initialize your pretrained GAN-based music model
        # For this demo, we’ll just store chord progressions
        self.chord_progressions = {
            "happy":    ["C", "G", "Am", "F"],
            "sad":      ["Dm", "Am", "E", "F"],
            "angry":    ["Gm", "Bb", "Eb", "F"],
            "surprise": ["C", "Em", "F", "G"],
            "neutral":  ["C", "F", "G"]
        }

    def generate_music(self, emotion):
        # In reality, feed the `emotion` into your pretrained model and generate music (MIDI/audio)
        # For now, just return a chord progression
        progression = self.chord_progressions.get(emotion, self.chord_progressions["neutral"])
        return " - ".join(progression)