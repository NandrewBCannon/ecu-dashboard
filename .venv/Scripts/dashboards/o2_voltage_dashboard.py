import tkinter as tk
import math

class O2VoltageDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.o2_hand = None
        self.o2_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.o2_hand = self.create_line(512, 300, 512, 450, fill='darkgreen', width=4)
        self.o2_label = self.create_text(512, 300, text="0.0 V", font=('Helvetica', 30, 'bold'))
        for i in range(0, 11):  # Scale from 0V to 1V in 0.1 increments
            angle = 150 + ((i / 10) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            self.create_text(x_end + 20 * math.cos(rad), y_end + 20 * math.sin(rad),
                             text=f"{i / 10:.1f}V", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        o2_voltage = float(data.get("O2Voltage", 0))
        angle = 150 + ((o2_voltage / 1.0) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.o2_hand, 512, 300, x, y)
        self.itemconfig(self.o2_label, text=f"{o2_voltage:.2f} V")
