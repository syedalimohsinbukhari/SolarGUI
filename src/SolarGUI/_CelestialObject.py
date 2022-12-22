"""
Created on Jun 25 23:53:34 2022
"""

from typing import Optional, Union

import numpy as np
from astropy.units import Quantity
from numpy import ndarray

from . import utilities


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
             self.escape_velocity) = utilities.GetPhysicalParameters(mass=mass,
                                                                     radius=radius).get()

    class OrbitalParameters:
        """
        Base class for the calculation of orbital parameters for the celestial objects.

        """

        def __init__(self, a_0: Quantity,
                     ecc: float,
                     orbital_period: Optional[float] = None,
                     av_orbital_speed: Optional[float] = None,
                     mean_anom: Optional[float] = None,
                     inclination: Optional[float] = None,
                     long_asc: Optional[float] = None,
                     arg_peri: Optional[float] = None,
                     axial_tilt: Optional[float] = None):
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

            self.apo, self.peri = a_0 * (1 - ecc), a_0 * (1 + ecc)

            self.orbital_period = utilities.if_none(val=orbital_period, unit='day')
            self.av_orbital_speed = utilities.if_none(val=av_orbital_speed, unit='km/s')
            self.mean_anomaly = utilities.if_none(val=mean_anom, unit='deg')
            self.inclination = utilities.if_none(val=inclination, unit='deg')
            self.longitude_of_ascending_node = utilities.if_none(val=long_asc, unit='deg')
            self.argument_of_perihelion = utilities.if_none(val=arg_peri, unit='deg')
            self.axial_tilt = utilities.if_none(val=axial_tilt, unit='deg')

    class ObservationalParameters:
        """
        Base class for the calculation of observational parameters for the celestial
        objects.

        """

        def __init__(self,
                     dist_from_earth: Quantity,
                     ap_mag_min: Optional[float] = None,
                     ap_mag_max: Optional[float] = None,
                     apparent_mag: Union[float, ndarray] = None,
                     absolute_mag: Union[float, ndarray] = None,
                     geom_albedo: Optional[float] = None,
                     ang_min: Optional[Quantity] = None,
                     ang_max: Optional[Quantity] = None,
                     av_ang_size: Optional[Quantity] = None):
            """
            Initialization method for ObservationalParameters class.


            Parameters
            ----------
            ang_min : Quantity
                Minimum angular size of the celestial object.
            ang_max : Quantity
                Maximum angular size of the celestial object.
            apparent_mag : Union[float, ndarray]
                Apparent magnitude of the celestial object.
            absolute_mag : Union[float, ndarray]
                Absolute magnitude of the celestial object.
            dist_from_earth : Quantity
                Distance of the celestial object from the Earth.

            Returns
            -------
            None.

            """

            if np.logical_and(apparent_mag is not None,
                              np.logical_and(ap_mag_min is None, ap_mag_max is None)):
                self.apparent_magnitude = apparent_mag
            elif None not in [ap_mag_min, ap_mag_max]:
                self.apparent_magnitude = np.mean([ap_mag_min, ap_mag_max])
            else:
                self.apparent_magnitude = None

            self.geom_albedo = geom_albedo
            self.distance_from_earth = dist_from_earth

            if absolute_mag is not None:
                self.absolute_magnitude = absolute_mag
            elif None not in [self.apparent_magnitude, self.distance_from_earth]:
                self.absolute_magnitude = utilities.get_absolute_magnitude(
                    apparent_magnitude=self.apparent_magnitude,
                    distance=self.distance_from_earth)
            else:
                self.absolute_magnitude = None

            if np.logical_and(av_ang_size is not None,
                              np.logical_and(ang_min is None, ang_max is None)):
                self.average_angular_size = av_ang_size
            elif None not in [ang_min, ang_max]:
                av_ = np.mean([ang_min.si.value, ang_max.si.value])
                self.average_angular_size = utilities.Q(av_, 'rad').to('arcsec')
            else:
                self.average_angular_size = None


c_ = CelestialObject
c_phy = c_.PhysicalParameters
c_orb = c_.OrbitalParameters
c_obs = c_.ObservationalParameters
