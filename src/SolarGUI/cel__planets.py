"""
Created on Jun 12 12:12:24 2022
"""

from numpy import mean

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
                                                              ecc=self.eccentricity)

            self.orbital_period = Q(155.8, 'day')
            self.av_orbital_speed = Q(47.36, 'km/s')
            self.mean_anomaly = Q(174.796, 'deg')
            self.inclination = Q(6.35, 'deg')
            self.longitude_of_ascending_node = Q(48.331, 'deg')
            self.argument_of_perihelion = Q(29.124, 'deg')
            self.axial_tilt = Q(2.04, 'arcmin').to('deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 7.25, -2.48
            ang_min, ang_max = Q(4.5, 'arcmin'), Q(13, 'arcmin')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.138
            self.distance_from_earth = SOL_EARTH_DISTANCE - (0.387 * SOL_EARTH_DISTANCE)

            super(
                    Mercury().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
                                                            ecc=self.eccentricity)

            self.orbital_period = Q(583.92, 'day')
            self.av_orbital_speed = Q(35.02, 'km/s')
            self.mean_anomaly = Q(50.115, 'deg')
            self.inclination = Q(2.15, 'deg')
            self.longitude_of_ascending_node = Q(76.680, 'deg')
            self.argument_of_perihelion = Q(54.884, 'deg')
            self.axial_tilt = Q(177.36, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.98, -4.92

            ang_min = Q(0, 'arcmin') + Q(9.7, 'arcsec')
            ang_max = Q(1, 'arcmin') + Q(6, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.689
            self.distance_from_earth = SOL_EARTH_DISTANCE - (0.723 * SOL_EARTH_DISTANCE)

            super(
                    Venus().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
            self.semi_major_axis = SOL_EARTH_DISTANCE
            self.eccentricity = 0.0167086

            super(Earth().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity)
            self.orbital_period = SOL_EARTH_PERIOD
            self.av_orbital_speed = Q(47.36, 'km/s')
            self.mean_anomaly = Q(29.78, 'deg')
            self.inclination = Q(1.57869, 'deg')
            self.longitude_of_ascending_node = Q(-11.26064, 'deg')
            self.argument_of_perihelion = Q(114.20783, 'deg')
            self.axial_tilt = Q(23.4392811, 'deg')


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
                                                           ecc=self.eccentricity)

            self.orbital_period = Q(686.980, 'day')
            self.av_orbital_speed = Q(24.07, 'km/s')
            self.mean_anomaly = Q(19.412, 'deg')
            self.inclination = Q(1.850, 'deg')
            self.longitude_of_ascending_node = Q(49.57854, 'deg')
            self.argument_of_perihelion = Q(286.5, 'deg')
            self.axial_tilt = Q(25.19, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.86, -2.94
            ang_min, ang_max = Q(3.5, 'arcsec'), Q(25.1, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.17
            self.distance_from_earth = (1.52 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Mars().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
            self.semi_major_axis = Q(5.2038, 'AU')
            self.eccentricity = 0.0489

            super(Jupiter().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity)

            self.orbital_period = Q(11.862, 'yr').to('day')
            self.av_orbital_speed = Q(13.07, 'km/s')
            self.mean_anomaly = Q(20.020, 'deg')
            self.inclination = Q(1.303, 'deg')
            self.longitude_of_ascending_node = Q(100.464, 'deg')
            self.argument_of_perihelion = Q(273.867, 'deg')
            self.axial_tilt = Q(3.13, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = -1.66, -2.94
            ang_min, ang_max = Q(29.8, 'arcsec'), Q(50.1, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.538
            self.distance_from_earth = (5.20 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Jupiter().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
            self.semi_major_axis = Q(9.5826, 'AU')
            self.eccentricity = 0.0565

            super(Saturn().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity)

            self.orbital_period = Q(29.4571, 'yr').to('day')
            self.av_orbital_speed = Q(9.68, 'km/s')
            self.mean_anomaly = Q(317.020, 'deg')
            self.inclination = Q(2.485, 'deg')
            self.longitude_of_ascending_node = Q(113.665, 'deg')
            self.argument_of_perihelion = Q(339.392, 'deg')
            self.axial_tilt = Q(26.73, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.17, -0.55
            ang_min, ang_max = Q(14.5, 'arcsec'), Q(20.1, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.499
            self.distance_from_earth = (9.57 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Saturn().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
            self.semi_major_axis = Q(19.19126, 'AU')
            self.eccentricity = 0.04717

            super(Uranus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity)

            self.orbital_period = Q(84.0205, 'yr').to('day')
            self.av_orbital_speed = Q(6.80, 'km/s')
            self.mean_anomaly = Q(142.238600, 'deg')
            self.inclination = Q(0.773, 'deg')
            self.longitude_of_ascending_node = Q(74.006, 'deg')
            self.argument_of_perihelion = Q(96.998857, 'deg')
            self.axial_tilt = Q(97.77, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 6.03, 5.38
            ang_min, ang_max = Q(3.3, 'arcsec'), Q(4.1, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.488
            self.distance_from_earth = (19.17 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Uranus().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


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
            self.semi_major_axis = Q(30.07, 'AU')
            self.eccentricity = 0.008678

            super(Neptune().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity)

            self.orbital_period = Q(164.8, 'yr').to('day')
            self.av_orbital_speed = Q(5.43, 'km/s')
            self.mean_anomaly = Q(256.228, 'deg')
            self.inclination = Q(1.770, 'deg')
            self.longitude_of_ascending_node = Q(131.783, 'deg')
            self.argument_of_perihelion = Q(273.187, 'deg')
            self.axial_tilt = Q(28.32, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = 8, 7.67
            ang_min, ang_max = Q(2.2, 'arcsec'), Q(2.4, 'arcsec')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.442
            self.distance_from_earth = (30.18 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            super(
                    Neptune().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)
