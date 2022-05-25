"""
Created on May 24 22:11:20 2022
"""

import astropy.units as u


class Venus:

    def __init__(self):
        self.age = 4.503 * u.Gyr  # google: age of venus planet
        self.mass = 4.8675e24 * u.kg
        self.radius = 6051.8 * u.km
        self.volume = 9.2843e11 * u.km**3
        self.density = 5.243 * u.g * u.cm**-3
        self.surface_area = 4.6023e8 * u.km**2
        self.surface_gravity = 8.87 * u.m * u.s**-2
