from __future__ import annotations

import numpy as np


class Camera:
    def __init__(self, camera_id: int, resolution: tuple):
        self.camera_id = camera_id
        self.resolution = resolution

    def capture_image(self) -> np.array:
        # Simulates capturing an image and returns image data.
        pass
