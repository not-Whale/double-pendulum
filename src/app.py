import tkinter as tk

from pendulum import Pendulum
from settings import Settings
from timer import Timer


class App:
    def __init__(self):
        # initiate root window
        self.root = tk.Tk()
        self.root.title('rezepinn/bmstu/pendulum.app')
        self.root.resizable(False, False)

        # create widgets
        self.timer = Timer(self.root)
        self.pendulum = Pendulum(self.root)
        self.settings = Settings(self.root, self.pendulum)

        # initiate command buttons
        self.button_start = tk.Button()
        self.button_stop = tk.Button()
        self.button_reset = tk.Button()
        self.init_and_grid_buttons()

        # start listening
        self.root.mainloop()

    def start(self):
        # set buttons state
        self.button_start['state'] = 'disabled'
        self.button_stop['state'] = 'normal'
        self.button_reset['state'] = 'disabled'
        self.settings.confirm_button['state'] = 'disabled'

        # start pendulum
        self.pendulum.start_pendulum()

        # start timer
        self.timer.start_timer()

    def stop(self):
        # set buttons state
        self.button_start['state'] = 'normal'
        self.button_stop['state'] = 'disabled'
        self.button_reset['state'] = 'normal'
        self.settings.confirm_button['state'] = 'normal'

        # stop pendulum
        self.pendulum.stop_pendulum()

        # stop timer
        self.timer.stop_timer()

    def reset(self):
        # reset pendulum
        self.pendulum.reset_pendulum()
        self.pendulum.draw_pendulum()
        self.pendulum.draw_traces()

        # reset settings
        self.settings.reset_settings()

    def init_and_grid_buttons(self):
        self.button_start = tk.Button(
            master=self.timer.get_timer_frame(),
            text='запустить',
            width=10,
            height=1,
            command=self.start
        )
        self.button_start.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.button_stop = tk.Button(
            master=self.timer.get_timer_frame(),
            text='остановить',
            width=10,
            height=1,
            command=self.stop,
            state='disabled'
        )
        self.button_stop.grid(
            row=2,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.button_reset = tk.Button(
            master=self.timer.get_timer_frame(),
            text='сбросить',
            width=10,
            height=1,
            command=self.reset
        )
        self.button_reset.grid(
            row=3,
            rowspan=1,
            column=0,
            columnspan=3
        )
