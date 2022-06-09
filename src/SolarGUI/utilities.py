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
    from . import celestial_objects
except ImportError:
    import tk_functions as tk_f
    import celestial_objects


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


class GetOrbitalParameters:

    def __init__(self, a_0: float, ecc: float):
        self.semi_major_axis = a_0
        self.eccentricity = ecc

    def get_apo_distance(self):
        return self.semi_major_axis * (1 - self.eccentricity)

    def get_peri_distance(self):
        return self.semi_major_axis * (1 + self.eccentricity)

    def get(self):
        return self.get_apo_distance(), self.get_peri_distance()


class GetPhysicalParameters:
    """
    Class to determine the physical parameters for the celestial objects.

    """

    def __init__(self, mass: float, radius: float):
        """
        Initialization function for PhysicalParameter class.

        Parameters
        ----------
        mass : float
            Mass of the celestial object.
        radius : float
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


def comparison(c_win: Union[tk.Tk, tk.Toplevel, tk.Frame], p_ojb: Any, c_obj: Any,
               c_lbl: str, c_type: str, column: float, reset: bool = False):
    """
    Compares the attributes of given celestial object (o_obj) with comparison celestial
    object (c_obj).

    Parameters
    ----------
    c_win : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    p_ojb : Any
        The object clas to which the comparison is being done.
    c_obj : Any
        The object class with which the comparison is being done.
    c_lbl : str
        Text representing the comparison celestial object.
    c_type: str
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
    attributes = p_ojb.__dict__.keys()
    # get their number
    num_attributes = len(attributes)

    if c_type == 'physical':
        c_obj = c_obj.PhysicalParameters()
    elif c_type == 'orbital':
        c_obj = c_obj.OrbitalParameters()
    else:
        c_obj = c_obj.ObservationalParameters()

    # divide the celestial object attribute values to that of comparison celestial
    # object attributes

    try:
        out = []
        for attr in attributes:
            ratio = p_ojb.__getattribute__(attr) / c_obj.__getattribute__(attr)
            if attr in ['apparent_magnitude', 'absolute_magnitude']:
                ratio = c_obj.__getattribute__(attr) - p_ojb.__getattribute__(attr)
                ratio = 100**(ratio / 5)
            out.append(ratio)
    except (ZeroDivisionError, RuntimeWarning):
        if type(c_obj) == celestial_objects.Sun.OrbitalParameters:
            out = [1] * num_attributes

    # place the entries on the comparison window or reset them
    for value, num in zip(out, range(1, num_attributes + 1)):
        if 0 < value <= 0.001:
            value = f'{abs(value):.5e} × {c_lbl}'
        elif value > int(1e9):
            value = f'{np.round(abs(value), 5):.3E} × {c_lbl}'
        else:
            value = f'{np.round(abs(value), 5)} × {c_lbl}'

        value = value if not reset else ''

        tk_f.entry_placement(window=c_win, value=value, row=num, columns=column, width=25)


def get_av_angular_size(min_size, max_size):
    ang_min, ang_max = min_size.si.value, max_size.si.value
    return (np.mean([ang_min, ang_max]) * u.rad).to(u.arcsec)


def get_abs_mag(ap_mag, distance):
    distance = distance.to(u.pc)
    return ap_mag - 5 * np.log10(distance.value) + 5
