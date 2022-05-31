"""
Created on May 24 22:12:45 2022
"""

import tkinter as tk
from typing import Any, Union

# added try/except because pip bundle and main file do not work with same imports

try:
    from . import tk_functions as tk_f
    from .utilities import convert
except ImportError:
    import tk_functions as tk_f
    from utilities import convert


def get_parameter_selection(window, title, object_class):
    planet_window = tk.Toplevel(master=window)
    planet_window.title(string=title)

    # adjust the geometry
    _width, _height = window.winfo_width(), window.winfo_height()
    planet_window.geometry(newGeometry=f"{_width}x{_height}")

    # do not let the window be smaller from its original size.
    planet_window.minsize(width=_width, height=_height)

    # adjust the columns in window's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(7)]

    phy = tk.Button(master=planet_window, text='Physical Parameters',
                    command=lambda: show_physical_parameters(window=planet_window,
                                                             object_class=object_class))
    phy.grid(row=2, column=0)

    orb = tk.Button(master=planet_window, text='Orbital Parameters',
                    command=lambda: show_orbital_parameters(window=planet_window,
                                                            object_class=object_class))
    orb.grid(row=4, column=0)

    tba = tk.Button(master=planet_window, text='TBA')
    tba.grid(row=6, column=0)

    show_physical_parameters(window=planet_window, object_class=object_class)


def show_physical_parameters(window: Union[tk.Tk, tk.Toplevel], object_class: Any):
    """
    Display the physical parameters of the celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel]
        tk.Tk or tk.Toplevel window to build the object inside.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    object_class = object_class.PhysicalParameters()

    # make a new toplevel window
    # planet_window = tk.Toplevel(master=window)
    # planet_window.title(string=title)

    planet_window = window

    # adjust the geometry
    # _width, _height = window.winfo_width(), window.winfo_height()
    # planet_window.geometry(newGeometry=f"{_width}x{_height}")
    #
    # # do not let the window be smaller from its original size.
    # planet_window.minsize(width=_width, height=_height)
    #
    # adjust the columns in window's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(7)]

    # heading labels
    tk_f.label_placement(window=planet_window, text="Physical parameters", row=0,
                         column=2, pad_y=5, sticky="e")
    tk_f.label_placement(window=planet_window, text="Values", row=0, column=3, pad_y=5)
    tk_f.label_placement(window=planet_window, text="Unit space", row=0, column=4,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text="Reset", row=0, column=5, pad_y=5)

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text="Equivalences",
                       function=lambda: tk_f.place_physical_equivalencies(
                               window=planet_window, cel_object=object_class, column=7),
                       row=0, column=6, sticky="nsew")

    # placing the details of celestial objects one by one
    tk_f.place_object_properties(window=planet_window, text="Age",
                                 value=object_class.age,
                                 function=convert, options=("s", "yr", "Myr", "Gyr"),
                                 row=1, column=2, default="Gyr")

    tk_f.place_object_properties(window=planet_window, text="Mass",
                                 value=object_class.mass, function=convert,
                                 options=("g", "kg", "M_earth", "M_jupiter", "M_sun"),
                                 row=2, column=2, default="kg")

    tk_f.place_object_properties(window=planet_window, text="Radius",
                                 value=object_class.radius, function=convert,
                                 options=("cm", "m", "km", "R_earth", "R_jupiter",
                                          "R_sun"), row=3, column=2, default="km")

    tk_f.place_object_properties(window=planet_window, text="Volume",
                                 value=object_class.volume, function=convert,
                                 options=("cm^3", "m^3", "km^3"), row=4, column=2,
                                 default="km^3")

    tk_f.place_object_properties(window=planet_window, text="Density",
                                 value=object_class.density, function=convert,
                                 options=("g/cm^3", "kg/cm^3", "kg/m^3"), row=5,
                                 column=2, default="g/cm^3")

    tk_f.place_object_properties(window=planet_window, text="Surface area",
                                 value=object_class.surface_area, function=convert,
                                 options=("cm^2", "m^2", "km^2"), row=6, column=2,
                                 default="km^2")

    tk_f.place_object_properties(window=planet_window, text="Surface gravity",
                                 value=object_class.surface_gravity, function=convert,
                                 options=("cm/s^2", "m/s^2", "km/s^2"), row=7, column=2,
                                 default="m/s^2")

    tk_f.place_object_properties(window=planet_window, text='Escape velocity',
                                 value=object_class.escape_velocity, function=convert,
                                 options=('cm/s', 'm/s', 'km/s', 'km/h'), row=8,
                                 column=2, default='km/s')


def show_orbital_parameters(window: Union[tk.Tk, tk.Toplevel],
                            object_class: Any):
    """
    Display the orbital parameters of the celestial object.
    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel]
        tk.Tk or tk.Toplevel window to build the object inside.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    object_class = object_class.OrbitalParameters()

    # make a new toplevel window
    planet_window = window
    # planet_window = tk.Toplevel(master=window)
    # planet_window.title(string=title)
    #
    # # adjust the geometry
    # _width, _height = window.winfo_width(), window.winfo_height()
    # planet_window.geometry(newGeometry=f"{_width}x{_height}")
    #
    # # do not let the window be smaller from its original size.
    # planet_window.minsize(width=_width, height=_height)
    #
    # # adjust the columns in window's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(6)]

    # heading labels
    tk_f.label_placement(window=planet_window, text="Orbital parameters", row=0,
                         column=2, pad_y=5, sticky="e")
    tk_f.label_placement(window=planet_window, text="Values", row=0, column=3,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text="Unit space", row=0, column=4,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text="Reset", row=0, column=5, pad_y=5)

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text="Equivalences",
                       function=lambda: tk_f.place_physical_equivalencies(
                               window=planet_window, cel_object=object_class, column=6),
                       row=0, column=4, sticky="nsew")

    # placing the details of celestial objects one by one
    tk_f.place_object_properties(window=planet_window, text='Semi Major Axis',
                                 value=object_class.semi_major_axis,
                                 function=convert, options=('cm', 'm', 'km', 'AU',
                                                            'pc'),
                                 row=1, default='AU', column=2)

    tk_f.place_object_properties(window=planet_window, text='Closest approach',
                                 value=object_class.apo, function=convert,
                                 options=('cm', 'm', 'km', 'AU', 'pc'), row=2,
                                 default='AU', column=2)

    tk_f.place_object_properties(window=planet_window, text='Farthest approach',
                                 value=object_class.peri, function=convert,
                                 options=('cm', 'm', 'km', 'AU', 'pc'), row=3,
                                 default='AU', column=2)

    tk_f.place_object_properties(window=planet_window, text='Eccentricity',
                                 value=object_class.eccentricity,
                                 function=convert, options=('', ''),
                                 row=4, default='', column=2)

    tk_f.place_object_properties(window=planet_window, text='Orbital Period',
                                 value=object_class.orbital_period,
                                 function=convert, options=('s', 'y', 'day', 'Myr'),
                                 row=5, default='day', column=2)

    tk_f.place_object_properties(window=planet_window, text='Av. Orbital Speed',
                                 value=object_class.av_orbital_speed,
                                 function=convert,
                                 options=('cm/s', 'm/s', 'km/s', 'km/h'), row=6,
                                 default='km/s', column=2)

    tk_f.place_object_properties(window=planet_window, text='Mean anomaly',
                                 value=object_class.mean_anomaly, function=convert,
                                 options=('deg', 'rad'), row=7, default='deg', column=2)

    tk_f.place_object_properties(window=planet_window, text='Inclination',
                                 value=object_class.inclination, function=convert,
                                 options=('deg', 'rad'), row=8, default='deg', column=2)

    tk_f.place_object_properties(window=planet_window, text='Longitude of Asc. node',
                                 value=object_class.longitude_of_ascending_node,
                                 function=convert, options=('deg', 'rad'), row=9,
                                 default='deg', column=2)

    tk_f.place_object_properties(window=planet_window, text='Argument of peri.',
                                 value=object_class.argument_of_perihelion,
                                 function=convert, options=('deg', 'rad'), row=10,
                                 default='deg', column=2)

    tk_f.place_object_properties(window=planet_window, text='Axial Tilt',
                                 value=object_class.axial_tilt, function=convert,
                                 options=('deg', 'rad'), row=11, default='deg', column=2)
