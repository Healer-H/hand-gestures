from __future__ import annotations


class Light:
    def __init__(self, light_id: int, state: bool = False):
        self.light_id = light_id
        self.state = state

    def turn_on(self):
        self.state = True
        print(f"Light {self.light_id} is now ON.")

    def turn_off(self):
        self.state = False
        print(f"Light {self.light_id} is now OFF.")
