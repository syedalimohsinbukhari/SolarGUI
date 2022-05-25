"""
Created on May 24 22:12:19 2022
"""

import astropy.units as u


class Uranus:

    def __init__(self):
        self.age = 4.503 * u.Gyr  # google: age of venus planet
        self.mass = 8.6810e25 * u.kg
        self.radius = 25362 * u.km
        self.volume = 6.833e13 * u.km**3
        self.density = 1.27 * u.g * u.cm**-3
        self.surface_area = 8.1156e9 * u.km**2
        self.surface_gravity = 8.69 * u.m * u.s**-2
