from __future__ import annotations

import pickle
import socket
import struct

import cv2
import numpy as np


class Camera:
    def __init__(self):
        pass

    def video_stream(self, host, port):
        # Create socket connection
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))

        # Initialize video capture
        cap = cv2.VideoCapture(0)

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break

                # Optional: resize frame for better performance
                frame = cv2.resize(frame, (640, 480))

                # Serialize frame
                data = pickle.dumps(frame)

                # Pack frame size and send
                message_size = struct.pack('L', len(data))
                client_socket.sendall(message_size + data)

                # Display locally
                cv2.imshow('Sending Frame', frame)

                # Press 'q' to quit
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            cap.release()
            client_socket.close()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    camera = Camera()
    camera.video_stream(host='127.0.0.1', port=9999)
