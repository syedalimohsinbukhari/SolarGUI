"""
Created on Jun 12 12:12:54 2022
"""

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
            t_orb = Q(247.94, 'yr').to('day').value

            self.semi_major_axis = Q(39.482, 'AU')
            self.eccentricity = 0.2488

            super(Pluto().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=t_orb,
                                                            av_orbital_speed=4.737,
                                                            mean_anom=14.53,
                                                            inclination=11.88,
                                                            long_asc=110.299,
                                                            arg_peri=113.834,
                                                            axial_tilt=122.53)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(0.06, 'arcsec'), Q(0.11, 'arcsec')

            d_ = (39.48 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Pluto().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  ap_mag_min=16.3,
                                                                  ap_mag_max=13.65,
                                                                  geom_albedo=0.52,
                                                                  ang_min=ang_min,
                                                                  ang_max=ang_max)
