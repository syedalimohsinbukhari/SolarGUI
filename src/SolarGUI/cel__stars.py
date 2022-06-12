"""
Created on Jun 12 12:12:04 2022
"""

import astropy.units as u

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
    from . import utilities as utils
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE
    import utilities as utils


class Sun:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = (1 * u.M_sun).si
            self.radius = (1 * u.R_sun).si.to(u.km)
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class ObservationalParameters:

        def __init__(self):
            ang_min, ang_max = 0.527 * u.deg, 0.545 * u.deg

            self.apparent_magnitude = -26.74
            self.geom_albedo = 0.0001
            self.distance_from_earth = SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
