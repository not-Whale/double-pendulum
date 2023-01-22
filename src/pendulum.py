import tkinter as tk
import numpy as np
import time

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
        self.init_canvas()

        # init pendulum settings
        self.length1 = 0.90
        self.length2 = 0.90
        self.mass1 = 1
        self.mass2 = 1
        self.alpha = np.pi / 2
        self.beta = np.pi / 2

        # init start time
        self.start_time = time.time()
        self.current_time = 0.0

        # init center pendulum coords
        self.center_coords = [self.canvas_width / 2, 2 * self.canvas_height / 5]

        # init pendulum bobs
        self.bob1_coords = [self.center_coords[0] + self.length1, self.center_coords[1]]
        self.bob2_coords = [self.bob1_coords[0] + self.length2, self.bob1_coords[1]]

        # init tracer
        self.tracer = tracer.Tracer()
        self.init_tracer()

        self.start_pendulum()

    def test_nazi_pendulum(self):
        t = self.current_time

        a11 = (self.length1 ** 2) * (self.mass1 + self.mass2) / G
        a12 = (self.mass1 * self.length1 * self.length2) / G
        a22 = (self.mass2 * (self.length2 ** 2)) / G

        c11 = (self.mass1 + self.mass2) * self.length1
        c12 = 0
        c22 = self.mass2 * self.length2

        n1 = np.sqrt(G / self.length1)
        n2 = np.sqrt(G / self.length2)

        x = np.sqrt((self.mass2 ** 2) / ((self.mass1 + self.mass2) * self.mass2))

        k1 = np.sqrt((1 / (2 * (1 - (x ** 2)))) *
                     ((n1 ** 2) + (n2 ** 2) + np.sqrt((((n2 ** 2) - (n1 ** 2)) ** 2) + 4 * (x ** 2) * (n1 ** 2) * (n2 ** 2))))

        k2 = np.sqrt((1 / (2 * (1 - (x ** 2)))) *
                     ((n1 ** 2) + (n2 ** 2) - np.sqrt((((n2 ** 2) - (n1 ** 2)) ** 2) + 4 * (x ** 2) * (n1 ** 2) * (n2 ** 2))))

        ce1 = 50.0
        ce2 = 50.0

        alpha1 = np.pi / 2
        alpha2 = np.pi / 2

        self.alpha = np.radians(ce1 * (c22 - (k1 ** 2) * a22) * np.sin(k1 * t + alpha1) +
                                ce2 * (c22 - k2 * a22) * np.sin(k2 * t + alpha2))

        self.beta = np.radians(ce1 * (k1 ** 2) * a12 * np.sin(k1 * t + alpha1) +
                               ce2 * (k2 ** 2) * a12 * np.sin(k2 * t + alpha2))

        self.calc_bob1_coords()
        self.calc_bob2_coords()

        print('alpha = ' + str(self.alpha))
        print('beta = ' + str(self.beta))
        print('x bob1 = ' + str(self.bob1_coords[0]))
        print('y bob1 = ' + str(self.bob1_coords[1]))
        print()

    def start_pendulum(self):
        self.start_time = time.time()
        self.update_pendulum()

    def update_pendulum(self):
        if self.current_time < 1000000:
            print('time = ' + str(self.current_time))
            self.test_nazi_pendulum()
            self.draw_pendulum()
            self.draw_trace('green')
            self.current_time = time.time() - self.start_time
            self.root.after(10, self.update_pendulum)

    def calc_bob1_coords(self):
        self.bob1_coords = [
            self.center_coords[0] + 100 * self.length1 * np.sin(self.alpha),
            self.center_coords[1] + 100 * self.length1 * np.cos(self.alpha)
        ]

    def calc_bob2_coords(self):
        self.bob2_coords = [
            self.bob1_coords[0] + 100 * self.length2 * np.sin(self.beta),
            self.bob1_coords[1] + 100 * self.length2 * np.cos(self.beta)
        ]

    def draw_trace(self, color):
        trace_x = self.tracer.get_trace()[0]
        trace_y = self.tracer.get_trace()[1]

        trace_len = len(trace_x)
        for i in range(trace_len - 1):
            self.canvas.create_line(
                trace_x[i],
                trace_y[i],
                trace_x[i + 1],
                trace_y[i + 1],
                fill=color
            )

    def draw_pendulum(self):
        self.init_canvas()

        self.canvas.create_oval(
            self.center_coords[0] - 3,
            self.center_coords[1] - 3,
            self.center_coords[0] + 3,
            self.center_coords[1] + 3,
            outline='white',
            fill='white'
        )

        self.canvas.create_line(
            self.center_coords[0],
            self.center_coords[1],
            self.bob1_coords[0],
            self.bob1_coords[1],
            fill='white'
        )

        self.canvas.create_line(
            self.bob1_coords[0],
            self.bob1_coords[1],
            self.bob2_coords[0],
            self.bob2_coords[1],
            fill='white'
        )

        self.canvas.create_oval(
            self.bob1_coords[0] - 5,
            self.bob1_coords[1] - 5,
            self.bob1_coords[0] + 5,
            self.bob1_coords[1] + 5,
            outline=BOB1_COLOR,
            fill=BOB1_COLOR
        )

        self.canvas.create_oval(
            self.bob2_coords[0] - 5,
            self.bob2_coords[1] - 5,
            self.bob2_coords[0] + 5,
            self.bob2_coords[1] + 5,
            outline=BOB2_COLOR,
            fill=BOB2_COLOR
        )

    def init_tracer(self):
        self.tracer = tracer.Tracer()
        self.tracer.add_coord(self.bob2_coords[0], self.bob2_coords[1])

    def init_canvas(self):
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
