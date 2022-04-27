import pygame as pyg
import numpy as np
from indi import Individual


class Petri:
    def __init__(self, size=[800, 600], scale=1.0, padding=False):
        self.size = size
        self.window_size = [scale * self.size[0], scale * self.size[1]]
        self.time_scale = 1
        self.padding_bool = padding
        self.pop_arr = None

    def get_window_info(self):
        return self.window_size, self.padding_bool

    def get_pop_arr(self):
        return self.pop_arr

    def populate(self):
        #   populate array
        self.pop_arr = np.full((self.size[0], self.size[1]), None)
        for row in self.pop_arr:
            for col in row:
                col = Individual(0, 0)

