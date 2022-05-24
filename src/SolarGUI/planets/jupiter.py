"""
Created on May 24 22:12:02 2022
"""

import astropy.units as u


class Jupiter:

    def __init__(self):
        self.age = 4.603 * u.Gyr  # google: age of venus planet
        self.mass = 1.8982e27 * u.kg
        self.radius = 69911 * u.km
        self.volume = 1.4313e15 * u.km**3
        self.density = (1326 * u.kg * u.m**-3).to('g/cm^3')
        self.surface_area = 6.1469e10 * u.km**2
        self.surface_gravity = 24.79 * u.m * u.s**-2

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
