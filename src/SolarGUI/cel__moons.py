"""
Created on Jun 12 12:12:36 2022
"""

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
            self.age = utils.Q(4.53, 'Gyr')
            self.mass = utils.Q(7.342e22, 'kg')
            self.radius = utils.Q(1737.4, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(384399, 'km').to('AU')
            self.eccentricity = 0.0549

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(27.321661, 'day')
            self.av_orbital_speed = utils.Q(1.022, 'km/s')
            self.mean_anomaly = utils.Q(135.27, 'deg')
            self.inclination = utils.Q(5.145, 'deg')
            self.longitude_of_ascending_node = utils.Q(125.08, 'deg')
            self.argument_of_perihelion = utils.Q(318.15, 'deg')
            self.axial_tilt = utils.Q(1.5427, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.5, -12.9
            ang_min, ang_max = utils.Q(29.3, 'arcmin'), utils.Q(34.1, 'arcmin')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.136
            self.distance_from_earth = 0.00256955529 * SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
