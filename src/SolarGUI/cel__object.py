"""
Created on Jun 25 23:53:34 2022
"""

from typing import Union

from astropy.units import Quantity
from numpy import ndarray

try:
    from . import utilities as utils
except ImportError:
    import utilities as utils


class CelestialObject:
    """
    Base class for the celestial objects and the calculations for their parameters.
    
    """

    class PhysicalParameters:
        """
        Base class for the calculation of physical parameters for the celestial objects.

        """

        def __init__(self, mass: Quantity, radius: Quantity):
            """
            Initialization method for PhysicalParameters class.

            Parameters
            ----------
            mass : Quantity
                Mass of the celestial object.
            radius : Quantity
                Radius of the celestial object.

            Returns
            -------
            None.

            """

            (self.volume,
             self.density,
             self.surface_area,
             self.surface_gravity,
             self.escape_velocity) = utils.GetPhysicalParameters(mass=mass,
                                                                 radius=radius).get()

    class OrbitalParameters:
        """
        Base class for the calculation of orbital parameters for the celestial objects.

        """

        def __init__(self, a_0: Quantity, ecc: float):
            """
            Initialization method for OrbitalParameters class

            Parameters
            ----------
            a_0 : Quantity
                Semi-major axis of the celestial object's orbit.
            ecc : float
                Eccentricity of the orbit.

            Returns
            -------
            None.

            """

            self.apo, self.peri = utils.GetOrbitalParameters(a_0=a_0, ecc=ecc).get()

    class ObservationalParameters:
        """
        Base class for the calculation of observational parameters for the celestial
        objects.

        """

        def __init__(self, ang_min: Quantity, ang_max: Quantity,
                     apparent_magnitude: Union[float, ndarray],
                     distance_from_earth: Quantity):
            """
            Initialization method for ObservationalParameter class.
            

            Parameters
            ----------
            ang_min : Quantity
                Minimum angular size of the celestial object.
            ang_max : Quantity
                Maximum angular size of the celestial object.
            apparent_magnitude : Union[float, ndarray]
                Apparent magnitude of the celestial object.
            distance_from_earth : Quantity
                Distance of the celestial object from the Earth.

            Returns
            -------
            None.

            """

            (self.absolute_magnitude,
             self.average_angular_size) = utils.GetObservationalParameters(
                    angular_size=tuple([ang_min, ang_max]),
                    apparent_magnitude=apparent_magnitude,
                    distance=distance_from_earth).get()


c_ = CelestialObject
c_phy = c_.PhysicalParameters
c_orb = c_.OrbitalParameters
c_obs = c_.ObservationalParameters
