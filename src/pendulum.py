import tkinter as tk
import numpy as np
import time
from point import Point

import tracer
from consts import *


class Pendulum:
    def __init__(self, root):
        # set root window
        self.root = root

        # initiate pendulum canvas
        self.canvas = tk.Canvas()
        self.initiate_and_grid_canvas()

        # initiate pendulum settings
        self.length1 = 90.0
        self.length2 = 90.0
        self.mass1 = 1.0
        self.mass2 = 1.0
        self.alpha = np.pi / 2
        self.beta = np.pi / 2
        self.d_alpha = 0.0
        self.d_beta = 0.0

        # initiate start time and current time
        self.start_time = time.time()
        # self.current_time = 0.0

        # set center pendulum coordinates
        self.center_coords = Point(CANVAS_WIDTH / 2, 2 * CANVAS_HEIGHT / 5)

        # initiate pendulum bob's coordinates
        self.bob1_coords = Point(self.center_coords.get_x() + self.length1, self.center_coords.get_y())
        self.bob2_coords = Point(self.bob1_coords.get_x() + self.length2, self.bob1_coords.get_y())

        # initiate tracer
        self.bob1_tracer = tracer.Tracer()
        self.bob2_tracer = tracer.Tracer()
        self.initiate_and_grid_tracers()

        # pendulum movement and drawing flags
        self.is_active = False
        self.tracing_mode = 0

        # set start state
        self.draw_pendulum()

    def stop_pendulum(self):
        self.is_active = False

    def start_pendulum(self):
        self.is_active = True
        self.start_time = time.time()
        self.update_pendulum()

    def update_pendulum(self):
        if self.is_active:
            # calculating
            self.calculate_pendulum_state()

            # drawing
            self.draw_pendulum()
            self.draw_traces()

            # next step
            self.root.after(10, self.update_pendulum)

    def set_tracing_mode(self, code):
        self.tracing_mode = code
        self.initiate_and_grid_tracers()

    def calculate_pendulum_state(self):
        self.calculate_pendulum_angles()
        self.calculate_bob1_coords()
        self.calculate_bob2_coords()

    def calculate_pendulum_angles(self):
        # components for the 2nd derivative of alpha for first bob
        component_1 = (- G * (2 * self.mass1 + self.mass2) * np.sin(self.alpha)) - \
                      (self.mass2 * G * np.sin(self.alpha - 2 * self.beta))

        component_2 = (2 * np.sin(self.alpha - self.beta) * self.mass2) * \
                      (self.d_beta ** 2 * self.length2 +
                       self.d_alpha ** 2 * self.length1 * np.cos(self.alpha - self.beta))

        component_3 = (2 * self.length1 * self.mass1) + \
                      (self.length1 * self.mass2 * (1 - np.cos(2 * self.alpha - 2 * self.beta)))

        # second derivative of alpha
        dd_alpha = (component_1 - component_2) / component_3

        # components for the 2nd derivative of beta for second bob
        component_1 = 2 * np.sin(self.alpha - self.beta)

        component_2 = (self.d_alpha ** 2 * self.length1 * (self.mass1 + self.mass2)) + \
                      (G * (self.mass1 + self.mass2) * np.cos(self.alpha)) + \
                      (self.d_beta ** 2 * self.length2 * self.mass2 * np.cos(self.alpha - self.beta))

        component_3 = (2 * self.length2 * self.mass1) + \
                      (self.length2 * self.mass2) + \
                      (self.length2 * self.mass2 * np.cos(2 * (self.alpha - self.beta)))

        # second derivative of beta
        dd_beta = (component_1 * component_2) / component_3

        # update d_angles and angles values
        self.d_alpha += dd_alpha * DELTA
        self.d_beta += dd_beta * DELTA
        self.alpha += self.d_alpha * DELTA
        self.beta += self.d_beta * DELTA

    def calculate_bob1_coords(self):
        # set new coordinates of first bob
        self.bob1_coords = Point(
            self.center_coords.get_x() + self.length1 * np.sin(self.alpha),
            self.center_coords.get_y() + self.length1 * np.cos(self.alpha)
        )

        # add new coordinates to trace line
        self.bob1_tracer.add_coord(
            self.center_coords.get_x() + self.length1 * np.sin(self.alpha),
            self.center_coords.get_y() + self.length1 * np.cos(self.alpha)
        )

    def calculate_bob2_coords(self):
        # set new coordinates of second bob
        self.bob2_coords = Point(
            self.bob1_coords.get_x() + self.length2 * np.sin(self.beta),
            self.bob1_coords.get_y() + self.length2 * np.cos(self.beta)
        )

        # add new coordinates to trace line
        self.bob2_tracer.add_coord(
            self.bob1_coords.get_x() + self.length2 * np.sin(self.beta),
            self.bob1_coords.get_y() + self.length2 * np.cos(self.beta)
        )

    def draw_traces(self):
        # delete previous trace line
        self.canvas.delete('trace')

        # tracing_mode == 1 || 2
        if self.tracing_mode > 0:
            self.draw_trace(
                self.bob1_tracer.get_trace(),
                TRACE_BOB1_COLOR
            )

        # tracing_mode == 2
        if self.tracing_mode > 1:
            self.draw_trace(
                self.bob2_tracer.get_trace(),
                TRACE_BOB2_COLOR
            )

    def draw_trace(self, trace, color):
        trace_length = len(trace)
        for i in range(trace_length - 1):
            self.canvas.create_line(
                trace[i].get_x(),
                trace[i].get_y(),
                trace[i + 1].get_x(),
                trace[i + 1].get_y(),
                fill=color,
                tags=['trace']
            )

    def draw_pendulum(self):
        # delete previous pendulum state
        self.canvas.delete('pendulum')

        # center point of pendulum
        self.canvas.create_oval(
            self.center_coords.get_x() - 3,
            self.center_coords.get_y() - 3,
            self.center_coords.get_x() + 3,
            self.center_coords.get_y() + 3,
            outline='white',
            fill='white',
            tags=['pendulum']
        )

        self.canvas.create_line(
            self.center_coords.get_x(),
            self.center_coords.get_y(),
            self.bob1_coords.get_x(),
            self.bob1_coords.get_y(),
            fill='white',
            tags=['pendulum']
        )

        # first bob
        self.canvas.create_line(
            self.bob1_coords.get_x(),
            self.bob1_coords.get_y(),
            self.bob2_coords.get_x(),
            self.bob2_coords.get_y(),
            fill='white',
            tags=['pendulum']
        )

        self.canvas.create_oval(
            self.bob1_coords.get_x() - 5,
            self.bob1_coords.get_y() - 5,
            self.bob1_coords.get_x() + 5,
            self.bob1_coords.get_y() + 5,
            outline=BOB1_COLOR,
            fill=BOB1_COLOR,
            tags=['pendulum']
        )

        # second bob
        self.canvas.create_oval(
            self.bob2_coords.get_x() - 5,
            self.bob2_coords.get_y() - 5,
            self.bob2_coords.get_x() + 5,
            self.bob2_coords.get_y() + 5,
            outline=BOB2_COLOR,
            fill=BOB2_COLOR,
            tags=['pendulum']
        )

    def initiate_and_grid_tracers(self):
        self.bob1_tracer = tracer.Tracer()
        self.bob1_tracer.add_coord(self.bob1_coords.get_x(), self.bob1_coords.get_y())

        self.bob2_tracer = tracer.Tracer()
        self.bob2_tracer.add_coord(self.bob2_coords.get_x(), self.bob2_coords.get_y())

    def initiate_and_grid_canvas(self):
        self.canvas = tk.Canvas(
            master=self.root,
            background='black',
            width=CANVAS_WIDTH,
            height=CANVAS_HEIGHT
        )
        self.canvas.grid(
            row=0,
            rowspan=10,
            column=3,
            columnspan=10,
            padx=20,
            pady=20
        )
