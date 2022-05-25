"""
Created on May 24 22:11:11 2022
"""

import astropy.units as u


class Mercury:

    def __init__(self):
        self.age = 4.503 * u.Gyr  # google: age of mercury planet
        self.mass = 3.3011e23 * u.kg
        self.radius = 2439.8 * u.km
        self.volume = 6.083e10 * u.km**3
        self.density = 4.527 * u.g * u.cm**-3
        self.surface_area = 7.48e7 * u.km**2
        self.surface_gravity = 3.7 * u.m * u.s**-2
