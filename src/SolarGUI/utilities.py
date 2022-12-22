"""
Created on May 26 01:47:13 2022
"""

from typing import Any, Optional, Tuple, Union

import numpy as np
from astropy.constants import codata2018 as c_2018
from astropy.units.quantity import Quantity

N_float = Union[float, np.float_, np.ndarray]


def convert(parameter: Quantity, change_to: str) -> Quantity:
    """
    Change the unit of given Quantity to change_to unit string.

    Parameters
    ----------
    parameter : Quantity
        Input value for the celestial object parameter of which the unit is to be changed.
    change_to : str
        String representing the unit to change the quantity into.

    Returns
    -------
    Quantity
        The celestial object parameter with changed unit.

    """
    return parameter.to(change_to) if not change_to == '' else parameter


def get_absolute_magnitude(apparent_magnitude: float, distance: Quantity) -> float:
    """
    Calculates the absolute magnitude for the celestial object.

    Parameters
    -------
    apparent_magnitude: float
        Apparent magnitude of the celestial object.
    distance: Quantity
        Distance of the celestial object from the Earth.

    Returns
    -------
    float:
        Absolute magnitude of the celestial object.

    """
    distance = distance.to('pc')
    return apparent_magnitude - 5 * np.log10(distance.value) + 5


class GetPhysicalParameters:
    """
    Class to determine the physical parameters for the celestial objects.

    """

    def __init__(self, mass: Quantity, radius: Quantity):
        """
        Initialization function for GetPhysicalParameter class.

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
        self.mass = mass
        self.radius = radius

    def volume(self) -> Quantity:
        """
        Calculate the volume of the celestial object assuming the object in spherical.

        Returns
        -------
        Quantity
            Volume of the celestial object.

        """
        return (4 / 3) * np.pi * self.radius**3

    def density(self) -> Quantity:
        """
        Calculate the mass density of the celestial object.

        Returns
        -------
        Quantity
            Density of the celestial object.

        """
        return (self.mass / self.volume()).to('g/cm^3')

    def surface_area(self) -> Quantity:
        """
        Calculate the surface area of the celestial object.

        Returns
        -------
        Quantity
            Surface are of the celestial object.

        """
        return 4 * np.pi * self.radius**2

    def surface_gravity(self) -> Quantity:
        """
        Calculate the surface gravity of the celestial object.

        Returns
        -------
        Quantity
            Surface gravity of the celestial object.

        """
        return (c_2018.G * (self.mass / self.radius**2)).si

    def escape_velocity(self) -> Quantity:
        """
        Calculate the escape velocity of the celestial object.

        Returns
        -------
        Quantity
            Escape velocity of the celestial object.

        """
        return (np.sqrt(2 * c_2018.G * self.mass * self.radius**-1)).to('km/s')

    def get(self) -> Tuple[Quantity, Quantity, Quantity, Quantity, Quantity]:
        """
        Get the values of volume, density, surface area, and surface gravity of the celestial object.

        """
        return self.volume(), self.density(), self.surface_area(), self.surface_gravity(), self.escape_velocity()


def Q(value: Union[float, np.ndarray], unit: str) -> Quantity:
    """
    This function initializes the value, unit pair of physical quantities.

    Parameters
    ----------
    value : float
        The value of the physical quantity.
    unit : str
        The unit of the physical quantity.

    Returns
    -------
    Quantity
        Physical quantity with value and unit.

    """
    return Quantity(value=value, unit=unit)


def if_none(val: float = None, unit: str = None) -> Optional[Quantity]:
    """
    Gives the output for input value and its units, or returns None

    Parameters
    ----------
    val : float, optional
        Magnitude of the physical quantity.
    unit : str, optional
        Unit of the physical quantity.

    Returns
    -------
    Quantity or None

    """
    return None if None in [val, unit] else Q(value=val, unit=unit)


pars_ = {'t_orb': [('s', 'hr', 'day', 'yr', 'Myr'), 'day'],
         'v_orb': [('cm/s', 'm/s', 'km/s', 'km/h'), 'km/s'],
         'm_anom': [('deg', 'rad'), 'deg'],
         'incl': [('deg', 'rad'), 'deg'],
         'long': [('deg', 'rad'), 'deg'],
         'arg': [('deg', 'rad'), 'deg'],
         'tilt': [('deg', 'rad'), 'deg'],
         'dist': [('cm', 'm', 'km', 'Gm', 'AU', 'lyr', 'pc'), 'km'],
         'size': [('arcsec', 'arcmin', 'deg', 'rad'), 'arcsec']
         }


def get_options(value: Any, prop: str) -> tuple:
    """
    Chooses options and default values for the given physical quantity.

    Parameters
    ----------
    value : Any
        Physical quantity.
    prop : str
        String containing the property shortcode to check against.

    Returns
    -------
    tuple
        Tuple containing the options and the default value is returned

    """
    if value is None:
        option_ = tuple()
        default_ = ''
    else:
        option_, default_ = pars_[prop]

    return option_, default_
