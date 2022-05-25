"""
Created on May 24 22:12:27 2022
"""

import astropy.units as u


class Neptune:

    def __init__(self):
        self.age = 4.503 * u.Gyr  # google: age of venus planet
        self.mass = 1.02413e26 * u.kg
        self.radius = 24622 * u.km
        self.volume = 6.253e13 * u.km**3
        self.density = 1.638 * u.g * u.cm**-3
        self.surface_area = 7.6187e9 * u.km**2
        self.surface_gravity = 11.15 * u.m * u.s**-2
