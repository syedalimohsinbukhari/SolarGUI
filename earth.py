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

    def convert_mass(self, change_to):
        return self.mass.to(change_to)

    def convert_radius(self, change_to):
        return self.radius.to(change_to)

    def convert_volume(self, change_to):
        return self.volume.to(change_to)

    def convert_surface_area(self, change_to):
        return self.surface_area.to(change_to)

    def convert_surface_gravity(self, change_to):
        return self.surface_gravity.to(change_to)
