"""
Created on May 24 22:12:45 2022
"""

import tkinter as tk

# added try/except because pip bundle and main file do not work with same imports
try:
    from . import tk_functions as tk_f
    from .utilities import convert
    from . import celestial_objects as c_objs
except ImportError:
    import tk_functions as tk_f
    from utilities import convert
    import celestial_objects as c_objs


def show_planet(window, text, planet_class):
    planet_window = tk.Toplevel(master=window)
    planet_window.title(string=text)

    _width, _height = window.winfo_width(), window.winfo_height()
    planet_window.geometry(newGeometry=f'{_width}x{_height}')

    planet_window.minsize(width=_width, height=_height)

    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(6)]

    tk_f.label_placement(window=planet_window, text='Physical parameters', row=0,
                         column=0, pad_y=5, sticky='e')
    tk_f.label_placement(window=planet_window, text='Values', row=0, column=1, pad_y=5)
    tk_f.label_placement(window=planet_window, text='Unit space', row=0, column=2,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text='Reset', row=0, column=3, pad_y=5)

    tk_f.place_dropdown_menu(window=planet_window, text='Age', value=planet_class.age,
                             function=convert, options=['s', 'yr', 'Myr', 'Gyr'], row=1,
                             default='Gyr')

    tk_f.place_dropdown_menu(window=planet_window, text='Mass', value=planet_class.mass,
                             function=convert,
                             options=['g', 'kg', 'M_earth', 'M_jupiter', 'M_sun'], row=2,
                             default='kg')

    tk_f.place_dropdown_menu(window=planet_window, text='Radius',
                             value=planet_class.radius, function=convert,
                             options=['cm', 'm', 'km', 'R_earth', 'R_jupiter', 'R_sun'],
                             row=3, default='km')

    tk_f.place_dropdown_menu(window=planet_window, text='Volume',
                             value=planet_class.volume, function=convert,
                             options=['cm^3', 'm^3', 'km^3'], row=4, default='km^3')

    tk_f.place_dropdown_menu(window=planet_window, text='Density',
                             value=planet_class.density, function=convert,
                             options=['g/cm^3', 'kg/cm^3', 'kg/m^3'], row=5,
                             default='g/cm^3')

    tk_f.place_dropdown_menu(window=planet_window, text='Surface area',
                             value=planet_class.surface_area, function=convert,
                             options=['cm^2', 'm^2', 'km^2'], row=6, default='km^2')

    tk_f.place_dropdown_menu(window=planet_window, text='Surface gravity',
                             value=planet_class.surface_gravity, function=convert,
                             options=['cm/s^2', 'm/s^2', 'km/s^2'], row=7,
                             default='m/s^2')

    tk_f.planet_button(window=planet_window, text='Equivalences',
                       function=lambda: tk_f.place_equivalencies(window=planet_window,
                                                                 planet=planet_class),
                       column=4, row=0, sticky='nsew')
