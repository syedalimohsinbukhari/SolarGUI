"""
Created on Jun 12 12:12:54 2022
"""

import numpy as np

try:
    from . import utilities as utils
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
    from .cel__object import c_, c_phy, c_orb, c_obs
except ImportError:
    import utilities as utils
    from cel__CONSTANTS import SOL_EARTH_DISTANCE
    from cel__object import c_, c_phy, c_orb, c_obs


class Pluto(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = utils.Q(4.603, 'Gyr')
            self.mass = utils.Q(1.303e22, 'kg')
            self.radius = utils.Q(1188.3, 'km')

            super(Pluto().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(39.482, 'AU')
            self.eccentricity = 0.2488

            super(Pluto().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity)

            self.orbital_period = utils.Q(247.94, 'yr').to('day')
            self.av_orbital_speed = utils.Q(4.743, 'km/s')
            self.mean_anomaly = utils.Q(14.53, 'deg')
            self.inclination = utils.Q(17.16, 'deg')
            self.longitude_of_ascending_node = utils.Q(110.299, 'deg')
            self.argument_of_perihelion = utils.Q(113.834, 'deg')
            self.axial_tilt = utils.Q(122.53, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 16.3, 13.65
            ang_min, ang_max = utils.Q(0.06, 'arcsec'), utils.Q(0.11, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.52
            self.distance_from_earth = (39.48 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Pluto().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)
