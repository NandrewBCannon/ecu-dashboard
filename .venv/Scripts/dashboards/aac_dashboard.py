import tkinter as tk
import math

class AACDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.aac_hand = None
        self.aac_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.aac_hand = self.create_line(512, 300, 512, 450, fill='brown', width=4)
        self.aac_label = self.create_text(512, 300, text="0%", font=('Helvetica', 30, 'bold'))
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
        aac_value = float(data.get("AAC", 0))
        angle = 150 + ((aac_value / 100) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.aac_hand, 512, 300, x, y)
        self.itemconfig(self.aac_label, text=f"{aac_value:.1f}%")
