import tkinter as tk
import math

class WaterTempDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.temp_hand = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.temp_hand = self.create_line(512, 300, 512, 450, fill='green', width=4)
        for i in range(60, 150, 10):
            angle = 150 + ((i - 60) / 80) * 270
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            self.create_text(x_end + 25 * math.cos(rad), y_end + 25 * math.sin(rad),
                             text=f"{i}°C", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        temp = int(data.get("CoolantTemp", 0))
        angle = 150 + ((temp - 60) / 80) * 270
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.temp_hand, 512, 300, x, y)
