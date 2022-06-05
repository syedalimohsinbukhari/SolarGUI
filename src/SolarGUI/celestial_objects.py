"""
Created on May 26 01:33:39 2022
"""

import astropy.units as u

try:
    from . import utilities as utils
except ImportError:
    import utilities as utils


class Sun:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = (1 * u.M_sun).si
            self.radius = (1 * u.R_sun).si.to(u.km)
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(self.mass,
                                                                 self.radius).get()

    class OrbitalParameters:
        def __init__(self):
            self.semi_major_axis = 0 * u.AU
            self.eccentricity = 0

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 0 * u.day
            self.av_orbital_speed = 0 * u.km * u.s**-1
            self.mean_anomaly = 0 * u.deg
            self.inclination = 0 * u.deg
            self.longitude_of_ascending_node = 0 * u.deg
            self.argument_of_perihelion = 0 * u.deg
            self.axial_tilt = 0 * u.deg


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


class Earth:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.5682 * u.Gyr
            self.mass = (1 * u.M_earth).si
            self.radius = (1 * u.R_earth).si.to(u.km)
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 1 * u.AU
            self.eccentricity = 0.0167086

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 365.256363004 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 29.78 * u.deg
            self.inclination = 1.57869 * u.deg
            self.longitude_of_ascending_node = -11.26064 * u.deg
            self.argument_of_perihelion = 114.20783 * u.deg
            self.axial_tilt = 23.4392811 * u.deg


class Moon:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.53 * u.Gyr
            self.mass = 7.342e22 * u.kg
            self.radius = 1737.4 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity, self.escape_velocity) = utils.GetPhysicalParameters(
                    mass=self.mass,
                    radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = (384399 * u.km).to(u.AU)
            self.eccentricity = 0.0549

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = 27.321661 * u.day
            self.av_orbital_speed = 1.022 * u.km * u.s**-1
            self.mean_anomaly = 135.27 * u.deg
            self.inclination = 5.145 * u.deg
            self.longitude_of_ascending_node = 125.08 * u.deg
            self.argument_of_perihelion = 318.15 * u.deg
            self.axial_tilt = 1.5427 * u.deg


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


class Jupiter:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = (1 * u.M_jupiter).si
            self.radius = (1 * u.R_jupiter).si.to(u.km)
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity, self.escape_velocity) = utils.GetPhysicalParameters(
                    mass=self.mass,
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


class Uranus:

    class PhysicalParameters:
        def __init__(self):
            self.age = 4.503 * u.Gyr
            self.mass = 8.6810e25 * u.kg
            self.radius = 25362 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity, self.escape_velocity) = utils.GetPhysicalParameters(
                    mass=self.mass,
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


class Pluto:

    class PhysicalParameters:

        def __init__(self):
            self.age = 4.603 * u.Gyr
            self.mass = 1.303e22 * u.kg
            self.radius = 1188.3 * u.km
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class OrbitalParameters:

        def __init__(self):
            self.semi_major_axis = 39.482 * u.AU
            self.eccentricity = 0.2488

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()

            self.orbital_period = (247.94 * u.yr).to(u.day)
            self.av_orbital_speed = 4.743 * u.km * u.s**-1
            self.mean_anomaly = 14.53 * u.deg
            self.inclination = 17.16 * u.deg
            self.longitude_of_ascending_node = 110.299 * u.deg
            self.argument_of_perihelion = 113.834 * u.deg
            self.axial_tilt = 122.53 * u.deg
