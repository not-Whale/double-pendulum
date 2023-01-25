import time
import tkinter as tk


class Timer:
    def __init__(self, root):
        # set root window
        self.root = root

        # initiate timer settings
        self.is_active = False
        self.start_time = time.time()

        # initiate timer and pendulum start/stop buttons
        self.timer_label = tk.Label()
        self.timer_frame = tk.Label()
        self.initiate_and_grid_timer()

    def get_timer_frame(self):
        return self.timer_frame

    def initiate_and_grid_timer(self):
        # frame for timer and buttons
        self.timer_frame = tk.Frame(
            master=self.root
        )
        self.timer_frame.grid(
            row=0,
            rowspan=4,
            column=0,
            columnspan=3,
            padx=20,
            pady=20
        )

        self.timer_label = tk.Label(
            master=self.timer_frame,
            text='0.00 ms',
            width=20,
            height=3
        )
        self.timer_label.grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3
        )

    def start_timer(self):
        self.is_active = True
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.is_active:
            delta = time.time() - self.start_time
            self.timer_label['text'] = '{0:.2f}'.format(delta) + " ms"
            self.root.after(90, self.update_timer)

    def stop_timer(self):
        self.is_active = False

    def reset_timer(self):
        self.timer_label['text'] = '0.00 ms'
