"""
Created on Jun 12 12:12:24 2022
"""

import numpy as np

try:
    from .cel__CONSTANTS import (EARTH_MASS, EARTH_RADIUS, JUPITER_MASS, JUPITER_RADIUS,
                                 SOL_EARTH_DISTANCE, SOL_EARTH_PERIOD)
    from . import utilities as utils
except ImportError:
    import utilities as utils
    from cel__CONSTANTS import (EARTH_MASS, EARTH_RADIUS, JUPITER_MASS, JUPITER_RADIUS,
                                SOL_EARTH_DISTANCE, SOL_EARTH_PERIOD)


class Mercury:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.503, 'Gyr')
            self.mass = utils.Q(3.3011e23, 'kg')
            self.radius = utils.Q(2439.8, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(0.387098, 'AU')
            self.eccentricity = 0.205630

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(155.8, 'day')
            self.av_orbital_speed = utils.Q(47.36, 'km/s')
            self.mean_anomaly = utils.Q(174.796, 'deg')
            self.inclination = utils.Q(6.35, 'deg')
            self.longitude_of_ascending_node = utils.Q(48.331, 'deg')
            self.argument_of_perihelion = utils.Q(29.124, 'deg')
            self.axial_tilt = utils.Q(2.04, 'arcmin').to('deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 7.25, -2.48
            ang_min, ang_max = utils.Q(4.5, 'arcmin'), utils.Q(13, 'arcmin')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.138
            self.distance_from_earth = SOL_EARTH_DISTANCE - (0.387 * SOL_EARTH_DISTANCE)

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Venus:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.503, 'Gyr')
            self.mass = utils.Q(4.8675e24, 'kg')
            self.radius = utils.Q(6051.8, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(0.728213, 'AU')
            self.eccentricity = 0.006772

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(583.92, 'day')
            self.av_orbital_speed = utils.Q(35.02, 'km/s')
            self.mean_anomaly = utils.Q(50.115, 'deg')
            self.inclination = utils.Q(2.15, 'deg')
            self.longitude_of_ascending_node = utils.Q(76.680, 'deg')
            self.argument_of_perihelion = utils.Q(54.884, 'deg')
            self.axial_tilt = utils.Q(177.36, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.98, -4.92

            ang_min = utils.Q(0, 'arcmin') + utils.Q(9.7, 'arcsec')
            ang_max = utils.Q(1, 'arcmin') + utils.Q(6, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.689
            self.distance_from_earth = SOL_EARTH_DISTANCE - (0.723 * SOL_EARTH_DISTANCE)

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Earth:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.5682, 'Gyr')
            self.mass = EARTH_MASS
            self.radius = EARTH_RADIUS
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = SOL_EARTH_DISTANCE
            self.eccentricity = 0.0167086

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = SOL_EARTH_PERIOD
            self.av_orbital_speed = utils.Q(47.36, 'km/s')
            self.mean_anomaly = utils.Q(29.78, 'deg')
            self.inclination = utils.Q(1.57869, 'deg')
            self.longitude_of_ascending_node = utils.Q(-11.26064, 'deg')
            self.argument_of_perihelion = utils.Q(114.20783, 'deg')
            self.axial_tilt = utils.Q(23.4392811, 'deg')


class Mars:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.603, 'Gyr')
            self.mass = utils.Q(6.4171e23, 'kg')
            self.radius = utils.Q(3398.5, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(1.52368055, 'AU')
            self.eccentricity = 0.0934

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(686.980, 'day')
            self.av_orbital_speed = utils.Q(24.07, 'km/s')
            self.mean_anomaly = utils.Q(19.412, 'deg')
            self.inclination = utils.Q(1.850, 'deg')
            self.longitude_of_ascending_node = utils.Q(49.57854, 'deg')
            self.argument_of_perihelion = utils.Q(286.5, 'deg')
            self.axial_tilt = utils.Q(25.19, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.86, -2.94
            ang_min, ang_max = utils.Q(3.5, 'arcsec'), utils.Q(25.1, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.17
            self.distance_from_earth = (1.52 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Jupiter:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.603, 'Gyr')
            self.mass = JUPITER_MASS
            self.radius = JUPITER_RADIUS
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(5.2038, 'AU')
            self.eccentricity = 0.0489

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(11.862, 'yr').to('day')
            self.av_orbital_speed = utils.Q(13.07, 'km/s')
            self.mean_anomaly = utils.Q(20.020, 'deg')
            self.inclination = utils.Q(1.303, 'deg')
            self.longitude_of_ascending_node = utils.Q(100.464, 'deg')
            self.argument_of_perihelion = utils.Q(273.867, 'deg')
            self.axial_tilt = utils.Q(3.13, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -1.66, -2.94
            ang_min, ang_max = utils.Q(29.8, 'arcsec'), utils.Q(50.1, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.538
            self.distance_from_earth = (5.20 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Saturn:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.503, 'Gyr')
            self.mass = utils.Q(5.6834e26, 'kg')
            self.radius = utils.Q(58232, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(9.5826, 'AU')
            self.eccentricity = 0.0565

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(29.4571, 'yr').to('day')
            self.av_orbital_speed = utils.Q(9.68, 'km/s')
            self.mean_anomaly = utils.Q(317.020, 'deg')
            self.inclination = utils.Q(2.485, 'deg')
            self.longitude_of_ascending_node = utils.Q(113.665, 'deg')
            self.argument_of_perihelion = utils.Q(339.392, 'deg')
            self.axial_tilt = utils.Q(26.73, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.17, -0.55
            ang_min, ang_max = utils.Q(14.5, 'arcsec'), utils.Q(20.1, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.499
            self.distance_from_earth = (9.57 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Uranus:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.503, 'Gyr')
            self.mass = utils.Q(8.6810e25, 'kg')
            self.radius = utils.Q(25362, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(19.19126, 'AU')
            self.eccentricity = 0.04717

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(84.0205, 'yr').to('day')
            self.av_orbital_speed = utils.Q(6.80, 'km/s')
            self.mean_anomaly = utils.Q(142.238600, 'deg')
            self.inclination = utils.Q(0.773, 'deg')
            self.longitude_of_ascending_node = utils.Q(74.006, 'deg')
            self.argument_of_perihelion = utils.Q(96.998857, 'deg')
            self.axial_tilt = utils.Q(97.77, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 6.03, 5.38
            ang_min, ang_max = utils.Q(3.3, 'arcsec'), utils.Q(4.1, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.488
            self.distance_from_earth = (19.17 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()


class Neptune:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.503, 'Gyr')
            self.mass = utils.Q(1.02413e26, 'kg')
            self.radius = utils.Q(24622, 'km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = utils.Q(30.07, 'AU')
            self.eccentricity = 0.008678

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = utils.Q(164.8, 'yr').to('day')
            self.av_orbital_speed = utils.Q(5.43, 'km/s')
            self.mean_anomaly = utils.Q(256.228, 'deg')
            self.inclination = utils.Q(1.770, 'deg')
            self.longitude_of_ascending_node = utils.Q(131.783, 'deg')
            self.argument_of_perihelion = utils.Q(273.187, 'deg')
            self.axial_tilt = utils.Q(28.32, 'deg')

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 8, 7.67
            ang_min, ang_max = utils.Q(2.2, 'arcsec'), utils.Q(2.4, 'arcsec')

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.442
            self.distance_from_earth = (30.18 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
