"""
Created on Jun 12 12:12:36 2022
"""

import astropy.units as u
import numpy as np

try:
    from . import utilities as utils
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
except ImportError:
    import utilities as utils
    from cel__CONSTANTS import SOL_EARTH_DISTANCE


class Moon:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.53 * u.Gyr
            self.mass = 7.342e22 * u.kg
            self.radius = 1737.4 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = (384399 * u.km).to(u.AU)
            self.eccentricity = 0.0549

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 27.321661 * u.day
            self.av_orbital_speed = 1.022 * u.km * u.s**-1
            self.mean_anomaly = 135.27 * u.deg
            self.inclination = 5.145 * u.deg
            self.longitude_of_ascending_node = 125.08 * u.deg
            self.argument_of_perihelion = 318.15 * u.deg
            self.axial_tilt = 1.5427 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.5, -12.9
            ang_min, ang_max = 29.3 * u.arcmin, 34.1 * u.arcmin

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.136
            self.distance_from_earth = 0.00256955529 * SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
