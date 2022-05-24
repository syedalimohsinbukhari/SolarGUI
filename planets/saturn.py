"""
Created on May 24 22:12:13 2022
"""

import astropy.units as u


class Saturn:

    def __init__(self):
        self.age = 4.503 * u.Gyr  # google: age of venus planet
        self.mass = 5.6834e26 * u.kg
        self.radius = 58232 * u.km
        self.volume = 8.2713e14 * u.km**3
        self.density = 0.687 * u.g * u.cm**-3
        self.surface_area = 4.27e10 * u.km**2
        self.surface_gravity = 10.44 * u.m * u.s**-2

    def convert_age(self, change_to):
        return self.age.to(change_to)

    def convert_mass(self, change_to):
        return self.mass.to(change_to)

    def convert_radius(self, change_to):
        return self.radius.to(change_to)

    def convert_volume(self, change_to):
        return self.volume.to(change_to)

    def convert_density(self, change_to):
        return self.density.to(change_to)

    def convert_surface_area(self, change_to):
        return self.surface_area.to(change_to)

    def convert_surface_gravity(self, change_to):
        return self.surface_gravity.to(change_to)
