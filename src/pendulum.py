import tkinter as tk
import numpy as np
import time
from point import Point

import tracer
from consts import *


class Pendulum:
    def __init__(self, root):
        # root window
        self.root = root

        # init pendulum canvas
        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas()
        self.init_and_grid_canvas()

        # init pendulum settings
        self.length_1 = 90.0
        self.length_2 = 90.0
        self.mass_1 = 1.0
        self.mass_2 = 1.0
        self.alpha = np.pi / 2
        self.beta = np.pi / 2

        # init start time
        self.start_time = time.time()
        self.current_time = 0.0

        # init center pendulum coords
        self.center_coords = Point(self.canvas_width / 2, 2 * self.canvas_height / 5)

        # init pendulum bobs
        self.bob1_coords = Point(self.center_coords.get_x() + self.length_1, self.center_coords.get_y())
        self.bob2_coords = Point(self.bob1_coords.get_x() + self.length_2, self.bob1_coords.get_y())

        # init tracer
        self.tracer = tracer.Tracer()
        self.init_and_grid_tracer()

        # pendulum movement flag
        self.is_active = False

        self.start_pendulum()

    def calc_pendulum_angles(self):
        # f начнем с чистого листа
        pass
    
    def stop_pendulum(self):
        self.is_active = False

    def start_pendulum(self):
        self.start_time = time.time()
        self.is_active = True
        self.update_pendulum()

    def update_pendulum(self):
        if self.is_active:
            # print('time = ' + str(self.current_time))
            self.current_time = time.time() - self.start_time
            # drawing
            self.calc_pendulum_angles()
            self.draw_pendulum()
            # self.draw_trace('green')
            # circle
            self.root.after(10, self.update_pendulum)

    def calc_bob1_coords(self):
        self.bob1_coords = Point(
            self.center_coords.get_x() + self.length_1 * np.sin(self.alpha),
            self.center_coords.get_y() + self.length_1 * np.cos(self.alpha)
        )

    def calc_bob2_coords(self):
        self.bob2_coords = Point(
            self.bob1_coords.get_x() + self.length_2 * np.sin(self.beta),
            self.bob1_coords.get_y() + self.length_2 * np.cos(self.beta)
        )

    # def draw_trace(self, color):
    #     trace_x = self.tracer.get_trace()[0]
    #     trace_y = self.tracer.get_trace()[1]
    #
    #     trace_len = len(trace_x)
    #     for i in range(trace_len - 1):
    #         self.canvas.create_line(
    #             trace_x[i],
    #             trace_y[i],
    #             trace_x[i + 1],
    #             trace_y[i + 1],
    #             fill=color
    #         )

    def draw_pendulum(self):
        self.init_and_grid_canvas()

        self.canvas.create_oval(
            self.center_coords.get_x() - 3,
            self.center_coords.get_y() - 3,
            self.center_coords.get_x() + 3,
            self.center_coords.get_y() + 3,
            outline='white',
            fill='white'
        )

        self.canvas.create_line(
            self.center_coords.get_x(),
            self.center_coords.get_y(),
            self.bob1_coords.get_x(),
            self.bob1_coords.get_y(),
            fill='white'
        )

        self.canvas.create_line(
            self.bob1_coords.get_x(),
            self.bob1_coords.get_y(),
            self.bob2_coords.get_x(),
            self.bob2_coords.get_y(),
            fill='white'
        )

        self.canvas.create_oval(
            self.bob1_coords.get_x() - 5,
            self.bob1_coords.get_y() - 5,
            self.bob1_coords.get_x() + 5,
            self.bob1_coords.get_y() + 5,
            outline=BOB1_COLOR,
            fill=BOB1_COLOR
        )

        self.canvas.create_oval(
            self.bob2_coords.get_x() - 5,
            self.bob2_coords.get_y() - 5,
            self.bob2_coords.get_x() + 5,
            self.bob2_coords.get_y() + 5,
            outline=BOB2_COLOR,
            fill=BOB2_COLOR
        )

    def init_and_grid_tracer(self):
        self.tracer = tracer.Tracer()
        self.tracer.add_coord(self.bob2_coords.get_x(), self.bob2_coords.get_y())

    def init_and_grid_canvas(self):
        self.canvas = tk.Canvas(
            master=self.root,
            background='black',
            width=self.canvas_width,
            height=self.canvas_height
        )
        self.canvas.grid(
            row=0,
            rowspan=10,
            column=3,
            columnspan=10,
            padx=20,
            pady=20
        )
