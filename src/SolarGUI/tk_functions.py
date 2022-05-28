"""
Created on May 24 22:08:46 2022
"""

import tkinter as tk
from tkinter import ttk

try:
    from . import celestial_objects as c_objs
    from . import utilities as utils
except ImportError:
    import celestial_objects as c_objs
    import utilities as utils


def planet_button(window, text, function, column, row=1, sticky='news'):
    tk.Button(master=window, text=text,
              command=lambda: function()).grid(row=row, column=column, sticky=sticky,
                                               padx=10, pady=5)


def place_dropdown_menu(window, text, value, function, options, row, default):
    # dropdown idea taken from https://pythonguides.com/python-tkinter-optionmenu/

    for i in range(6):
        window.grid_columnconfigure(index=i, weight=1)

    label_placement(window=window, text=text, row=row, sticky='e')
    val_entry = entry_placement(window=window, value=value, row=row, columns=1, width=30)

    def command(change_to, reset=False):
        if not isinstance(change_to, str):
            change_to = change_to.widget.get()

        # taken from https://stackoverflow.com/a/35236892/3212945
        if reset:
            dropdown.set('')

        alter_value(entry=val_entry, function=function, value=value, change_to=change_to)

    get_var = tk.StringVar()

    # taken from https://stackoverflow.com/a/68128312/3212945
    dropdown = ttk.Combobox(master=window, textvariable=get_var, values=options,
                            state='readonly')
    dropdown.bind('<<ComboboxSelected>>', command)
    dropdown.grid(row=row, column=2, padx=10, sticky='news')

    reset_button = tk.Button(master=window, text='Reset',
                             command=lambda: command(change_to=default, reset=True))
    reset_button.grid(row=row, column=3, padx=10, sticky='news')


def label_placement(window, text, row, column=0, sticky='news', pad_y=None):
    label = tk.Label(master=window, text=text)
    label.grid(row=row, column=column, padx=10, pady=pad_y, sticky=sticky)

    return label


def entry_placement(window, value, row, columns, width=None):
    entry_widget = tk.Entry(master=window, width=width)
    entry_widget.insert(index=0, string=f'{value}')
    entry_widget.grid(row=row, column=columns, padx=10, sticky='news')

    return entry_widget


def place_equivalencies(window, planet):
    parent_window = window

    _w, _h = 300, 100

    equiv_window = tk.Toplevel(master=window)
    equiv_window.geometry(newGeometry=f'{_w}x{_h}')

    equiv_window.title(string='Equivalencies')

    get_val = tk.StringVar()

    equiv_radio_buttons(window=equiv_window, text='Sun', value='Sun',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Sun(),
                                                          c_lbl='Sun'),
                        row=0, column=0, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Mercury', value='Mercury',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Mercury(),
                                                          c_lbl='Mercury'),
                        row=0, column=1, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Venus', value='Venus',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Venus(),
                                                          c_lbl='Venus'),
                        row=0, column=2, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Earth', value='Earth',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Earth(),
                                                          c_lbl='Earth'),
                        row=0, column=3, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Moon', value='Moon',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Moon(),
                                                          c_lbl='Moon'),
                        row=1, column=0, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Mars', value='Mars',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Mars(),
                                                          c_lbl='Mars'),
                        row=1, column=1, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Jupiter', value='Jupiter',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Jupiter(),
                                                          c_lbl='Jupiter'),
                        row=1, column=2, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Saturn', value='Saturn',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Saturn(),
                                                          c_lbl='Saturn'),
                        row=1, column=3, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Uranus', value='Uranus',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Uranus(),
                                                          c_lbl='Uranus'),
                        row=2, column=0, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Neptune', value='Neptune',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Neptune(),
                                                          c_lbl='Neptune'),
                        row=2, column=1, radio_val=get_val)

    equiv_radio_buttons(window=equiv_window, text='Pluto', value='Pluto',
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=planet,
                                                          c_obj=c_objs.Pluto(),
                                                          c_lbl='Pluto'),
                        row=2, column=2, radio_val=get_val)

    reset_button = tk.Button(master=equiv_window, text='Reset',
                             command=lambda: utils.comparison(c_win=parent_window,
                                                              p_ojb=planet,
                                                              c_obj=c_objs.Pluto(),
                                                              c_lbl='Reset', reset=True))
    reset_button.grid(row=3, column=0, columnspan=4, padx=10, sticky='news')

    # taken from https://stackoverflow.com/a/69416040/3212945
    for i in range(5):
        equiv_window.grid_columnconfigure(index=i, weight=1)
        equiv_window.grid_rowconfigure(index=i, weight=1)


def equiv_radio_buttons(window, text, value, radio_val, function, row, column):
    r1 = tk.Radiobutton(master=window, text=text, value=value, variable=radio_val,
                        command=function)
    r1.grid(row=row, column=column, sticky='w', padx=5)


def alter_value(entry, function, value, change_to):
    entry.delete(first=0, last='end')
    entry.insert(index=0, string=function(parameter=value, change_to=change_to))
