"""
Created on May 24 22:12:45 2022
"""

import tkinter as tk

from . import tk_functions as tk_f


def show_planet(window, text, planet_class):
    planet_window = tk.Toplevel(window)
    planet_window.title(text)

    _f_w, _f_h = window.winfo_width(), window.winfo_height()
    planet_window.geometry(f'{_f_w}x{_f_h}')

    tk_f.label_placement(window=planet_window, text='', row=0, pad_y=0.01)

    tk_f.place_dropdown_menu(window=planet_window, text='Age', value=planet_class.age,
                             function=planet_class.convert_age, row=1,
                             options=['s', 'yr', 'Myr', 'Gyr'], default='Gyr')

    tk_f.place_dropdown_menu(window=planet_window, text='Mass', value=planet_class.mass,
                             function=planet_class.convert_mass, row=2,
                             options=['g', 'kg', 'M_earth', 'M_jupiter', 'M_sun'],
                             default='kg')

    tk_f.place_dropdown_menu(window=planet_window, text='Radius',
                             value=planet_class.radius,
                             function=planet_class.convert_radius, row=3,
                             options=['cm', 'm', 'km', 'R_earth', 'R_jupiter', 'R_sun'],
                             default='km')

    tk_f.place_dropdown_menu(window=planet_window, text='Volume',
                             value=planet_class.volume,
                             function=planet_class.convert_volume, row=4,
                             options=['cm^3', 'm^3', 'km^3', 'R_earth^3', 'R_jupiter^3',
                                      'R_sun^3'], default='km^3')

    tk_f.place_dropdown_menu(window=planet_window, text='Density',
                             value=planet_class.density,
                             function=planet_class.convert_density, row=5,
                             options=['g/cm^3', 'kg/cm^3', 'kg/m^3', 'kg/km^3',
                                      'M_jupiter/km^3', 'M_sun/km^3'], default='g/cm^3')

    tk_f.place_dropdown_menu(window=planet_window, text='Surface area',
                             value=planet_class.surface_area,
                             function=planet_class.convert_surface_area, row=6,
                             options=['cm^2', 'm^2', 'km^2', 'R_earth^2', 'R_jupiter^2',
                                      'R_sun^2'], default='km^2')

    tk_f.place_dropdown_menu(window=planet_window, text='Surface gravity',
                             value=planet_class.surface_gravity,
                             function=planet_class.convert_surface_gravity, row=7,
                             options=['cm/s^2', 'm/s^2', 'km/s^2', 'km/h^2',
                                      'R_earth/s^2', 'R_jupiter/s^2', 'R_sun/s^2'],
                             default='m/s^2')
