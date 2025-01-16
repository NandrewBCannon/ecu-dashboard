import tkinter as tk
import math

class AFMVoltageDashboard(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=1024, height=600, bg='white')
        self.afm_hand = None
        self.afm_label = None
        self.draw_gauge()

    def draw_gauge(self):
        self.create_oval(362, 150, 662, 450, outline='black', width=4)
        self.afm_hand = self.create_line(512, 300, 512, 450, fill='darkblue', width=4)
        self.afm_label = self.create_text(512, 300, text="0.0 V", font=('Helvetica', 30, 'bold'))
        for i in range(0, 51, 5):  # Scale from 0V to 5V in 0.5 increments
            angle = 150 + ((i / 50) * 270)
            rad = math.radians(angle)
            x_start = 512 + 120 * math.cos(rad)
            y_start = 300 + 120 * math.sin(rad)
            x_end = 512 + 150 * math.cos(rad)
            y_end = 300 + 150 * math.sin(rad)
            self.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)
            self.create_text(x_end + 20 * math.cos(rad), y_end + 20 * math.sin(rad),
                             text=f"{i / 10:.1f}V", font=('Helvetica', 10, 'bold'))

    def update_data(self, data):
        afm_voltage = float(data.get("AFMVoltage", 0))
        angle = 150 + ((afm_voltage / 5.0) * 270)
        rad = math.radians(angle)
        x = 512 + 120 * math.cos(rad)
        y = 300 + 120 * math.sin(rad)
        self.coords(self.afm_hand, 512, 300, x, y)
        self.itemconfig(self.afm_label, text=f"{afm_voltage:.2f} V")
