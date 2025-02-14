import tkinter as tk
import math

class TPSDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.tps_hand = None
        self.tps_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.tps_hand = self.create_line(512, 300, 512, 450, fill='darkred', width=4)
        self.tps_label = self.create_text(512, 300, text="0%", font=('Helvetica', 30, 'bold'))
        for i in range(0, 101, 10):  # Scale from 0% to 100%
            angle = 150 + ((i / 100) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            self.create_text(x_end + 20 * math.cos(rad), y_end + 20 * math.sin(rad),
                             text=f"{i}%", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        tps_value = float(data.get("TPSPosition", 0))
        angle = 150 + ((tps_value / 100) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.tps_hand, 512, 300, x, y)
        self.itemconfig(self.tps_label, text=f"{tps_value:.1f}%")
