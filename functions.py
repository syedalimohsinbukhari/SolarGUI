"""
Created on May 23 09:05:42 2022
"""

import tkinter as tk

from earth import Earth

_earth = Earth()


def show_earth(window):
    earth_window = tk.Toplevel(window)
    earth_window.title('Earth')

    _f_w, _f_h = window.winfo_width(), window.winfo_height()
    earth_window.geometry(f'{_f_w}x{_f_h}')

    _dict = Dictionaries()

    property_value(window=earth_window, text='Mass of Earth', row=0, value=_earth.mass,
                   radio_dict=_dict.mass, function=_earth.convert_mass)

    property_value(window=earth_window, text='Radius of Earth', row=1,
                   value=_earth.radius, radio_dict=_dict.radius,
                   function=_earth.convert_radius)

    property_value(window=earth_window, text='Surface area of Earth', row=2,
                   value=_earth.surface_area, radio_dict=_dict.surface_area,
                   function=_earth.convert_surface_area)


class Dictionaries:
    mass = {'g': ['g', 2],
            'kg': ['kg', 3],
            'Msun': ['Msun', 4]}

    radius = {'cm': ['cm', 2],
              'm': ['m', 3],
              'km': ['km', 4],
              'Rsun': ['Rsun', 5]}

    surface_area = {'cm^2': ['cm2', 2],
                    'm^2': ['m2', 3],
                    'km^2': ['km2', 4],
                    'Rsun^2': ['Rsun2', 5]}


def align_radio_buttons(window, string_var, radio_button_dict, function, row):
    for (text, value) in radio_button_dict.items():
        tk.Radiobutton(master=window,
                       text=text,
                       variable=string_var,
                       value=value[0],
                       command=lambda: function()).grid(row=row,
                                                        column=value[1],
                                                        padx=5,
                                                        sticky='w')


def label_placement(window, text, row):
    mass_label = tk.Label(master=window, text=text)
    mass_label.grid(row=row, column=0, padx=10, sticky='w')


def entry_placement(window, value, row):
    entry_widget = tk.Entry(master=window, width=30)
    entry_widget.insert(0, f'{value}')
    entry_widget.grid(row=row, column=1, padx=10, sticky='w')

    return entry_widget


def alter_value(entry, function, change_to):
    entry.delete(0, 'end')
    entry.insert(0, function(change_to=change_to))


def property_value(window, text, row, value, radio_dict, function):
    label_placement(window=window, text=text, row=row)

    entry = entry_placement(window=window, value=value, row=row)

    get_value = tk.StringVar()

    align_radio_buttons(window=window,
                        string_var=get_value,
                        radio_button_dict=radio_dict,
                        function=lambda: alter_value(entry=entry,
                                                     function=function,
                                                     change_to=get_value.get()),
                        row=row)
