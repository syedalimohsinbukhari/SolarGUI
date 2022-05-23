"""
Created on May 23 09:05:42 2022
"""

import tkinter as tk

from earth import Earth

earth_ = Earth()


def show_earth(window):
    earth_window = tk.Toplevel(window)
    earth_window.title('Earth')

    _f_w, _f_h = window.winfo_width(), window.winfo_height()
    earth_window.geometry(f'{_f_w}x{_f_h}')

    mass_value(earth_window)
    radius_value(earth_window)
    surface_area_value(earth_window)


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


def surface_area_value(earth_window):

    def change_surface_area_value():
        surface_area_entry.delete(0, 'end')
        if get_value.get() == 'km2':
            surface_area_entry.insert(0, earth_.surface_area)
        elif get_value.get() == 'm2':
            surface_area_entry.insert(0, earth_.convert_surface_area('m2'))
        elif get_value.get() == 'Rsun2':
            surface_area_entry.insert(0, earth_.convert_surface_area('Rsun2'))

    label_placement(window=earth_window,
                    text='Surface area of Earth',
                    row=3)

    surface_area_entry = entry_placement(window=earth_window,
                                         value=earth_.surface_area,
                                         row=3)

    get_value = tk.StringVar()

    surface_area_radio_button = {'m^2': ['m2', 2],
                                 'km^2': ['km2', 3],
                                 'Rsun^2': ['Rsun2', 4]}

    align_radio_buttons(window=earth_window,
                        string_var=get_value,
                        radio_button_dict=surface_area_radio_button,
                        function=change_surface_area_value,
                        row=3)


def radius_value(earth_window):

    def change_radius_value():
        radius_entry.delete(0, 'end')
        if get_value.get() == 'm':
            radius_entry.insert(0, earth_.radius)
        elif get_value.get() == 'km':
            radius_entry.insert(0, earth_.convert_radius('km'))
        elif get_value.get() == 'Rsun':
            radius_entry.insert(0, earth_.convert_radius('Rsun'))

    label_placement(window=earth_window,
                    text='Radius of Earth',
                    row=1)

    radius_entry = entry_placement(window=earth_window,
                                   value=earth_.radius,
                                   row=1)

    get_value = tk.StringVar()

    radius_radio_button = {'m': ['m', 2],
                           'km': ['km', 3],
                           'Rsun': ['Rsun', 4]}

    align_radio_buttons(window=earth_window,
                        string_var=get_value,
                        radio_button_dict=radius_radio_button,
                        function=change_radius_value,
                        row=1)


def mass_value(earth_window):

    def change_mass_value():
        mass_entry.delete(0, 'end')
        if get_value.get() == 'kg':
            mass_entry.insert(0, earth_.mass)
        elif get_value.get() == 'Msun':
            mass_entry.insert(0, earth_.convert_mass('Msun'))

    label_placement(window=earth_window,
                    text='Mass of Earth',
                    row=0)

    mass_entry = entry_placement(window=earth_window,
                                 value=earth_.mass,
                                 row=0)

    get_value = tk.StringVar()

    mass_radio_button = {'kg': ['kg', 2],
                         'Msun': ['Msun', 3]}

    align_radio_buttons(window=earth_window,
                        string_var=get_value,
                        radio_button_dict=mass_radio_button,
                        function=change_mass_value,
                        row=0)
