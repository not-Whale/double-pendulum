import time
import tkinter as tk


class Timer:
    def __init__(self, root, pendulum):
        # set root and pendulum windows
        self.root = root
        self.pendulum = pendulum

        # initiate timer settings
        self.is_active = False
        self.start_time = time.time()

        # initiate timer and pendulum start/stop buttons
        self.timer_label = tk.Label()
        self.button_start = tk.Button()
        self.button_stop = tk.Button()
        self.init_and_grid_timer()

    def init_and_grid_timer(self):
        # frame for timer and buttons
        timer_frame = tk.Frame(
            master=self.root
        )
        timer_frame.grid(
            row=0,
            rowspan=4,
            column=0,
            columnspan=3,
            padx=20,
            pady=20
        )

        self.timer_label = tk.Label(
            master=timer_frame,
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

        self.button_start = tk.Button(
            master=timer_frame,
            text='start',
            width=10,
            height=1,
            command=self.start_timer
        )
        self.button_start.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.button_stop = tk.Button(
            master=timer_frame,
            text='stop',
            width=10,
            height=1,
            command=self.stop_timer
        )
        self.button_stop.grid(
            row=2,
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
