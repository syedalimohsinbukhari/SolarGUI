"""
Created on Jun 12 12:12:04 2022
"""

from . import CONSTANTS, _CelestialObject, utilities


class Sun(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = utilities.Q(4.603, 'Gyr')
            self.mass = CONSTANTS.SOL_MASS
            self.radius = CONSTANTS.SOL_RADIUS.to('km')

            super(Sun().PhysicalParameters, self).__init__(mass=self.mass,
                                                           radius=self.radius)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            ang_min, ang_max = utilities.Q(0.527, 'deg'), utilities.Q(0.545, 'deg')

            d_ = CONSTANTS.SOL_EARTH_DISTANCE

            super(Sun().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                apparent_mag=-26.74,
                                                                geom_albedo=0.0001,
                                                                ang_min=ang_min,
                                                                ang_max=ang_max)
