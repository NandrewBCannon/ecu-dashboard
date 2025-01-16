import time  # Make sure this is imported for timing functions

class DevModeDataSource:
    def __init__(self):
        self.fake_rpm = 700  # Starting RPM
        self.fake_speed = 0  # Starting Speed

    def get_data(self):
        # Increment RPM
        self.fake_rpm += 50
        if self.fake_rpm > 7500:
            self.fake_rpm = 700

        # Increment Speed
        self.fake_speed += 1
        if self.fake_speed > 240:
            self.fake_speed = 0

        # Return simulated ECU data
        data = {
            "Time": time.strftime("%H:%M:%S"),
            "RPM": str(self.fake_rpm),
            "Speed": str(self.fake_speed)
        }
        return data
