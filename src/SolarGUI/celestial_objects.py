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
            self.orbital_period = 0 * u.day
            self.av_orbital_speed = 0 * u.km * u.s**-1
            self.mean_anomaly = 0 * u.deg
            self.inclination = 0 * u.deg
            self.longitude_of_ascending_node = 0 * u.deg
            self.argument_of_perihelion = 0 * u.deg
            self.axial_tilt = 0 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.orbital_period = 583.92 * u.day
            self.av_orbital_speed = 35.02 * u.km * u.s**-1
            self.mean_anomaly = 50.115 * u.deg
            self.inclination = 2.15 * u.deg
            self.longitude_of_ascending_node = 76.680 * u.deg
            self.argument_of_perihelion = 54.884 * u.deg
            self.axial_tilt = 177.36 * u.deg

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()


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
            self.semi_major_axis = 0.387098 * u.AU
            self.eccentricity = 0.205630
            self.orbital_period = 155.8 * u.day
            self.av_orbital_speed = 47.36 * u.km * u.s**-1
            self.mean_anomaly = 174.796 * u.deg
            self.inclination = 6.35 * u.deg
            self.longitude_of_ascending_node = 48.331 * u.deg
            self.argument_of_perihelion = 29.124 * u.deg
            self.axial_tilt = 2 * u.min

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity).get()
