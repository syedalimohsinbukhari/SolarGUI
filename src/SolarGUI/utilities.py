"""
Created on May 26 01:47:13 2022
"""

import numpy as np
from astropy.constants import codata2018 as c_2018

try:
    from . import celestial_objects as c_objs
    from . import tk_functions as tk_f
except ImportError:
    import celestial_objects as c_objs
    import tk_functions as tk_f


def convert(parameter, change_to):
    return parameter.to(change_to)


class PhysicalParameters:

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

    def volume(self):
        return (4 / 3) * np.pi * self.radius**3

    def density(self):
        return (self.mass / self.volume()).to('g/cm^3')

    def surface_area(self):
        return 4 * np.pi * self.radius**2

    def surface_gravity(self):
        return (c_2018.G * (self.mass / self.radius**2)).si

    def get(self):
        return self.volume(), self.density(), self.surface_area(), self.surface_gravity()


def comparison(c_win, p_ojb, c_obj, c_lbl, reset=False):
    attributes = p_ojb.__dict__.keys()
    num_attributes = len(attributes)
    out = [p_ojb.__getattribute__(attr) / c_obj.__getattribute__(attr) for attr
           in attributes]

    for value, num in zip(out, range(1, num_attributes + 1)):
        if value < 0.001:
            value = f'{value:.5e} × {c_lbl}'
        else:
            value = f'{np.round(value, 5)} × {c_lbl}'

        if not reset:
            tk_f.entry_placement(window=c_win, value=value, row=num, columns=4, width=20)
        else:
            tk_f.entry_placement(window=c_win, value='', row=num, columns=4, width=20)
