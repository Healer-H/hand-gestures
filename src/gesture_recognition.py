from __future__ import annotations

import numpy as np


class GestureRecognitionSystem:
    def __init__(self, model):
        self.model = model  # Trained MLP model

    def preprocess_image(self, image: np.array) -> np.array:
        # Preprocess the captured image (resize, normalize, etc.)
        pass

    def classify_gesture(self, preprocessed_image: np.array) -> str:
        # Use the trained model to classify gestures
        return self.model.predict(preprocessed_image)

    def map_to_action(self, gesture: str) -> str:
        # Maps gesture to action (e.g., 'gesture1' -> 'turn_on_light1')
        actions = {
            'gesture1': 'turn_off_all',
            'gesture2': 'turn_on_light1',
            'gesture3': 'turn_on_light2',
            'gesture4': 'turn_on_light3',
            'gesture5': 'turn_on_all',
        }
        return actions.get(gesture, 'unknown_action')
