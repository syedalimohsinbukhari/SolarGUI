"""
Created on Jun 12 12:12:36 2022
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


class Moon(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = utils.Q(4.53, 'Gyr')
            self.mass = utils.Q(7.342e22, 'kg')
            self.radius = utils.Q(1737.4, 'km')

            super(Moon().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(384399, 'km').to('AU')
            self.eccentricity = 0.0549

            super(Moon().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                           ecc=self.eccentricity)

            self.orbital_period = utils.Q(27.321661, 'day')
            self.av_orbital_speed = utils.Q(1.022, 'km/s')
            self.mean_anomaly = utils.Q(135.27, 'deg')
            self.inclination = utils.Q(5.145, 'deg')
            self.longitude_of_ascending_node = utils.Q(125.08, 'deg')
            self.argument_of_perihelion = utils.Q(318.15, 'deg')
            self.axial_tilt = utils.Q(1.5427, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.5, -12.9
            ang_min, ang_max = utils.Q(29.3, 'arcmin'), utils.Q(34.1, 'arcmin')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.136
            self.distance_from_earth = 0.00256955529 * SOL_EARTH_DISTANCE

            super(
                    Moon().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)
