"""
Created on Jun 12 12:12:24 2022
"""

try:
    from .cel__CONSTANTS import (EARTH_MASS, EARTH_RADIUS, JUPITER_MASS, JUPITER_RADIUS,
                                 SOL_EARTH_DISTANCE, SOL_EARTH_PERIOD)
    from .cel__object import c_, c_obs, c_orb, c_phy
    from .utilities import Q
except ImportError:
    from cel__CONSTANTS import (EARTH_MASS, EARTH_RADIUS, JUPITER_MASS, JUPITER_RADIUS,
                                SOL_EARTH_DISTANCE, SOL_EARTH_PERIOD)
    from cel__object import c_, c_obs, c_orb, c_phy
    from utilities import Q


class Mercury(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.503, 'Gyr')
            self.mass = Q(3.3011e23, 'kg')
            self.radius = Q(2439.8, 'km')

            super(Mercury().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(0.387098, 'AU')
            self.eccentricity = 0.205630

            super(Mercury().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=87.9691,
                                                              av_orbital_speed=47.36,
                                                              mean_anom=174.897,
                                                              inclination=3.38,
                                                              long_asc=48.331,
                                                              arg_peri=29.124,
                                                              axial_tilt=2.04 / 60.)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(4.5, 'arcmin'), Q(13, 'arcmin')

            d_ = SOL_EARTH_DISTANCE - (0.387 * SOL_EARTH_DISTANCE)

            super(Mercury().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    ap_mag_min=7.25,
                                                                    ap_mag_max=-2.48,
                                                                    geom_albedo=0.138,
                                                                    ang_min=ang_min,
                                                                    ang_max=ang_max)


class Venus(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.503, 'Gyr')
            self.mass = Q(4.8675e24, 'kg')
            self.radius = Q(6051.8, 'km')

            super(Venus().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(0.728213, 'AU')
            self.eccentricity = 0.006772

            super(Venus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=224.701,
                                                            av_orbital_speed=35.02,
                                                            mean_anom=50.115,
                                                            inclination=3.86,
                                                            long_asc=76.680,
                                                            arg_peri=54.884,
                                                            axial_tilt=177.36)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min = Q(0, 'arcmin') + Q(9.7, 'arcsec')
            ang_max = Q(1, 'arcmin') + Q(6, 'arcsec')

            d_ = SOL_EARTH_DISTANCE - (0.723 * SOL_EARTH_DISTANCE)

            super(Venus().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  ap_mag_min=-2.98,
                                                                  ap_mag_max=-4.92,
                                                                  geom_albedo=0.689,
                                                                  ang_min=ang_min,
                                                                  ang_max=ang_max)


class Earth(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.5682, 'Gyr')
            self.mass = EARTH_MASS
            self.radius = EARTH_RADIUS

            super(Earth().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            t_orb = SOL_EARTH_PERIOD.value

            self.semi_major_axis = Q(1.0, 'AU')
            self.eccentricity = 0.0167086

            super(Earth().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=t_orb,
                                                            av_orbital_speed=29.78,
                                                            mean_anom=358.617,
                                                            inclination=7.155,
                                                            long_asc=-11.26064,
                                                            arg_peri=114.20783,
                                                            axial_tilt=23.4392811)


class Mars(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.603, 'Gyr')
            self.mass = Q(6.4171e23, 'kg')
            self.radius = Q(3398.5, 'km')

            super(Mars().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(1.52368055, 'AU')
            self.eccentricity = 0.0934

            super(Mars().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                           ecc=self.eccentricity,
                                                           orbital_period=686.980,
                                                           av_orbital_speed=24.07,
                                                           mean_anom=19.412,
                                                           inclination=5.65,
                                                           long_asc=49.57854,
                                                           arg_peri=286.5,
                                                           axial_tilt=25.19)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(3.5, 'arcsec'), Q(25.1, 'arcsec')

            d_ = (1.52 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Mars().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                 ap_mag_min=1.86,
                                                                 ap_mag_max=-2.94,
                                                                 geom_albedo=0.17,
                                                                 ang_min=ang_min,
                                                                 ang_max=ang_max)


class Jupiter(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.603, 'Gyr')
            self.mass = JUPITER_MASS
            self.radius = JUPITER_RADIUS

            super(Jupiter().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            t_orb = Q(11.862, 'yr').to('day').value

            self.semi_major_axis = Q(5.2038, 'AU')
            self.eccentricity = 0.0489

            super(Jupiter().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=t_orb,
                                                              av_orbital_speed=13.07,
                                                              mean_anom=20.020,
                                                              inclination=6.09,
                                                              long_asc=100.464,
                                                              arg_peri=273.867,
                                                              axial_tilt=3.13)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(29.8, 'arcsec'), Q(50.1, 'arcsec')

            d_ = (5.20 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Jupiter().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    ap_mag_min=-1.66,
                                                                    ap_mag_max=-2.94,
                                                                    geom_albedo=0.538,
                                                                    ang_min=ang_min,
                                                                    ang_max=ang_max)


class Saturn(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.503, 'Gyr')
            self.mass = Q(5.6834e26, 'kg')
            self.radius = Q(58232, 'km')

            super(Saturn().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            t_orb = Q(29.4571, 'yr').to('day').value

            self.semi_major_axis = Q(9.5826, 'AU')
            self.eccentricity = 0.0565

            super(Saturn().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=t_orb,
                                                             av_orbital_speed=9.68,
                                                             mean_anom=317.020,
                                                             inclination=5.51,
                                                             long_asc=113.665,
                                                             arg_peri=339.392,
                                                             axial_tilt=26.73)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(14.5, 'arcsec'), Q(20.1, 'arcsec')

            d_ = (9.57 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Saturn().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   ap_mag_min=1.17,
                                                                   ap_mag_max=-0.55,
                                                                   geom_albedo=0.499,
                                                                   ang_min=ang_min,
                                                                   ang_max=ang_max)


class Uranus(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.503, 'Gyr')
            self.mass = Q(8.6810e25, 'kg')
            self.radius = Q(25362, 'km')

            super(Uranus().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            t_orb = Q(84.0205, 'yr').to('day').value

            self.semi_major_axis = Q(19.19126, 'AU')
            self.eccentricity = 0.04717

            super(Uranus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=t_orb,
                                                             av_orbital_speed=6.80,
                                                             mean_anom=142.2386,
                                                             inclination=6.48,
                                                             long_asc=74.006,
                                                             arg_peri=96.998857,
                                                             axial_tilt=97.77)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(3.3, 'arcsec'), Q(4.1, 'arcsec')

            d_ = (19.17 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Uranus().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   ap_mag_min=6.03,
                                                                   ap_mag_max=5.38,
                                                                   geom_albedo=0.488,
                                                                   ang_min=ang_min,
                                                                   ang_max=ang_max)


class Neptune(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.503, 'Gyr')
            self.mass = Q(1.02413e26, 'kg')
            self.radius = Q(24622, 'km')

            super(Neptune().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            t_orb = Q(164.8, 'yr').to('day').value

            self.semi_major_axis = Q(30.07, 'AU')
            self.eccentricity = 0.008678

            super(Neptune().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=t_orb,
                                                              av_orbital_speed=5.43,
                                                              mean_anom=256.228,
                                                              inclination=6.43,
                                                              long_asc=131.783,
                                                              arg_peri=273.187,
                                                              axial_tilt=28.32)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(2.2, 'arcsec'), Q(2.4, 'arcsec')

            d_ = (30.18 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(Neptune().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    ap_mag_min=8,
                                                                    ap_mag_max=7.67,
                                                                    geom_albedo=0.442,
                                                                    ang_min=ang_min,
                                                                    ang_max=ang_max)
