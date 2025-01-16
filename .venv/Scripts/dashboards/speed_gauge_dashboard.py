import tkinter as tk
import math

class SpeedGaugeDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.speed_hand = None
        self.speed_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.speed_hand = self.create_line(512, 300, 512, 450, fill='blue', width=4)
        self.speed_label = self.create_text(512, 300, text="0 km/h", font=('Helvetica', 30, 'bold'))
        for i in range(0, 241, 10):
            angle = 150 + ((i / 240) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            width = 3 if i % 20 == 0 else 1
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=width)

    def update_data(self, data):
        speed = int(data.get("Speed", 0))
        angle = 150 + ((speed / 240) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.speed_hand, 512, 300, x, y)
        self.itemconfig(self.speed_label, text=f"{speed} km/h")
