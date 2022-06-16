"""
Created on Jun 12 12:12:04 2022
"""

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE, SOL_MASS, SOL_RADIUS
    from . import utilities as utils
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE, SOL_MASS, SOL_RADIUS
    import utilities as utils


class Sun:

    class PhysicalParameters:

        def __init__(self):
            self.age = utils.Q(4.603, 'Gyr')
            self.mass = SOL_MASS
            self.radius = SOL_RADIUS.to('km')
            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=self.mass,
                                                                 radius=self.radius).get()

    class ObservationalParameters:

        def __init__(self):
            ang_min, ang_max = utils.Q(0.527, 'deg'), utils.Q(0.545, 'deg')

            self.apparent_magnitude = -26.74
            self.geom_albedo = 0.0001
            self.distance_from_earth = SOL_EARTH_DISTANCE

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth).get()
