"""
Created on May 23 09:05:42 2022
"""

import tkinter as tk

from planets.earth import Earth
from tk_functions import label_placement, place_dropdown_menu

_earth = Earth()


def show_earth(window):
    earth_window = tk.Toplevel(window)
    earth_window.title('Earth')

    _f_w, _f_h = window.winfo_width(), window.winfo_height()
    earth_window.geometry(f'{_f_w}x{_f_h}')

    label_placement(window=earth_window, text='', row=0, pad_y=0.01)

    place_dropdown_menu(window=earth_window, text='Age', value=_earth.age,
                        function=_earth.convert_age, row=1,
                        options=['s', 'yr', 'Myr', 'Gyr'], default='Gyr')

    place_dropdown_menu(window=earth_window, text='Mass', value=_earth.mass,
                        function=_earth.convert_mass, row=2,
                        options=['g', 'kg', 'M_jupiter', 'M_sun'], default='kg')

    place_dropdown_menu(window=earth_window, text='Radius', value=_earth.radius,
                        function=_earth.convert_radius, row=3,
                        options=['cm', 'm', 'km', 'R_jupiter', 'R_sun'], default='km')

    place_dropdown_menu(window=earth_window, text='Volume', value=_earth.volume,
                        function=_earth.convert_volume, row=4,
                        options=['cm^3', 'm^3', 'km^3', 'R_jupiter^3', 'R_sun^3'],
                        default='km^3')

    place_dropdown_menu(window=earth_window, text='Surface area',
                        value=_earth.surface_area,
                        function=_earth.convert_surface_area, row=5,
                        options=['cm^2', 'm^2', 'km^2', 'R_jupiter^2', 'R_sun^2'],
                        default='km^2')

    place_dropdown_menu(window=earth_window, text='Surface gravity',
                        value=_earth.surface_gravity,
                        function=_earth.convert_surface_gravity, row=6,
                        options=['cm/s^2', 'm/s^2', 'km/s^2', 'km/h^2', 'R_jupiter/s^2',
                                 'R_sun/s^2'], default='m/s^2')
