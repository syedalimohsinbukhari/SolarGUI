"""
Created on Jun 12 12:12:24 2022
"""

import astropy.units as u
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
            self.age = 4.503 * u.Gyr
            self.mass = 3.3011e23 * u.kg
            self.radius = 2439.8 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = (2 * u.arcmin).to(u.deg)

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 7.25, -2.48
            ang_min, ang_max = 4.5 * u.arcmin, 13 * u.arcmin

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
            self.age = 4.503 * u.Gyr
            self.mass = 4.8675e24 * u.kg
            self.radius = 6051.8 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 0.728213 * u.AU
            self.eccentricity = 0.006772

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 583.92 * u.day
            self.av_orbital_speed = 35.02 * u.km * u.s**-1
            self.mean_anomaly = 50.115 * u.deg
            self.inclination = 2.15 * u.deg
            self.longitude_of_ascending_node = 76.680 * u.deg
            self.argument_of_perihelion = 54.884 * u.deg
            self.axial_tilt = 177.36 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -2.98, -4.92
            ang_min, ang_max = 0 * u.arcmin + 9.7 * u.arcsec, 1 * u.arcmin + 6 * u.arcsec

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
            self.age = 4.5682 * u.Gyr
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
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 29.78 * u.deg
            self.inclination = 1.57869 * u.deg
            self.longitude_of_ascending_node = -11.26064 * u.deg
            self.argument_of_perihelion = 114.20783 * u.deg
            self.axial_tilt = 23.4392811 * u.deg


class Mars:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = 6.4171e23 * u.kg
            self.radius = 3398.5 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 1.52368055 * u.AU
            self.eccentricity = 0.0934

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 686.980 * u.day
            self.av_orbital_speed = 24.07 * u.km * u.s**-1
            self.mean_anomaly = 19.412 * u.deg
            self.inclination = 1.850 * u.deg
            self.longitude_of_ascending_node = 49.57854 * u.deg
            self.argument_of_perihelion = 286.5 * u.deg
            self.axial_tilt = 25.19 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.86, -2.94
            ang_min, ang_max = 3.5 * u.arcsec, 25.1 * u.arcsec

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
            self.age = 4.603 * u.Gyr
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
            self.semi_major_axis = 5.2038 * u.AU
            self.eccentricity = 0.0489

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (11.862 * u.yr).to(u.day)
            self.av_orbital_speed = 13.07 * u.km * u.s**-1
            self.mean_anomaly = 20.020 * u.deg
            self.inclination = 1.303 * u.deg
            self.longitude_of_ascending_node = 100.464 * u.deg
            self.argument_of_perihelion = 273.867 * u.deg
            self.axial_tilt = 3.13 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = -1.66, -2.94
            ang_min, ang_max = 29.8 * u.arcsec, 50.1 * u.arcsec

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
            self.age = 4.503 * u.Gyr
            self.mass = 5.6834e26 * u.kg
            self.radius = 58232 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 9.5826 * u.AU
            self.eccentricity = 0.0565

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (29.4571 * u.yr).to(u.day)
            self.av_orbital_speed = 9.68 * u.km * u.s**-1
            self.mean_anomaly = 317.020 * u.deg
            self.inclination = 2.485 * u.deg
            self.longitude_of_ascending_node = 113.665 * u.deg
            self.argument_of_perihelion = 339.392 * u.deg
            self.axial_tilt = 26.73 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 1.17, -0.55
            ang_min, ang_max = 14.5 * u.arcsec, 20.1 * u.arcsec

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
            self.age = 4.503 * u.Gyr
            self.mass = 8.6810e25 * u.kg
            self.radius = 25362 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 19.19126 * u.AU
            self.eccentricity = 0.04717

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (84.0205 * u.yr).to(u.day)
            self.av_orbital_speed = 6.80 * u.km * u.s**-1
            self.mean_anomaly = 142.238600 * u.deg
            self.inclination = 0.773 * u.deg
            self.longitude_of_ascending_node = 74.006 * u.deg
            self.argument_of_perihelion = 96.998857 * u.deg
            self.axial_tilt = 97.77 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 6.03, 5.38
            ang_min, ang_max = 3.3 * u.arcsec, 4.1 * u.arcsec

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
            self.age = 4.503 * u.Gyr
            self.mass = 1.02413e26 * u.kg
            self.radius = 24622 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 30.07 * u.AU
            self.eccentricity = 0.008678

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (164.8 * u.yr).to(u.day)
            self.av_orbital_speed = 5.43 * u.km * u.s**-1
            self.mean_anomaly = 256.228 * u.deg
            self.inclination = 1.770 * u.deg
            self.longitude_of_ascending_node = 131.783 * u.deg
            self.argument_of_perihelion = 273.187 * u.deg
            self.axial_tilt = 28.32 * u.deg

    class ObservationalParameters:

        def __init__(self):
            ap_mag_min, ap_mag_max = 8, 7.67
            ang_min, ang_max = 2.2 * u.arcsec, 2.4 * u.arcsec

            self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            self.geom_albedo = 0.442
            self.distance_from_earth = (30.18 * SOL_EARTH_DISTANCE) - SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
