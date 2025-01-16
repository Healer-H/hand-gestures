from __future__ import annotations

import os
import pickle
import socket
import struct

import cv2
import dotenv
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
dotenv.load_dotenv()


# model_path = "models/checkpoints/gesture_recognizer.task"

# BaseOptions = mp.tasks.BaseOptions
# GestureRecognizer = mp.tasks.vision.GestureRecognizer
# GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
# GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
# VisionRunningMode = mp.tasks.vision.RunningMode

# # Create a gesture recognizer instance with the live stream mode:
# def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
#     print('gesture recognition result: {}'.format(result))

# options = GestureRecognizerOptions(
#     base_options=BaseOptions(model_asset_path='/path/to/model.task'),
#     running_mode=VisionRunningMode.LIVE_STREAM,
#     result_callback=print_result)
# with GestureRecognizer.create_from_options(options) as recognizer:
#   # The detector is initialized. Use it here.
#   # ...
#   pass

host = os.environ.get('HOST')
port = int(os.environ.get('PORT'))


class GestureRecognitionSystem:
    def __init__(self, model):
        self.model = model  # Trained MLP model

    def preprocess_image(self, image: np.array) -> np.array:
        # Preprocess the captured image (resize, normalize, etc.)
        return image

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

    def run(self):
        while True:
            # Create socket server
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((host, port))
            server_socket.listen(5)

            print('Waiting for connection...')
            client_socket, _ = server_socket.accept()
            data = b''
            payload_size = struct.calcsize('L')

            try:
                while True:
                    # Receive message size
                    while len(data) < payload_size:
                        data += client_socket.recv(4096)

                    packed_msg_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack('L', packed_msg_size)[0]

                    # Receive frame data
                    while len(data) < msg_size:
                        data += client_socket.recv(4096)

                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    frame = pickle.loads(frame_data)
                    print(frame.shape)
                    cv2.imshow('Received Frame', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            finally:
                client_socket.close()
                server_socket.close()
                cv2.destroyAllWindows()
