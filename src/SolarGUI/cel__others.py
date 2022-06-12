"""
Created on Jun 12 12:12:54 2022
"""

import astropy.units as u
import numpy as np

try:
    from . import utilities as utils
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
except ImportError:
    import utilities as utils
    from cel__CONSTANTS import SOL_EARTH_DISTANCE


class Pluto:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = 1.303e22 * u.kg
            self.radius = 1188.3 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 39.482 * u.AU
            self.eccentricity = 0.2488

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (247.94 * u.yr).to(u.day)
            self.av_orbital_speed = 4.743 * u.km * u.s**-1
            self.mean_anomaly = 14.53 * u.deg
            self.inclination = 17.16 * u.deg
            self.longitude_of_ascending_node = 110.299 * u.deg
            self.argument_of_perihelion = 113.834 * u.deg
            self.axial_tilt = 122.53 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 16.3, 13.65
            ang_min, ang_max = 0.06 * u.arcsec, 0.11 * u.arcsec

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.52
            self.distance_from_earth = (39.48 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
