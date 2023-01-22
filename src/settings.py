import tkinter as tk


class Settings:
    def __init__(self, root):
        self.root = root

        self.length1 = 90
        self.length2 = 90
        self.mass1 = 1.0
        self.mass2 = 1.0

        self.mass1_scale = tk.Scale()
        self.mass2_scale = tk.Scale()
        self.len1_scale = tk.Scale()
        self.len2_scale = tk.Scale()
        self.confirm_button = tk.Button()

        self.init_mass1_scale()
        self.init_mass2_scale()
        self.init_len1_scale()
        self.init_len2_scale()
        self.init_confirm_button()

    def init_mass1_scale(self):
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
            from_=0.5,
            to=2.5,
            tickinterval=0.5,
            resolution=0.5
        )
        self.mass1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass1_scale.set(1.0)

    def init_mass2_scale(self):
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
            from_=0.5,
            to=2.5,
            tickinterval=0.5,
            resolution=0.5
        )
        self.mass2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.mass2_scale.set(1.0)

    def init_len1_scale(self):
        len1_frame = tk.Frame(
            master=self.root
        )
        len1_frame.grid(
            row=10,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=len1_frame,
            text='Длина 1 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.len1_scale = tk.Scale(
            master=len1_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=10
        )
        self.len1_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.len1_scale.set(90)

    def init_len2_scale(self):
        len2_frame = tk.Frame(
            master=self.root
        )
        len2_frame.grid(
            row=12,
            rowspan=2,
            column=3,
            columnspan=3,
            padx=10,
            pady=10
        )

        tk.Label(
            master=len2_frame,
            text='Длина 2 нити'
        ).grid(
            row=0,
            rowspan=1,
            column=0,
            columnspan=3,
            sticky='w'
        )

        self.len2_scale = tk.Scale(
            master=len2_frame,
            orient=tk.HORIZONTAL,
            length=200,
            from_=50,
            to=90,
            tickinterval=10,
            resolution=10
        )
        self.len2_scale.grid(
            row=1,
            rowspan=1,
            column=0,
            columnspan=3
        )

        self.len2_scale.set(90)

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
        self.length1 = self.len1_scale.get()
        self.length2 = self.len2_scale.get()
        self.mass1 = self.mass1_scale.get()
        self.mass2 = self.mass2_scale.get()

    def get_length1(self):
        return self.length1

    def get_length2(self):
        return self.length2

    def get_mass1(self):
        return self.mass1

    def get_mass2(self):
        return self.mass2
