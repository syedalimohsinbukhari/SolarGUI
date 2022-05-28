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


def show_object(window: Union[tk.Tk, tk.Toplevel], title: str, object_class: Any):
    """
    Display the celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel]
        tk.Tk or tk.Toplevel window to build the object inside.
    title : str
        Text to display on the title of object's window.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    # make a new toplevel window
    planet_window = tk.Toplevel(master=window)
    planet_window.title(string=title)

    # adjust the geometry
    _width, _height = window.winfo_width(), window.winfo_height()
    planet_window.geometry(newGeometry=f"{_width}x{_height}")

    # do not let the window be smaller from its original size.
    planet_window.minsize(width=_width, height=_height)

    # adjust the columns in window's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(6)]

    # heading labels
    tk_f.label_placement(window=planet_window, text="Physical parameters", row=0,
                         column=0, pad_y=5, sticky="e")
    tk_f.label_placement(window=planet_window, text="Values", row=0, column=1, pad_y=5)
    tk_f.label_placement(window=planet_window, text="Unit space", row=0, column=2,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text="Reset", row=0, column=3, pad_y=5)

    tk_f.place_object_properties(window=planet_window, text="Age", value=object_class.age,
                                 function=convert, options=("s", "yr", "Myr", "Gyr"),
                                 row=1, default="Gyr")

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text="Equivalences",
                       function=lambda: tk_f.place_equivalencies(window=planet_window,
                                                                 cel_object=object_class),
                       row=0, column=4, sticky="nsew")

    # placing the details of celestial objects one by one
    tk_f.place_object_properties(window=planet_window, text="Mass",
                                 value=object_class.mass, function=convert,
                                 options=("g", "kg", "M_earth", "M_jupiter", "M_sun"),
                                 row=2, default="kg")

    tk_f.place_object_properties(window=planet_window, text="Radius",
                                 value=object_class.radius, function=convert,
                                 options=("cm", "m", "km", "R_earth", "R_jupiter",
                                          "R_sun"), row=3, default="km")

    tk_f.place_object_properties(window=planet_window, text="Volume",
                                 value=object_class.volume, function=convert,
                                 options=("cm^3", "m^3", "km^3"), row=4, default="km^3")

    tk_f.place_object_properties(window=planet_window, text="Density",
                                 value=object_class.density, function=convert,
                                 options=("g/cm^3", "kg/cm^3", "kg/m^3"), row=5,
                                 default="g/cm^3")

    tk_f.place_object_properties(window=planet_window, text="Surface area",
                                 value=object_class.surface_area, function=convert,
                                 options=("cm^2", "m^2", "km^2"), row=6, default="km^2")

    tk_f.place_object_properties(window=planet_window, text="Surface gravity",
                                 value=object_class.surface_gravity, function=convert,
                                 options=("cm/s^2", "m/s^2", "km/s^2"), row=7,
                                 default="m/s^2")
