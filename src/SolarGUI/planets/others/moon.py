"""
Created on May 25 00:25:57 2022
"""

import astropy.units as u


class Moon:

    def __init__(self):
        self.age = 4.53 * u.Gyr  # google: age of venus planet
        self.mass = 7.342e22 * u.kg
        self.radius = 1737.4 * u.km
        self.volume = 2.1958e10 * u.km**3
        self.density = 3.344 * u.g * u.cm**-3
        self.surface_area = 3.793e7 * u.km**2
        self.surface_gravity = 1.622 * u.m * u.s**-2
