import tkinter as tk
import time
import os
import serial
from config import DASHBOARD_CLASSES

def is_consult_connected():
    """Check if the Nissan Consult cable is connected."""
    return os.path.exists('/dev/ttyUSB0')

class ECUApp(tk.Tk):
    def __init__(self, data_source):
        super().__init__()
        self.title("Swipeable ECU Dashboard")
        self.geometry("1024x600")
        self.data_source = data_source

        # Long press detection variables
        self.press_time = None
        self.long_press_duration = 2000  # 2 seconds

        # Create frames for each enabled dashboard
        self.dashboard_frames = []
        self.current_frame_index = 0
        self.load_dashboards(DASHBOARD_CLASSES)

        # Bind long press for touch and mouse
        self.bind("<ButtonPress-1>", self.start_long_press)  # Touch press
        self.bind("<ButtonPress-3>", self.start_long_press)  # Right-click for mouse simulation
        self.bind("<ButtonRelease-1>", self.end_long_press)  # Touch release
        self.bind("<ButtonRelease-3>", self.end_long_press)  # Right-click release for mouse simulation

        # Bind swipe gestures
        self.bind("<Left>", lambda e: self.show_next_frame())
        self.bind("<Right>", lambda e: self.show_previous_frame())
        self.bind("<Button-4>", lambda e: self.show_previous_frame())
        self.bind("<Button-5>", lambda e: self.show_next_frame())

        self.update_data()

    def load_dashboards(self, dashboard_list):
        for widget in self.dashboard_frames:
            widget.grid_remove()
        self.dashboard_frames.clear()

        for dashboard_name in dashboard_list:
            dashboard_loader = DASHBOARD_CLASSES.get(dashboard_name)
            if dashboard_loader:
                try:
                    frame = dashboard_loader(self)
                    self.dashboard_frames.append(frame)
                    frame.grid(row=0, column=0, sticky="nsew")
                except Exception as e:
                    print(f"Error loading dashboard '{dashboard_name}': {e}")
            else:
                print(f"Warning: Dashboard '{dashboard_name}' not found.")
        self.show_frame(0)

    def start_long_press(self, event):
        self.press_time = self.after(self.long_press_duration, self.open_customizer)

    def end_long_press(self, event):
        if self.press_time:
            self.after_cancel(self.press_time)
            self.press_time = None

    def open_customizer(self):
        self.press_time = None
        popup = tk.Toplevel(self)
        popup.title("Customize Dashboards")
        popup.geometry("400x500")

        tk.Label(popup, text="Select Dashboards:", font=("Helvetica", 12, "bold")).pack(pady=10)
        dashboard_vars = {}

        for dashboard_name in DASHBOARD_CLASSES.keys():
            var = tk.BooleanVar(value=dashboard_name in [frame.__class__.__name__ for frame in self.dashboard_frames])
            tk.Checkbutton(popup, text=dashboard_name, variable=var).pack(anchor='w')
            dashboard_vars[dashboard_name] = var

        def apply_changes():
            selected = [name for name, var in dashboard_vars.items() if var.get()]
            self.load_dashboards(selected)
            popup.destroy()

        tk.Button(popup, text="Apply Changes", command=apply_changes).pack(pady=20)

    def show_frame(self, index):
        for i, frame in enumerate(self.dashboard_frames):
            frame.grid_remove() if i != index else frame.grid()
        self.current_frame_index = index

    def show_next_frame(self):
        next_index = (self.current_frame_index + 1) % len(self.dashboard_frames)
        self.show_frame(next_index)

    def show_previous_frame(self):
        prev_index = (self.current_frame_index - 1) % len(self.dashboard_frames)
        self.show_frame(prev_index)

    def update_data(self):
        try:
            data = self.data_source.get_data()
            for frame in self.dashboard_frames:
                frame.update_data(data)
        except Exception as e:
            print(f"Error reading data: {e}")
        self.after(100, self.update_data)

if __name__ == "__main__":
    if is_consult_connected():
        try:
            serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
            from real_mode import RealModeDataSource  # Replace with your actual data source
            data_source = RealModeDataSource()
            print("Nissan Consult detected. Running in real mode.")
        except Exception as e:
            print(f"Error connecting to ECU: {e}")
            from dev_mode import DevModeDataSource
            data_source = DevModeDataSource()
            print("Falling back to dev mode due to connection error.")
    else:
        from dev_mode import DevModeDataSource
        data_source = DevModeDataSource()
        print("Nissan Consult not detected. Running in dev mode.")

    app = ECUApp(data_source)
    app.mainloop()
