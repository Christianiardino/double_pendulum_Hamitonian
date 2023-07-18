import numpy as np
import random
from scipy.integrate import odeint
from tkinter import *


class double_pendulum:
    def __init__(self, canvas, width, height, t_one, t_two, len_one, len_two, mass_one, mass_two, gravity,
                 vel_one, vel_two, total_time, time_step, arm_visible, ball_visible, ball_two_visible, tracer_visible):
        self.canvas = canvas
        self.t_one = t_one
        self.len_one = len_one
        self.t_two = t_two
        self.len_two = len_two
        self.mass_one = mass_one
        self.mass_two = mass_two
        self.vel_one = vel_one
        self.vel_two = vel_two
        self.gravity = gravity
        self.width = width
        self.height = height
        self.total_time = total_time
        self.time_step = time_step
        self.arm_visible = arm_visible
        self.ball_visible = ball_visible
        self.ball_two_visible = ball_two_visible
        self.tracer_visible = tracer_visible

        self.mass_draw_one = 10 * np.log10(mass_one * 10)
        self.mass_draw_two = 10 * np.log10(mass_two * 10)
        self.len_draw_one = len_one * 100
        self.len_draw_two = len_two * 100

        # Create arm One
        self.arm_one_x0 = self.width / 2
        self.arm_one_x1 = self.arm_one_x0 + self.len_draw_one * np.sin(self.t_one)
        self.arm_one_y0 = self.height / 2
        self.arm_one_y1 = self.arm_one_y0 + self.len_draw_one * np.cos(self.t_one)
        # Create arm Two
        self.arm_two_x0 = self.arm_one_x1
        self.arm_two_x1 = self.arm_two_x0 + self.len_draw_two * np.sin(self.t_two)
        self.arm_two_y0 = self.arm_one_y1
        self.arm_two_y1 = self.arm_two_y0 + self.len_draw_two * np.cos(self.t_two)

        if self.arm_visible:
            self.arm_one = self.canvas.create_line(self.arm_one_x0, self.arm_one_y0,
                                                   self.arm_one_x1, self.arm_one_y1,
                                                   width=5, fill="#FFFFFF")
            self.arm_two = self.canvas.create_line(self.arm_two_x0, self.arm_two_y0,
                                                   self.arm_two_x1, self.arm_two_y1,
                                                   width=5, fill="#FFFFFF")

        # Create ball
        self.ball_color = "#" + str(hex(random.randrange(0, 0xcccccc))[2:])
        while len(self.ball_color) <= 6:
            self.ball_color += "0"

        if self.ball_visible:
            self.ball_one = canvas.create_oval(self.arm_one_x1 - self.mass_draw_one,
                                               self.arm_one_y1 - self.mass_draw_one,
                                               self.arm_one_x1 + self.mass_draw_one,
                                               self.arm_one_y1 + self.mass_draw_one,
                                               fill=self.ball_color, outline="")

        if not self.ball_two_visible:
            self.mass_draw_two = 1
            self.ball_two = canvas.create_oval(self.arm_two_x1 - self.mass_draw_two,
                                                self.arm_two_y1 - self.mass_draw_two,
                                                self.arm_two_x1 + self.mass_draw_two,
                                                self.arm_two_y1 + self.mass_draw_two,
                                                fill="#000000", outline="")

        if self.ball_two_visible:
            self.ball_two = canvas.create_oval(self.arm_two_x1 - self.mass_draw_two,
                                               self.arm_two_y1 - self.mass_draw_two,
                                               self.arm_two_x1 + self.mass_draw_two,
                                               self.arm_two_y1 + self.mass_draw_two,
                                               fill=self.ball_color, outline="")

        # Create background for pixels
        if self.tracer_visible:
            self.img = PhotoImage(width=self.width, height=self.height)
            self.canvas.create_image((self.width / 2, self.height / 2), image=self.img, state="normal")

    def calculate_new_position(self, theta_one, theta_two):
        cord_two = self.canvas.coords(self.ball_two)

        one_x1 = self.arm_one_x0 + self.len_draw_one * np.sin(theta_one)
        one_y1 = self.arm_one_y0 + self.len_draw_one * np.cos(theta_one)

        if self.arm_visible:
            self.canvas.coords(self.arm_one, self.arm_one_x0, self.arm_one_y0, one_x1, one_y1)

        if self.ball_visible:
            self.canvas.coords(self.ball_one, one_x1 - self.mass_draw_one, one_y1 - self.mass_draw_one,
                               one_x1 + self.mass_draw_one, one_y1 + self.mass_draw_one)

        two_x1 = one_x1 + self.len_draw_two * np.sin(theta_two)
        two_y1 = one_y1 + self.len_draw_two * np.cos(theta_two)

        if self.arm_visible:
            self.canvas.coords(self.arm_two, one_x1, one_y1, two_x1, two_y1)

        self.canvas.coords(self.ball_two, two_x1 - self.mass_draw_two, two_y1 - self.mass_draw_two,
                            two_x1 + self.mass_draw_two, two_y1 + self.mass_draw_two)

        # Self.img.put(self.ball_color, (int(two_x1), int(two_y1)))
        if self.tracer_visible:
            self.canvas.create_line(int(cord_two[0] + self.mass_draw_two), int(cord_two[1] + self.mass_draw_two),
                                    two_x1, two_y1, width=1, fill=self.ball_color)

    def equations(self, y, t, mass_one, mass_two, len_one, len_two):
        gravity = self.gravity

        t_one_, vel_one_, t_two_, vel_two_ = y
        t1_t2 = t_one_ - t_two_
        cos_t1_t2 = np.cos(t1_t2)
        sin_t1_t2 = np.sin(t1_t2)
        v1_2 = vel_one_ ** 2
        v2_2 = vel_two_ ** 2

        w1 = vel_one_
        w2 = vel_two_

        # p1 = mass_two * gravity * sin_t2 * cos_t1_t2
        # p2 = -(mass_two * sin_t1_t2 * ((len_one * v1_2 * cos_t1_t2) + (len_two * v2_2)))
        # p3 = -((mass_one + mass_two) * gravity * sin_t1)
        #
        # q1 = mass_one + mass_two
        # q2 = len_one * v1_2 * sin_t1_t2
        # q3 = -(gravity * sin_t2)
        # q4 = gravity * sin_t1 * cos_t1_t2
        # q5 = mass_two * len_two * v2_2 * sin_t1_t2 * cos_t1_t2
        #
        # d = mass_one + (mass_two * (sin_t1_t2 ** 2))
        #
        # w1_dot = (p1 + p2 + p3) / (len_one * d)
        # w2_dot = ((q1 * (q2 + q3 + q4)) + q5)/ (len_two * d)

        w1_dot = (mass_two * gravity * np.sin(t_two_) * cos_t1_t2 - mass_two * sin_t1_t2 * (
                len_one * v1_2 * cos_t1_t2 + len_two * v2_2) - (mass_one + mass_two) * gravity * np.sin(
            t_one_)) / len_one / (mass_one + mass_two * sin_t1_t2 ** 2)

        w2_dot = ((mass_one + mass_two) * (len_one * v1_2 * sin_t1_t2 - gravity * np.sin(t_two_) + gravity * np.sin(
            t_one_) * cos_t1_t2) + mass_two * len_two * v2_2 * sin_t1_t2 * cos_t1_t2) / len_two / (
                         mass_one + mass_two * sin_t1_t2 ** 2)

        return w1, w1_dot, w2, w2_dot

    def calc_position(self):
        y_ = odeint(self.equations, np.array([self.t_one, self.vel_one, self.t_two, self.vel_two]),
                    np.arange(0, self.total_time, self.time_step),
                    args=(self.mass_one, self.mass_two, self.len_one, self.len_two))
        return y_
