import tkinter as tk
import math

class IgnitionTimingDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.timing_hand = None
        self.timing_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.timing_hand = self.create_line(512, 300, 512, 450, fill='green', width=4)
        self.timing_label = self.create_text(512, 300, text="0° BTDC", font=('Helvetica', 30, 'bold'))
        for i in range(-10, 41, 10):  # Scale from -10° to 40° BTDC
            angle = 150 + (((i + 10) / 50) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            self.create_text(x_end + 20 * math.cos(rad), y_end + 20 * math.sin(rad),
                             text=f"{i}°", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        timing = float(data.get("IgnitionTiming", 0))
        angle = 150 + (((timing + 10) / 50) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.timing_hand, 512, 300, x, y)
        self.itemconfig(self.timing_label, text=f"{timing:.1f}° BTDC")
