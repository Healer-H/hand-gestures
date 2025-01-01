from __future__ import annotations


class Controller:
    def __init__(self):
        self.lights = {}

    def add_light(self, light):
        self.lights[light.light_id] = light

    def execute_command(self, action: str):
        if action == 'turn_off_all':
            for light in self.lights.values():
                light.turn_off()
        elif action == 'turn_on_all':
            for light in self.lights.values():
                light.turn_on()
        elif 'turn_on_light' in action:
            light_id = int(action[-1])
            if light_id in self.lights:
                self.lights[light_id].turn_on()
