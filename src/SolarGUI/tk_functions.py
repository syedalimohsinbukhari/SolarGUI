"""
Created on May 24 22:08:46 2022
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Tuple, Union

from astropy.units.quantity import Quantity

try:
    from .cel__moons import Moon
    from .cel__others import Pluto
    from .cel__planets import (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus,
                               Neptune)
    from .cel__stars import Sun
    from .utilities import comparison
except ImportError:
    from cel__moons import Moon
    from cel__others import Pluto
    from cel__planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
    from cel__stars import Sun
    from utilities import comparison


def object_button(window: Union[tk.Tk, tk.Toplevel, tk.Frame], function: Callable,
                  text: str, row: int = 1, column: int = 0, sticky: str = 'news',
                  width: int = None):
    """
    Displays a button for a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    function : Callable
        A function/method to apply on click of the button.
    text : str
        Text to display on the button.
    row : int, optional
        The row number to place the object in a tkinter grid. The default is 1.
    column : int, optional
        The column number to place the object in a tkinter grid. The default is 0.
    sticky : str, optional
        Alignment of the text within the button. The default is 'news'.
    width : int, optional
        To determine teh width of the button placed.

    Returns
    -------
    None.

    """
    tk.Button(master=window, text=text,
              command=lambda: function(), width=width).grid(row=row, column=column,
                                                            sticky=sticky, padx=10,
                                                            pady=5)


def place_object_properties(window: Union[tk.Tk, tk.Toplevel, tk.Frame],
                            function: Callable, text: str, value: str, row: int,
                            column: int, options: Tuple, default: str):
    """
    Place the dropdown menu in the tkinter window grid.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    function : Callable
        A function/method to apply on selection of the dropdown item.
    text : str
        Value name for the celestial object property.
    value : str
        Value that the `get()` method will receive upon selection.
    row : int
        The row number to place the dropdown menu object in a tkinter grid.
    column: int
        The starting column number for the widget placement.
    options : Tuple
        Option tuple which will be displayed in the dropdown menu.
    default : str
        Default unit to which the value in tk.Entry will be reset to after reset button
        is pressed.

    Returns
    -------
    None.

    """
    # dropdown idea taken from https://pythonguides.com/python-tkinter-optionmenu/

    [window.grid_columnconfigure(index=i, weight=1) for i in range(6)]

    label_placement(window=window, text=text, row=row, column=column, sticky='e')
    val_entry = entry_placement(window=window, value=value, row=row, columns=column + 1,
                                width=30)

    def value_set(change_to: Union[tk.Event, str], reset: bool = False):
        """
        Sets the `tk.Entry` value to selected `change_to` variable.

        Parameters
        ----------
        change_to : Union[tk.Event, str]
            tk.Event or str dictating the unit to change into.
        reset : TYPE, bool
            Resets the tk.Entry widgets to emtpy. The default is False.

        Returns
        -------
        None.

        """
        # checking type of change_to variable
        if not isinstance(change_to, str):
            change_to = change_to.widget.get()

        # taken from https://stackoverflow.com/a/35236892/3212945
        if reset:
            dropdown.set('')

        change_value(entry=val_entry, value=value, change_to=change_to, function=function)

    get_var = tk.StringVar()

    # taken from https://stackoverflow.com/a/68128312/3212945
    state = 'disabled' if default == '' else 'readonly'

    dropdown = ttk.Combobox(master=window, textvariable=get_var, values=options,
                            state=state)

    dropdown.bind('<<ComboboxSelected>>', value_set)
    dropdown.grid(row=row, column=column + 2, padx=10, sticky='news')

    state = 'disabled' if default == '' else 'normal'

    reset_button = tk.Button(master=window, text='Reset', state=state,
                             command=lambda: value_set(change_to=default, reset=True))
    reset_button.grid(row=row, column=column + 3, padx=10, sticky='news')


def label_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str, row: float,
                    column: float = 0, columnspan: int = None, pad_y: int = None,
                    sticky: str = 'news'):
    """
    Places a label on specified tkinter window.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    text : str
        Label to place on the tkinter window.
    row : int
        The row number to place the object label in a tkinter grid.
    column : int, optional
        The column number to place the object label in a tkinter grid. The default is 0.
    columnspan : int, optional
        The number of columns to adjust the width of label.
    pad_y : int, optional
        Padding for the label in y direction. The default is None.
    sticky : str, optional
        Alignment of the text within the button. The default is 'news'.

    Returns
    -------
    None

    """
    label = tk.Label(master=window, text=text)
    label.grid(row=int(row), column=int(column), padx=10, pady=pad_y, sticky=sticky,
               columnspan=columnspan)


def entry_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], value: str, row: int,
                    columns: int, width: int = None) -> tk.Entry:
    """
    Places the `tk.Entry` widget in the tkinter window.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    value : str
        The value for given celestial object's property.
    row : int
        The row number to place the tk.Entry in a tkinter grid.
    columns : int
        The column number to place the tk.Entry in a tkinter grid.
    width : int, optional
        Width of the tk.Entry widget. The default is None.

    Returns
    -------
    entry_widget : tk.Entry
        tk.Entry widget.

    """
    entry_widget = tk.Entry(master=window, width=width)
    entry_widget.insert(index=0, string=f'{value}')
    entry_widget.grid(row=int(row), column=int(columns), padx=10, sticky='news')

    return entry_widget


def place_equivalencies(window: Union[tk.Tk, tk.Toplevel, tk.Frame], cel_object: Callable,
                        equiv_type: str, column: int):
    """
    Put the equivalence values for selected celestial object in tkinter window.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    cel_object : Callable
        Celestial object class for which the equivalencies are to be found.
    equiv_type: str
        Whether the equivalencies to be placed are physical or orbital.
    column: int
        Where to place the equivalencies.

    Returns
    -------
    None.

    """
    # keep track of parent window
    parent_window = window

    # geometry of new window
    _w, _h = 300, 100

    # make a new equiv_window to place the equivalency radiobutton
    equiv_window = tk.Toplevel(master=window)
    equiv_window.geometry(newGeometry=f'{_w}x{_h}')

    equiv_window.title(string='Equivalencies')

    get_val = tk.StringVar()

    state = 'disabled' if equiv_type in ['orbital'] else 'active'

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Sun, sec_lbl='Sun',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Sun',
                        value='Sun', radio_val=get_val, row=0, column=0, state=state)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Mercury,
                                                    sec_lbl='Mercury',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Mercury',
                        value='Mercury', radio_val=get_val, row=0, column=1)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Venus, sec_lbl='Venus',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Venus',
                        value='Venus', radio_val=get_val, row=0, column=2)

    state = 'disabled' if equiv_type == 'observation' else 'active'

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Earth, sec_lbl='Earth',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Earth',
                        value='Earth', radio_val=get_val, row=0, column=3, state=state)

    state = 'disabled' if equiv_type in ['orbital', 'observation'] else 'active'

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Moon, sec_lbl='Moon',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Moon',
                        value='Moon', radio_val=get_val, row=1, column=0, state=state)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Mars, sec_lbl='Mars',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Mars',
                        value='Mars', radio_val=get_val, row=1, column=1)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Jupiter,
                                                    sec_lbl='Jupiter',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Jupiter',
                        value='Jupiter', radio_val=get_val, row=1, column=2)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Saturn,
                                                    sec_lbl='Saturn',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Saturn',
                        value='Saturn', radio_val=get_val, row=1, column=3)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Uranus,
                                                    sec_lbl='Uranus',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Uranus',
                        value='Uranus', radio_val=get_val, row=2, column=0)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Neptune,
                                                    sec_lbl='Neptune',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Neptune',
                        value='Neptune', radio_val=get_val, row=2, column=1)

    equiv_radio_buttons(window=equiv_window,
                        function=lambda: comparison(c_win=parent_window,
                                                    primary_obj=cel_object,
                                                    sec_obj=Pluto, sec_lbl='Pluto',
                                                    comparison_type=equiv_type,
                                                    column=column), text='Pluto',
                        value='Pluto', radio_val=get_val, row=2, column=2)

    reset_button = tk.Button(master=equiv_window, text='Reset',
                             command=lambda: comparison(c_win=parent_window,
                                                        primary_obj=cel_object,
                                                        sec_obj=Pluto,
                                                        sec_lbl='Reset',
                                                        comparison_type=equiv_type,
                                                        column=column, reset=True))
    reset_button.grid(row=3, column=0, columnspan=4, padx=10, sticky='news')

    # taken from https://stackoverflow.com/a/69416040/3212945
    for i in range(5):
        equiv_window.grid_columnconfigure(index=i, weight=1)
        equiv_window.grid_rowconfigure(index=i, weight=1)


def equiv_radio_buttons(window: Union[tk.Tk, tk.Toplevel, tk.Frame], function: Callable,
                        text: str, value: str, radio_val: tk.StringVar, row: int,
                        column: int, state: str = 'normal'):
    """
    Add radio buttons to select equivalent values against the selected celestial object.


    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    function : Callable
        A function/method to apply on selection of the radiobutton.
    text : str
        Text to display by the radiobutton.
    value : str
        Value of the radiobutton when selected.
    radio_val : tk.StringVar
        tk.StringVar to store the selected radiobutton value.
    row : int
        The row number to place the tk.Radiobutton in a tkinter grid.
    column : int
        The column number to place the tk.Radiobutton in a tkinter grid.
    state : str
        Determines the state of radiobutton.

    Returns
    -------
    None.

    """
    tk.Radiobutton(master=window, text=text, value=value, variable=radio_val, state=state,
                   command=function).grid(row=row, column=column, sticky='w', padx=5)


def change_value(entry: tk.Entry, value: Union[Quantity, str], change_to: str,
                 function: Callable):
    """
    Change the value of tk.Entry widget.

    Parameters
    ----------
    entry : tk.Entry
        The tk.Entry widget in which the value needs to be changed.
    value : Union[Quantity, str]
        Unit (either string or astropy.units.quantity.Quantity) to change from.
    change_to : str
        The string representing the unit to which the value needs to be changed.
    function : Callable
        A function/method to apply on the tk.Entry widgets.

    Returns
    -------
    None.

    """
    entry.delete(first=0, last='end')
    entry.insert(index=0, string=function(parameter=value, change_to=change_to))


def image_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str, row: int,
                    column: int = 0, wraplength: int = 1550, justify: str = tk.CENTER,
                    sticky: str = 'news'):
    """
    Places images and their descriptions in one of tk.Tk, tk.Toplevel, or tk.Frame

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    text : str
        Text to display with the image.
    row : int
        The row number to place the image in a tkinter widget.
    column : int, optional
        The column number to place the image in a tkinter widget. The default is 0.
    wraplength : int, optional
        Length after which the text is to be wrapped. The default is 1550.
    justify : str, optional
        Justification of text placement in the tkinter widget. The default is tk.CENTER.
    sticky : str, optional
        Alignment of the text within the label. The default is 'news'.

    Returns
    -------
    None.

    """
    tk.Label(master=window, text=text, wraplength=wraplength,
             justify=justify).grid(row=row, column=column, sticky=sticky)
