"""
Created on May 23 09:05:42 2022
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable

from earth import Earth

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


def place_dropdown_menu(window, text, value, function, row, options, default):

    def command(change_to, reset=False):
        if not isinstance(change_to, str):
            change_to = change_to.widget.get()

        # taken from https://stackoverflow.com/a/35236892/3212945
        if reset:
            dropdown.set('')

        alter_value(entry=age_, function=function, change_to=change_to)

    # dropdown idea taken from https://pythonguides.com/python-tkinter-optionmenu/
    label_placement(window=window, text=text, row=row)
    age_ = entry_placement(window=window, row=row, value=value)

    get_var = tk.StringVar()

    # taken from https://stackoverflow.com/a/68128312/3212945
    dropdown = ttk.Combobox(master=window, textvariable=get_var, values=options,
                            state='readonly')
    dropdown.bind('<<ComboboxSelected>>', command)
    dropdown.grid(row=row, column=2, padx=10, sticky='w')

    reset_button = tk.Button(master=window, text='Reset',
                             command=lambda: command(change_to=default, reset=True))
    reset_button.grid(row=row, column=3, padx=10, sticky='w')


def label_placement(window, text, row, pad_y=None):
    mass_label = tk.Label(master=window, text=text)
    mass_label.grid(row=row, column=0, padx=10, pady=pad_y, sticky='w')


def entry_placement(window, value, row):
    entry_widget = tk.Entry(master=window, width=40)
    entry_widget.insert(index=0, string=f'{value}')
    entry_widget.grid(row=row, column=1, padx=10, sticky='w')

    return entry_widget


def alter_value(entry: tk.Entry, function: Callable, change_to: str) -> None:
    """
    Change the value in a tkinter.Entry widget

    Parameters
    ----------
    entry: tk.Entry
        The entry widget variable.
    function: Callable
        Function to apply in the entry widget.
    change_to: str
        String containing the argument to which the unit is to be changed.
    """

    entry.delete(first=0, last='end')
    entry.insert(index=0, string=function(change_to=change_to))
