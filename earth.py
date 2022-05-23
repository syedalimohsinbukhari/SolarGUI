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

    def convert_radius(self, into):
        if into == 'km':
            out = self.radius.to('km')
        elif into == 'Rsun':
            out = self.radius.to('Rsun')
        else:
            out = self.radius

        return out

    def convert_surface_area(self, into):
        if into == 'm2':
            out = self.surface_area.to('m**2')
        elif into == 'Rsun2':
            out = self.surface_area.to('Rsun**2')
        else:
            out = self.surface_area

        return out
