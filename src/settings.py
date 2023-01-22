import tkinter as tk


class Settings:
    def __init__(self, root):
        self.root = root

        self.length_1 = 90
        self.length_2 = 90
        self.mass_1 = 1.0
        self.mass_2 = 1.0

        self.mass_1_scale = tk.Scale()
        self.mass_2_scale = tk.Scale()
        self.length_1_scale = tk.Scale()
        self.length_2_scale = tk.Scale()
        self.confirm_button = tk.Button()

        self.init_and_grid_mass1_scale()
        self.init_and_grid_mass2_scale()
        self.init_and_grid_length1_scale()
        self.init_and_grid_length2_scale()
        self.init_confirm_button()

    def init_and_grid_mass1_scale(self):
        mass_1_frame = tk.Frame(
            master=self.root
        )
        mass_1_frame.grid(
            row=10,
            rowspan=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=mass_1_frame,
            text='Масса 1 груза'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.mass_1_scale = tk.Scale(
            master=mass_1_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=0.5,
            to=2.5,
            tickinterval=0.5,
            resolution=0.5
        )
        self.mass_1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass_1_scale.set(1.0)

    def init_and_grid_mass2_scale(self):
        mass_2_frame = tk.Frame(
            master=self.root
        )
        mass_2_frame.grid(
            row=12,
            rowspan=2,
            column=0,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=mass_2_frame,
            text='Масса 2 груза'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.mass_2_scale = tk.Scale(
            master=mass_2_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=0.5,
            to=2.5,
            tickinterval=0.5,
            resolution=0.5
        )
        self.mass_2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass_2_scale.set(1.0)

    def init_and_grid_length1_scale(self):
        length_1_frame = tk.Frame(
            master=self.root
        )
        length_1_frame.grid(
            row=10,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=length_1_frame,
            text='Длина 1 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.length_1_scale = tk.Scale(
            master=length_1_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=10
        )
        self.length_1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.length_1_scale.set(90)

    def init_and_grid_length2_scale(self):
        length_2_frame = tk.Frame(
            master=self.root
        )
        length_2_frame.grid(
            row=12,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=length_2_frame,
            text='Длина 2 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.length_2_scale = tk.Scale(
            master=length_2_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=10
        )
        self.length_2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.length_2_scale.set(90)

    def init_confirm_button(self):
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
        self.length_1 = self.length_1_scale.get()
        self.length_2 = self.length_2_scale.get()
        self.mass_1 = self.mass_1_scale.get()
        self.mass_2 = self.mass_2_scale.get()

    def get_length1(self):
        return self.length_1

    def get_length2(self):
        return self.length_2

    def get_mass1(self):
        return self.mass_1

    def get_mass2(self):
        return self.mass_2
