"""
Created on May 26 01:47:13 2022
"""

import numpy as np
from astropy.constants import codata2018 as c_2018


def convert(parameter, change_to):
    return parameter.to(change_to)


class PhysicalParameters:

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    def volume(self):
        return (4 / 3) * np.pi * self.radius**3

    def density(self):
        return (self.mass / self.volume()).si

    def surface_area(self):
        return (4 * np.pi * self.radius**2).si

    def surface_gravity(self):
        return (c_2018.G * (self.mass / self.radius**2)).si

    def get(self):
        return self.volume(), self.density(), self.surface_area(), self.surface_gravity()
