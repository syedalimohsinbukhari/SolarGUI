"""
Created on May 22 01:22:02 2022
"""

import astropy.units as u


class Earth:

    def __init__(self):
        self.mass = (1 * u.Mearth).si.value * u.kg
        self.radius = (1 * u.Rearth).si.value * u.m
        self.volume = 1.08321e12 * u.km**3
        self.surface_area = 510072000 * u.km**2
        self.surface_gravity = 9.80665 * u.m * u.s**-2

    def convert_mass(self, into):
        return self.mass.to('Msun') if into == 'Msun' else self.mass
