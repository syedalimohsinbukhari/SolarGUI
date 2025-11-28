"""
Created on May 24 22:08:46 2022

Tkinter utility functions for the SolarGUI application.

This module provides helper functions for creating and styling tkinter widgets
including buttons, labels, entries, dropdowns, and radio buttons.
"""

import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Tuple, Union

import numpy as np
from astropy.units.quantity import Quantity

from . import moons, others, planets, stars

# Modern color scheme (shared with solar_gui.py)
COLORS = {
    'bg_dark': '#1a1a2e',
    'bg_medium': '#16213e',
    'bg_light': '#0f3460',
    'accent': '#e94560',
    'text_light': '#eaeaea',
    'text_muted': '#a0a0a0',
    'button_bg': '#0f3460',
    'button_hover': '#e94560',
    'entry_bg': '#1a1a2e',
}


def object_button(window, function, text, row=1, column=0, sticky='news', width=None):
    """
    Create and display a styled button for a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget to build the button inside.
    function : Callable
        Callback function to execute on button click.
    text : str
        Text to display on the button.
    row : int, optional
        Grid row position. Default is 1.
    column : int, optional
        Grid column position. Default is 0.
    sticky : str, optional
        Grid sticky alignment. Default is 'news'.
    width : int, optional
        Button width in characters. Default is None.

    Returns
    -------
    tk.Button
        The created button widget.

    """
    btn = tk.Button(
        master=window,
        text=text,
        command=function,
        width=width,
        font=('Helvetica', 9),
        bg=COLORS['button_bg'],
        fg=COLORS['text_light'],
        activebackground=COLORS['button_hover'],
        activeforeground=COLORS['text_light'],
        relief=tk.FLAT,
        cursor='hand2'
    )
    btn.grid(row=row, column=column, sticky=sticky, padx=5, pady=3)

    # Add hover effects
    btn.bind('<Enter>', lambda e: btn.configure(bg=COLORS['button_hover']))
    btn.bind('<Leave>', lambda e: btn.configure(bg=COLORS['button_bg']))

    return btn


def place_object_properties(window, function, text, value, row, column, options, default):
    """
    Create a property row with label, entry, dropdown, and reset button.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget to build the controls inside.
    function : Callable
        Unit conversion function to apply on selection change.
    text : str
        Property name label text.
    value : str
        Initial value for the entry widget.
    row : int
        Grid row position.
    column : int
        Starting grid column position.
    options : Tuple
        Unit options for the dropdown menu.
    default : str
        Default unit to reset to.

    Returns
    -------
    None

    """
    # Configure column weights
    for i in range(6):
        window.grid_columnconfigure(index=i, weight=1)

    # Create widgets
    label_placement(window=window, text=text, row=row, column=column, sticky='e')
    val_entry = entry_placement(window=window, value=value, row=row, columns=column + 1, width=30)

    def value_set(change_to, reset=False):
        """
        Update the entry value based on dropdown selection.

        Parameters
        ----------
        change_to : Union[tk.Event, str]
            Unit to convert to, or event from dropdown selection.
        reset : bool, optional
            Whether to reset the dropdown to empty. Default is False.

        """
        if not isinstance(change_to, str):
            change_to = change_to.widget.get()

        if reset:
            dropdown.set('')

        change_value(entry=val_entry, value=value, change_to=change_to, function=function)

    get_var = tk.StringVar()
    state = 'disabled' if default == '' else 'readonly'

    dropdown = ttk.Combobox(
        master=window,
        textvariable=get_var,
        values=options,
        state=state,
        font=('Helvetica', 9)
    )
    dropdown.bind('<<ComboboxSelected>>', value_set)
    dropdown.grid(row=row, column=column + 2, padx=5, sticky='news')

    # Reset button
    btn_state = 'disabled' if default == '' else 'normal'
    reset_button = tk.Button(
        master=window,
        text='Reset',
        state=btn_state,
        command=lambda: value_set(change_to=default, reset=True),
        font=('Helvetica', 8),
        bg=COLORS['button_bg'],
        fg=COLORS['text_light'],
        activebackground=COLORS['button_hover'],
        activeforeground=COLORS['text_light'],
        relief=tk.FLAT
    )
    reset_button.grid(row=row, column=column + 3, padx=5, sticky='news')


def label_placement(window, text, row, column=0, columnspan=None, pad_y=None, sticky='news'):
    """
    Create and place a styled label widget.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget to place the label inside.
    text : str
        Label text to display.
    row : int
        Grid row position.
    column : int, optional
        Grid column position. Default is 0.
    columnspan : int, optional
        Number of columns to span. Default is None.
    pad_y : int, optional
        Vertical padding. Default is None.
    sticky : str, optional
        Grid sticky alignment. Default is 'news'.

    Returns
    -------
    tk.Label
        The created label widget.

    """
    label = tk.Label(
        master=window,
        text=text,
        font=('Helvetica', 9),
        bg=COLORS['bg_medium'],
        fg=COLORS['text_light']
    )
    label.grid(
        row=int(row),
        column=int(column),
        padx=5,
        pady=pad_y,
        sticky=sticky,
        columnspan=columnspan
    )
    return label


def entry_placement(window, value, row, columns, width=None):
    """
    Create and place a styled entry widget.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget to place the entry inside.
    value : str
        Initial value to display in the entry.
    row : int
        Grid row position.
    columns : int
        Grid column position.
    width : int, optional
        Entry widget width. Default is None.

    Returns
    -------
    tk.Entry
        The created entry widget.

    """
    entry_widget = tk.Entry(
        master=window,
        width=width,
        font=('Helvetica', 9),
        bg=COLORS['entry_bg'],
        fg=COLORS['text_light'],
        insertbackground=COLORS['text_light'],
        relief=tk.FLAT,
        highlightthickness=1,
        highlightbackground=COLORS['bg_light'],
        highlightcolor=COLORS['accent']
    )
    entry_widget.insert(index=0, string=str(value))
    entry_widget.grid(row=int(row), column=int(columns), padx=5, sticky='news')

    return entry_widget


def place_equivalencies(window, cel_object, equiv_type, column):
    """
    Create an equivalencies selection window for celestial object comparisons.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for reference.
    cel_object : Callable
        Celestial object class for equivalency calculations.
    equiv_type : str
        Type of equivalencies: 'physical', 'orbital', or 'observation'.
    column : int
        Column position for displaying equivalencies.

    Returns
    -------
    None

    """
    parent_window = window
    _w, _h = 350, 150

    equiv_window = tk.Toplevel(master=window)
    equiv_window.geometry(newGeometry='{}x{}'.format(_w, _h))
    equiv_window.title(string='Equivalencies')
    equiv_window.configure(bg=COLORS['bg_medium'])

    get_val = tk.StringVar()

    # Define equivalency options with their states
    equiv_options = [
        # Row 0
        [
            ('Sun', stars.Sun, 'disabled' if equiv_type in ['orbital'] else 'active'),
            ('Mercury', planets.Mercury, 'active'),
            ('Venus', planets.Venus, 'active'),
            ('Earth', planets.Earth, 'disabled' if equiv_type == 'observation' else 'active'),
        ],
        # Row 1
        [
            ('Moon', moons.Moon, 'disabled' if equiv_type in ['orbital', 'observation'] else 'active'),
            ('Mars', planets.Mars, 'active'),
            ('Jupiter', planets.Jupiter, 'active'),
            ('Saturn', planets.Saturn, 'active'),
        ],
        # Row 2
        [
            ('Uranus', planets.Uranus, 'active'),
            ('Neptune', planets.Neptune, 'active'),
            ('Pluto', others.Pluto, 'active'),
        ],
    ]

    for row_idx, row_options in enumerate(equiv_options):
        for col_idx, (name, obj_class, state) in enumerate(row_options):
            equiv_radio_buttons(
                window=equiv_window,
                function=lambda p=parent_window, o=cel_object, s=obj_class, l=name: comparison(
                    c_win=p, primary_obj=o, sec_obj=s, sec_lbl=l,
                    comparison_type=equiv_type, column=column
                ),
                text=name,
                value=name,
                radio_val=get_val,
                row=row_idx,
                column=col_idx,
                state=state
            )

    # Reset button
    reset_button = tk.Button(
        master=equiv_window,
        text='Reset',
        command=lambda: comparison(
            c_win=parent_window, primary_obj=cel_object, sec_obj=others.Pluto,
            sec_lbl='Reset', comparison_type=equiv_type, column=column, reset=True
        ),
        font=('Helvetica', 9),
        bg=COLORS['button_bg'],
        fg=COLORS['text_light'],
        activebackground=COLORS['button_hover'],
        activeforeground=COLORS['text_light'],
        relief=tk.FLAT
    )
    reset_button.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky='news')

    # Configure grid weights
    for i in range(5):
        equiv_window.grid_columnconfigure(index=i, weight=1)
        equiv_window.grid_rowconfigure(index=i, weight=1)


def equiv_radio_buttons(window, function, text, value, radio_val, row, column, state='normal'):
    """
    Create a styled radio button for equivalency selection.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for the radio button.
    function : Callable
        Callback function on selection.
    text : str
        Label text for the radio button.
    value : str
        Value assigned to the radio button.
    radio_val : tk.StringVar
        Variable to store the selected value.
    row : int
        Grid row position.
    column : int
        Grid column position.
    state : str, optional
        Button state ('normal', 'disabled', 'active'). Default is 'normal'.

    Returns
    -------
    tk.Radiobutton
        The created radio button widget.

    """
    rb = tk.Radiobutton(
        master=window,
        text=text,
        value=value,
        variable=radio_val,
        state=state,
        command=function,
        font=('Helvetica', 9),
        bg=COLORS['bg_medium'],
        fg=COLORS['text_light'],
        activebackground=COLORS['bg_medium'],
        activeforeground=COLORS['accent'],
        selectcolor=COLORS['bg_dark'],
        highlightthickness=0
    )
    rb.grid(row=row, column=column, sticky='w', padx=5, pady=2)
    return rb


def change_value(entry, value, change_to, function):
    """
    Update an entry widget with a converted value.

    Parameters
    ----------
    entry : tk.Entry
        Entry widget to update.
    value : Union[Quantity, str]
        Original value to convert.
    change_to : str
        Target unit for conversion.
    function : Callable
        Conversion function to apply.

    Returns
    -------
    None

    """
    entry.delete(first=0, last='end')
    entry.insert(index=0, string=function(parameter=value, change_to=change_to))


# def image_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str, row: int,
#                     column: int = 0, wraplength: int = 1550, justify: str = tk.CENTER,
#                     sticky: str = 'news'):
#     """
#     Places images and their descriptions in one of tk.Tk, tk.Toplevel, or tk.Frame
#
#     Parameters
#     ----------
#     window : Union[tk.Tk, tk.Toplevel, tk.Frame]
#         tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
#     text : str
#         Text to display with the image.
#     row : int
#         The row number to place the image in a tkinter widget.
#     column : int, optional
#         The column number to place the image in a tkinter widget. The default is 0.
#     wraplength : int, optional
#         Length after which the text is to be wrapped. The default is 1550.
#     justify : str, optional
#         Justification of text placement in the tkinter widget. The default is tk.CENTER.
#     sticky : str, optional
#         Alignment of the text within the label. The default is 'news'.
#
#     Returns
#     -------
#     None.
#
#     """
#     tk.Label(master=window, text=text, wraplength=wraplength,
#              justify=justify).grid(row=row, column=column, sticky=sticky)


def comparison(c_win, primary_obj, sec_obj, sec_lbl, comparison_type, column, reset=False):
    """
    Compare celestial object attributes and display equivalencies.

    Parameters
    ----------
    c_win : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for displaying results.
    primary_obj : Any
        Primary celestial object for comparison.
    sec_obj : Any
        Secondary celestial object to compare against.
    sec_lbl : str
        Label for the comparison object.
    comparison_type : str
        Type of comparison: 'physical', 'orbital', or 'observation'.
    column : int
        Column position for displaying results.
    reset : bool, optional
        Whether to reset values to empty. Default is False.

    Returns
    -------
    None

    """
    attributes = primary_obj.__dict__.keys()
    num_attributes = len(attributes)

    # Get the appropriate parameter class from the secondary object
    if comparison_type == 'physical':
        sec_obj = sec_obj.PhysicalParameters()
    elif comparison_type == 'orbital':
        sec_obj = sec_obj.OrbitalParameters()
    else:
        sec_obj = sec_obj.ObservationalParameters()

    # Calculate ratios
    out = []
    for attr in attributes:
        if primary_obj.__getattribute__(attr) is None:
            ratio = None
        elif attr in ['apparent_magnitude', 'absolute_magnitude']:
            ratio = sec_obj.__getattribute__(attr)
            ratio -= primary_obj.__getattribute__(attr)
            ratio = 100 ** (ratio / 5)
        else:
            ratio = primary_obj.__getattribute__(attr) / sec_obj.__getattribute__(attr)
        out.append(ratio)

    # Display results
    for value, num in zip(out, range(1, num_attributes + 1)):
        if value is None:
            formatted_value = None
        elif 0 < value <= 0.001:
            formatted_value = '{:.5e} \xd7 {}'.format(abs(value), sec_lbl)
        elif value > int(1e9):
            formatted_value = '{:.5E} \xd7 {}'.format(np.round(abs(value), 9), sec_lbl)
        else:
            formatted_value = '{} \xd7 {}'.format(np.round(abs(value), 9), sec_lbl)

        formatted_value = formatted_value if not reset else ''
        entry_placement(window=c_win, value=formatted_value, row=num, columns=column, width=25)
