import tkinter as tk
import math

class CombinedDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.rpm_hand = None
        self.speed_hand = None
        self.speed_label = None
        self.draw_gauges()

    def draw_gauges(self):
        # RPM Gauge (Left)
        self.create_oval(100, 150, 400, 450, outline='black', width=4)
        self.rpm_hand = self.create_line(250, 300, 250, 170, fill='red', width=4)
        for i in range(1, 19):
            angle = 150 + ((i / 18) * 270)
            rad = math.radians(angle)
            x_start = 250 + 100 * math.cos(rad)
            y_start = 300 + 100 * math.sin(rad)
            x_end = 250 + 120 * math.cos(rad)
            y_end = 300 + 120 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            if i % 2 == 0:
                self.create_text(x_end + 15 * math.cos(rad), y_end + 15 * math.sin(rad),
                                 text=f"{i * 500}", font=('Helvetica', 8, 'bold'))
        
        # Speed Gauge (Right)
        self.create_oval(624, 150, 924, 450, outline='black', width=4)
        self.speed_hand = self.create_line(774, 300, 774, 170, fill='blue', width=4)
        self.speed_label = self.create_text(774, 300, text="0 km/h", font=('Helvetica', 20, 'bold'))
        for i in range(0, 241, 10):
            angle = 150 + ((i / 240) * 270)
            rad = math.radians(angle)
            x_start = 774 + 100 * math.cos(rad)
            y_start = 300 + 100 * math.sin(rad)
            x_end = 774 + 120 * math.cos(rad)
            y_end = 300 + 120 * math.sin(rad)
            width = 3 if i % 20 == 0 else 1
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=width)

    def update_data(self, data):
        # Update RPM Gauge
        rpm = int(data.get("RPM", 0))
        angle_rpm = 150 + ((rpm / 9000) * 270)
        rad_rpm = math.radians(angle_rpm)
        x_rpm = 250 + 100 * math.cos(rad_rpm)
        y_rpm = 300 + 100 * math.sin(rad_rpm)
        self.coords(self.rpm_hand, 250, 300, x_rpm, y_rpm)

        # Update Speed Gauge
        speed = int(data.get("Speed", 0))
        angle_speed = 150 + ((speed / 240) * 270)
        rad_speed = math.radians(angle_speed)
        x_speed = 774 + 100 * math.cos(rad_speed)
        y_speed = 300 + 100 * math.sin(rad_speed)
        self.coords(self.speed_hand, 774, 300, x_speed, y_speed)
        self.itemconfig(self.speed_label, text=f"{speed} km/h")
