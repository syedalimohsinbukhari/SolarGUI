"""
Created on May 26 01:47:13 2022
"""

import tkinter as tk
from typing import Any, Union

import numpy as np
from astropy import units as u
from astropy.constants import codata2018 as c_2018
from astropy.units.quantity import Quantity

try:
    from . import tk_functions as tk_f
except ImportError:
    import tk_functions as tk_f

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


class GetObservationalParameters:
    """
    Class to determine the observational parameters for the celestial object.
    """

    def __init__(self, angular_size: tuple, apparent_magnitude: N_float,
                 distance: Quantity):
        """
        Initialization function for GetObservationalParameters class

        Parameters
        ----------
        angular_size: tuple
            A pair of angular sizes for calculation of average angular size for the
            celestial object.
        apparent_magnitude : N_float
            Apparent magnitude of the celestial object.
        distance : Quantity
            Distance between Earth and the celestial object.

        Returns
        ----------
        None.

        """
        self.angular_size = angular_size
        self.apparent_magnitude = apparent_magnitude
        self.distance = distance

    def get_average_angular_size(self) -> Quantity:
        """
        Calculates the average angular size for the celestial object.

        Returns
        -------
        Quantity:
            Average angular size of the celestial object.

        """
        ang_min, ang_max = [i.si.value for i in self.angular_size]
        return (np.mean([ang_min, ang_max]) * u.rad).to('arcsec')

    def get_absolute_magnitude(self):
        """
        Calculates the absolute magnitude for the celestial object.

        Returns
        -------
        float:
            Absolute magnitude of the celestial object.

        """
        distance = self.distance.to('pc')
        return self.apparent_magnitude - 5 * np.log10(distance.value) + 5

    def get(self):
        """
        Get the values for average angular size and absolute magnitude for the
        celestial object.

        """
        return self.get_absolute_magnitude(), self.get_average_angular_size()


class GetOrbitalParameters:
    """
    Class to determine the orbital parameters for the celestial objects.
    """

    def __init__(self, a_0: Quantity, ecc: float):
        """
        Initialization function for GetOrbitalParameter class

        Parameters
        ----------
        a_0 : Quantity
            Semi-major axis of the celestial object.
        ecc : float
            Eccentricity of the celestial object.

        Returns
        -------
        None.

        """
        self.semi_major_axis = a_0
        self.eccentricity = ecc

    def get_apo_distance(self) -> Quantity:
        """
        Calculates the farthest approach of a celestial object in orbit.

        Returns
        -------
        Quantity
            Apo-distance of a celestial object.

        """
        return self.semi_major_axis * (1 - self.eccentricity)

    def get_peri_distance(self) -> Quantity:
        """
        Calculates the closest approach of a celestial object in orbit.

        Returns
        -------
        Quantity
            Peri-distance of a celestial object.

        """
        return self.semi_major_axis * (1 + self.eccentricity)

    def get(self):
        """
        Get the values of apo and peri distances for the celestial objects.

        """
        return self.get_apo_distance(), self.get_peri_distance()


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

    def volume(self):
        """
        Calculate the volume of the celestial object assuming the object in spherical.

        Returns
        -------
        Quantity
            Volume of the celestial object.

        """
        return (4 / 3) * np.pi * self.radius**3

    def density(self):
        """
        Calculate the mass density of the celestial object.

        Returns
        -------
        Quantity
            Density of the celestial object.

        """
        return (self.mass / self.volume()).to('g/cm^3')

    def surface_area(self):
        """
        Calculate the surface area of the celestial object.

        Returns
        -------
        Quantity
            Surface are of the celestial object.

        """
        return 4 * np.pi * self.radius**2

    def surface_gravity(self):
        """
        Calculate the surface gravity of the celestial object.

        Returns
        -------
        Quantity
            Surface gravity of the celestial object.

        """
        return (c_2018.G * (self.mass / self.radius**2)).si

    def escape_velocity(self):
        """
        Calculate the escape velocity of the celestial object.

        Returns
        -------
        Quantity
            Escape velocity of the celestial object.

        """
        return (np.sqrt(2 * c_2018.G * self.mass * self.radius**-1)).to('km/s')

    def get(self):
        """
        Get the values of volume, density, surface area, and surface gravity of the
        celestial object.

        """
        return (self.volume(), self.density(), self.surface_area(),
                self.surface_gravity(), self.escape_velocity())


def comparison(c_win: Union[tk.Tk, tk.Toplevel, tk.Frame], primary_obj: Any, sec_obj: Any,
               sec_lbl: str, comparison_type: str, column: float, reset: bool = False):
    """
    Compares the attributes of given celestial object (o_obj) with comparison celestial
    object (c_obj).

    Parameters
    ----------
    c_win : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    primary_obj : Any
        The object clas to which the comparison is being done.
    sec_obj : Any
        The object class with which the comparison is being done.
    sec_lbl : str
        Text representing the comparison celestial object.
    comparison_type: str
        Whether the comparison should be of physical, orbital or observational parameters.
    column: float
        Specify the column number where the equivalencies should be placed.
    reset : bool, optional
        Option to set the comparison entries to null. The default is False.

    Returns
    -------
    None.

    """
    # get all the class attributes
    attributes = primary_obj.__dict__.keys()
    # get their number
    num_attributes = len(attributes)

    if comparison_type == 'physical':
        sec_obj = sec_obj.PhysicalParameters()
    elif comparison_type == 'orbital':
        sec_obj = sec_obj.OrbitalParameters()
    else:
        sec_obj = sec_obj.ObservationalParameters()

    # divide the celestial object attribute values to that of comparison celestial
    # object attributes

    out = []
    for attr in attributes:
        ratio = primary_obj.__getattribute__(attr) / sec_obj.__getattribute__(attr)
        if attr in ['apparent_magnitude', 'absolute_magnitude']:
            ratio = sec_obj.__getattribute__(attr) - primary_obj.__getattribute__(attr)
            ratio = 100**(ratio / 5)
        out.append(ratio)

    # place the entries on the comparison window or reset them
    for value, num in zip(out, range(1, num_attributes + 1)):
        if 0 < value <= 0.001:
            value = f'{abs(value):.5e} × {sec_lbl}'
        elif value > int(1e9):
            value = f'{np.round(abs(value), 5):.3E} × {sec_lbl}'
        else:
            value = f'{np.round(abs(value), 5)} × {sec_lbl}'

        value = value if not reset else ''

        tk_f.entry_placement(window=c_win, value=value, row=num, columns=column, width=25)


def Q(value: float, unit: str) -> Quantity:
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
