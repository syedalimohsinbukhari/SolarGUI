"""
Created on Jun 25 23:53:34 2022
"""
from src.SolarGUI import utilities as utils


class CelestialObject:

    class PhysicalParameters:

        def __init__(self, mass, radius):
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=mass,
                                                                 radius=radius).get()

    class OrbitalParameters:

        def __init__(self, a_0, ecc):
            self.apo, self.peri = utils.GetOrbitalParameters(a_0=a_0, ecc=ecc).get()

    class ObservationalParameters:

        def __init__(self, ang_min, ang_max, apparent_magnitude, distance_from_earth):
            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=apparent_magnitude,
                    distance=distance_from_earth).get()


c_ = CelestialObject
c_phy = c_.PhysicalParameters
c_orb = c_.OrbitalParameters
c_obs = c_.ObservationalParameters
