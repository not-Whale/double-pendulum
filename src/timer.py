import time
import tkinter as tk


class Timer:
    def __init__(self, root, pendulum):
        self.root = root
        self.pendulum = pendulum

        self.timer_status = False
        self.start_time = time.time()

        self.timer_label = tk.Label()
        self.button_start = tk.Button()
        self.button_stop = tk.Button()
        self.error_label = tk.Button()

        self.init_and_grid_timer()

    def init_and_grid_timer(self):
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
            text='start timer',
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
            text='stop timer',
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

        self.error_label = tk.Label(
            master=timer_frame,
            text='',
            width=30,
            height=3,
            foreground='red'
        )
        self.error_label.grid(
            row=3,
            rowspan=1,
            column=0,
            columnspan=3
        )

    def start_timer(self):
        if self.timer_status:
            self.error_label['text'] = 'таймер уже запущен'
        else:
            self.error_label['text'] = ''
            self.timer_status = True
            self.start_time = time.time()
            self.update_timer()

    def update_timer(self):
        if self.timer_status:
            delta = time.time() - self.start_time
            self.timer_label['text'] = '{0:.2f}'.format(delta) + " ms"
            self.root.after(90, self.update_timer)

    def stop_timer(self):
        if self.timer_status:
            self.error_label['text'] = ''
            self.timer_status = False
        else:
            self.error_label['text'] = 'таймер уже остановлен'
