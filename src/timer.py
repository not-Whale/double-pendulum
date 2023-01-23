import time
import tkinter as tk


class Timer:
    def __init__(self, root, pendulum, settings):
        # set root, pendulum and settings windows
        self.root = root
        self.pendulum = pendulum
        self.settings = settings

        # initiate timer settings
        self.is_active = False
        self.start_time = time.time()

        # initiate timer and pendulum start/stop buttons
        self.timer_label = tk.Label()
        self.button_start = tk.Button()
        self.button_stop = tk.Button()
        self.initiate_and_grid_timer()

    def initiate_and_grid_timer(self):
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
            command=self.stop_timer,
            state='disabled'
        )
        self.button_stop.grid(
            row=2,
            rowspan=1,
            column=0,
            columnspan=3
        )

    def start_timer(self):
        # set buttons state
        self.button_start['state'] = 'disabled'
        self.button_stop['state'] = 'normal'
        self.settings.confirm_button['state'] = 'disabled'

        # start pendulum
        self.pendulum.start_pendulum()

        # start timer
        self.is_active = True
        self.start_time = time.time()
        self.update_timer()

    def update_timer(self):
        if self.is_active:
            delta = time.time() - self.start_time
            self.timer_label['text'] = '{0:.2f}'.format(delta) + " ms"
            self.root.after(90, self.update_timer)

    def stop_timer(self):
        # set buttons state
        self.button_start['state'] = 'normal'
        self.button_stop['state'] = 'disabled'
        self.settings.confirm_button['state'] = 'normal'

        # stop pendulum
        self.pendulum.stop_pendulum()

        # stop timer
        self.is_active = False
