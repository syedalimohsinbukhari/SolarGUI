"""
Created on Jun 12 12:12:54 2022
"""

from . import CONSTANTS, _CelestialObject, utilities


class Pluto(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = utilities.Q(4.603, 'Gyr')
            self.mass = utilities.Q(1.303e22, 'kg')
            self.radius = utilities.Q(1188.3, 'km')

            super(Pluto().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            t_orb = utilities.Q(247.94, 'yr').to('day').value

            self.semi_major_axis = utilities.Q(39.482, 'AU')
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

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            ang_min, ang_max = utilities.Q(0.06, 'arcsec'), utilities.Q(0.11, 'arcsec')

            d_ = (39.48 * CONSTANTS.SOL_EARTH_DISTANCE) - CONSTANTS.SOL_EARTH_DISTANCE

            super(Pluto().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  ap_mag_min=16.3,
                                                                  ap_mag_max=13.65,
                                                                  geom_albedo=0.52,
                                                                  ang_min=ang_min,
                                                                  ang_max=ang_max)
