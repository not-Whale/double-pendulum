import tkinter as tk


class Settings:
    def __init__(self, root, pendulum):
        # set root window and pendulum widget
        self.root = root
        self.pendulum = pendulum

        # initiate pendulum settings scales
        self.mass1_scale = tk.Scale()
        self.initiate_and_grid_mass1_scale()

        self.mass2_scale = tk.Scale()
        self.initiate_and_grid_mass2_scale()

        self.length1_scale = tk.Scale()
        self.initiate_and_grid_length1_scale()

        self.length2_scale = tk.Scale()
        self.initiate_and_grid_length2_scale()

        self.tracing_mode_scale = tk.Scale()
        self.initiate_and_grid_tracing_mode_scale()

        self.confirm_button = tk.Button()
        self.initiate_and_grid_confirm_button()

    def initiate_and_grid_mass1_scale(self):
        # frame for label and scale
        mass1_frame = tk.Frame(
            master=self.root
        )
        mass1_frame.grid(
            row=10,
            rowspan=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=mass1_frame,
            text='Масса 1 груза'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.mass1_scale = tk.Scale(
            master=mass1_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=5,
            to=20,
            tickinterval=5,
            resolution=1
        )
        self.mass1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass1_scale.set(5)

    def initiate_and_grid_mass2_scale(self):
        # frame for label and scale
        mass2_frame = tk.Frame(
            master=self.root
        )
        mass2_frame.grid(
            row=12,
            rowspan=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=mass2_frame,
            text='Масса 2 груза'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.mass2_scale = tk.Scale(
            master=mass2_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=5,
            to=20,
            tickinterval=5,
            resolution=1
        )
        self.mass2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass2_scale.set(5)

    def initiate_and_grid_length1_scale(self):
        # frame for label and scale
        length1_frame = tk.Frame(
            master=self.root
        )
        length1_frame.grid(
            row=10,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=length1_frame,
            text='Длина 1 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.length1_scale = tk.Scale(
            master=length1_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=1
        )
        self.length1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.length1_scale.set(90)

    def initiate_and_grid_length2_scale(self):
        # frame for label and scale
        length2_frame = tk.Frame(
            master=self.root
        )
        length2_frame.grid(
            row=12,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=length2_frame,
            text='Длина 2 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.length2_scale = tk.Scale(
            master=length2_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=1
        )
        self.length2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.length2_scale.set(90)

    def initiate_and_grid_tracing_mode_scale(self):
        # frame for label and scale
        tracing_mode_frame = tk.Frame(
            master=self.root
        )
        tracing_mode_frame.grid(
            row=10,
            rowspan=2,
            column=6,
            columnspan=3,
            padx=20,
            pady=20
        )

        tk.Label(
            master=tracing_mode_frame,
            text='Тип отслеживания'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=1,
            sticky='w'
        )

        self.tracing_mode_scale = tk.Scale(
            master=tracing_mode_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=0,
            to=2,
            tickinterval=1,
            resolution=1
        )
        self.tracing_mode_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=1
        )

    def initiate_and_grid_confirm_button(self):
        self.confirm_button = tk.Button(
            master=self.root,
            text='подтвердить настройки',
            width=20,
            command=self.set_settings
        )
        self.confirm_button.grid(
            row=13,
            rowspan=1,
            column=6,
            columnspan=3,
            padx=20,
            pady=20
        )

    def set_settings(self):
        # set new pendulum settings
        self.pendulum.set_mass1(self.mass1_scale.get())
        self.pendulum.set_mass2(self.mass2_scale.get())
        self.pendulum.set_length1(self.length1_scale.get())
        self.pendulum.set_length2(self.length2_scale.get())
        self.pendulum.calculate_bob1_coords()
        self.pendulum.calculate_bob2_coords()

        # set new tracing settings
        self.pendulum.set_tracing_mode(self.tracing_mode_scale.get())

        # update picture on canvas
        self.pendulum.draw_pendulum()
        self.pendulum.draw_traces()

    def reset_settings(self):
        self.mass1_scale.set(5)
        self.mass2_scale.set(5)
        self.length1_scale.set(90)
        self.length2_scale.set(90)
        self.tracing_mode_scale.set(0)
