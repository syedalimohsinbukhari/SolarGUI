"""
Created on May 24 22:12:02 2022
"""

import astropy.units as u


class Jupiter:

    def __init__(self):
        self.age = 4.603 * u.Gyr
        self.mass = 1.8982e27 * u.kg
        self.radius = 69911 * u.km
        self.volume = 1.4313e15 * u.km**3
        self.density = 1.326 * u.g * u.cm**-3
        self.surface_area = 6.1469e10 * u.km**2
        self.surface_gravity = 24.79 * u.m * u.s**-2
