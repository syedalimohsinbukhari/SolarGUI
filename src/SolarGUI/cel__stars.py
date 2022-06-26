"""
Created on Jun 12 12:12:04 2022
"""

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE, SOL_MASS, SOL_RADIUS
    from .cel__object import c_, c_phy, c_orb, c_obs
    from .utilities import Q
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE, SOL_MASS, SOL_RADIUS
    from cel__object import c_, c_phy, c_orb, c_obs
    from utilities import Q


class Sun(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = Q(4.603, 'Gyr')
            self.mass = SOL_MASS
            self.radius = SOL_RADIUS.to('km')

            super(Sun().PhysicalParameters, self).__init__(mass=self.mass,
                                                           radius=self.radius)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = Q(0.527, 'deg'), Q(0.545, 'deg')

            d_ = SOL_EARTH_DISTANCE

            super(Sun().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                apparent_mag=-26.74,
                                                                geom_albedo=0.0001,
                                                                ang_min=ang_min,
                                                                ang_max=ang_max)
