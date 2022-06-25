"""
Created on Jun 12 12:12:36 2022
"""

from numpy import mean

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
    from .cel__object import c_, c_phy, c_orb, c_obs
    from .cel__planets import Mars
    from .utilities import Q
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE
    from cel__object import c_, c_phy, c_orb, c_obs
    from cel__planets import Mars
    from utilities import Q


class Deimos(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = 'NA'
            self.mass = Q(1.4762e15, 'kg')
            self.radius = Q(6.2, 'km')

            super(Deimos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(23463.2, 'km').to('AU')
            self.eccentricity = 0.00033

            super(Deimos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity)

            self.orbital_period = Q(1.263, 'day')
            self.av_orbital_speed = Q(1.3513, 'km/s')
            self.mean_anomaly = 'NA'
            self.inclination = Q(0.92, 'deg')
            self.longitude_of_ascending_node = 'NA'
            self.argument_of_perihelion = 'NA'
            self.axial_tilt = 'NA'

    class ObservationalParameters(c_obs):

        def __init__(self):
            m_ = Mars().ObservationalParameters()
            ang_min = ang_max = Q(2.5, 'arcmin')

            self.apparent_magnitude = 12.89
            self.geom_albedo = 0.068
            self.distance_from_earth = m_.distance_from_earth

            super(
                    Deimos().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


class Phobos(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = 'NA'
            self.mass = Q(1.0658e16, 'kg')
            self.radius = Q(11.2667, 'km')

            super(Phobos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(9367, 'km').to('AU')
            self.eccentricity = 0.0151

            super(Phobos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity)

            self.orbital_period = Q(0.31891023, 'day')
            self.av_orbital_speed = Q(2.138, 'km/s')
            self.mean_anomaly = 'NA'
            self.inclination = Q(1.093, 'deg')
            self.longitude_of_ascending_node = 'NA'
            self.argument_of_perihelion = 'NA'
            self.axial_tilt = Q(0, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            m_ = Mars().ObservationalParameters()
            ang_min, ang_max = Q(0.14, 'deg'), Q(0.20, 'deg')

            self.apparent_magnitude = 11.8
            self.geom_albedo = 0.071
            self.distance_from_earth = m_.distance_from_earth

            super(
                    Phobos().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)


class Moon(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.53, 'Gyr')
            self.mass = Q(7.342e22, 'kg')
            self.radius = Q(1737.4, 'km')

            super(Moon().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = Q(384399, 'km').to('AU')
            self.eccentricity = 0.0549

            super(Moon().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                           ecc=self.eccentricity)

            self.orbital_period = Q(27.321661, 'day')
            self.av_orbital_speed = Q(1.022, 'km/s')
            self.mean_anomaly = Q(135.27, 'deg')
            self.inclination = Q(5.145, 'deg')
            self.longitude_of_ascending_node = Q(125.08, 'deg')
            self.argument_of_perihelion = Q(318.15, 'deg')
            self.axial_tilt = Q(1.5427, 'deg')

    class ObservationalParameters(c_obs):

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.5, -12.9
            ang_min, ang_max = Q(29.3, 'arcmin'), Q(34.1, 'arcmin')

            self.apparent_magnitude = mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.136
            self.distance_from_earth = 0.00256955529 * SOL_EARTH_DISTANCE

            super(
                    Moon().ObservationalParameters, self
                    ).__init__(ang_min=ang_min,
                               ang_max=ang_max,
                               apparent_magnitude=self.apparent_magnitude,
                               distance_from_earth=self.distance_from_earth)
