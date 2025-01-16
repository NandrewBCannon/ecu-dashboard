import tkinter as tk
import math

class RpmDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.rpm_hand = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.rpm_hand = self.create_line(512, 300, 512, 450, fill='red', width=4)
        for i in range(1, 19):
            angle = 150 + ((i / 18) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            if i % 2 == 0:
                self.create_text(x_end + 25 * math.cos(rad), y_end + 25 * math.sin(rad),
                                 text=f"{i * 500}", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        rpm = int(data.get("RPM", 0))
        angle = 150 + ((rpm / 9000) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.rpm_hand, 512, 300, x, y)