"""
Created on Jun 12 12:12:54 2022
"""

from numpy import mean

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
    from .cel__object import c_, c_phy, c_orb, c_obs
    from .utilities import Q
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE
    from cel__object import c_, c_phy, c_orb, c_obs
    from utilities import Q


class Pluto(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.603, 'Gyr')
            self.mass = Q(1.303e22, 'kg')
            self.radius = Q(1188.3, 'km')

            super(Pluto().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(39.482, 'AU')
            self.eccentricity = 0.2488

            super(Pluto().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity)

            self.orbital_period = Q(247.94, 'yr').to('day')
            self.av_orbital_speed = Q(4.743, 'km/s')
            self.mean_anomaly = Q(14.53, 'deg')
            self.inclination = Q(17.16, 'deg')
            self.longitude_of_ascending_node = Q(110.299, 'deg')
            self.argument_of_perihelion = Q(113.834, 'deg')
            self.axial_tilt = Q(122.53, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 16.3, 13.65
            ang_min, ang_max = Q(0.06, 'arcsec'), Q(0.11, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.52
            self.distance_from_earth = (39.48 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Pluto().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)
