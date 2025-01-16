from __future__ import annotations

import os

import dotenv
from camera import Camera
from controller import Controller
from gesture_recognition import GestureRecognitionSystem
dotenv.load_dotenv()

# Initialize Components
# camera = Camera(camera_id=1, resolution=(640, 480))
# model = None
# gesture_recognition = GestureRecognitionSystem(model=model)
# controller = Controller()
# light1 = Light(light_id=1)
# light2 = Light(light_id=2)
# light3 = Light(light_id=3)

# # Add Lights to Controller
# controller.add_light(light1)
# controller.add_light(light2)
# controller.add_light(light3)

# # Capture Gesture and Control Lights
# captured_image = camera.capture_image()
# preprocessed_image = gesture_recognition.preprocess_image(captured_image)
# gesture = gesture_recognition.classify_gesture(preprocessed_image)
# action = gesture_recognition.map_to_action(gesture)
# controller.execute_command(action)


if __name__ == '__main__':
    # Initialize Components
    HOST = os.environ.get('HOST')
    PORT = int(os.environ.get('PORT'))
    camera = Camera()

    model = None
    gesture_recognition = GestureRecognitionSystem(model=model)
    gesture_recognition.run()
