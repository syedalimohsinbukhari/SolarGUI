"""
Created on May 26 01:33:39 2022
"""

import astropy.units as u

try:
    from . import utilities as utils
except ImportError:
    import utilities as utils


class Sun:

    def __init__(self):
        self.age = 4.603 * u.Gyr
        self.mass = (1 * u.M_sun).si
        self.radius = (1 * u.R_sun).si.to(u.km)
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Mercury:

    def __init__(self):
        self.age = 4.503 * u.Gyr
        self.mass = 3.3011e23 * u.kg
        self.radius = 2439.8 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Venus:

    def __init__(self):
        self.age = 4.503 * u.Gyr
        self.mass = 4.8675e24 * u.kg
        self.radius = 6051.8 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Earth:

    def __init__(self):
        self.age = 4.5682 * u.Gyr
        self.mass = (1 * u.M_earth).si
        self.radius = (1 * u.R_earth).si.to(u.km)
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Moon:

    def __init__(self):
        self.age = 4.53 * u.Gyr
        self.mass = 7.342e22 * u.kg
        self.radius = 1737.4 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Mars:

    def __init__(self):
        self.age = 4.603 * u.Gyr
        self.mass = 6.4171e23 * u.kg
        self.radius = 3398.5 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Jupiter:

    def __init__(self):
        self.age = 4.603 * u.Gyr
        self.mass = (1 * u.M_jupiter).si
        self.radius = (1 * u.R_jupiter).si.to(u.km)
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Saturn:

    def __init__(self):
        self.age = 4.503 * u.Gyr
        self.mass = 5.6834e26 * u.kg
        self.radius = 58232 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Uranus:

    def __init__(self):
        self.age = 4.503 * u.Gyr
        self.mass = 8.6810e25 * u.kg
        self.radius = 25362 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Neptune:

    def __init__(self):
        self.age = 4.503 * u.Gyr
        self.mass = 1.02413e26 * u.kg
        self.radius = 24622 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()


class Pluto:

    def __init__(self):
        self.age = 4.603 * u.Gyr
        self.mass = 1.303e22 * u.kg
        self.radius = 1188.3 * u.km
        (self.volume,
         self.density,
         self.surface_area,
         self.surface_gravity) = utils.PhysicalParameters(self.mass, self.radius).get()
