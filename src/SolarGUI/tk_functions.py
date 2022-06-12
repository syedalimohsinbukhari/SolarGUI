"""
Created on May 24 22:08:46 2022
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable, Optional, Tuple, Union

from astropy.units.quantity import Quantity

try:
    from . import utilities as utils
    from .cel__stars import Sun
    from .cel__planets import (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus,
                               Neptune)
    from .cel__moons import Moon
    from .cel__others import Pluto
except ImportError:
    import utilities as utils
    from cel__stars import Sun
    from cel__planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
    from cel__moons import Moon
    from cel__others import Pluto


def object_button(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str,
                  function: Callable, row: int = 1, column: int = 0, width=None,
                  sticky: str = 'news'):
    """
    Displays a button for a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    text : str
        Text to display on the button.
    function : Callable
        A function/method to apply on click of the button.
    row : int, optional
        The row number to place the object in a tkinter grid. The default is 1.
    column : int, optional
        The column number to place the object in a tkinter grid. The default is 0.
    width : float, optional
        To determine teh width of the button placed.
    sticky : str, optional
        Alignment of the text within the button. The default is 'news'.

    Returns
    -------
    None.

    """
    tk.Button(master=window, text=text,
              command=lambda: function(), width=width).grid(row=row, column=column,
                                                            sticky=sticky, padx=10,
                                                            pady=5)


def place_object_properties(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str,
                            value: str, function: Callable, options: Tuple, row: float,
                            column: float, default: str):
    """
    Place the dropdown menu in the tkinter window grid.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    text : str
        Value name for the celestial object property.
    value : str
        Value that the `get()` method will receive upon selection.
    function : Callable
        A function/method to apply on selection of the dropdown item.
    options : Tuple
        Option tuple which will be displayed in the dropdown menu.
    row : float
        The row number to place the dropdown menu object in a tkinter grid. The default
        is 1.
    column: float
        The starting column number for the widget placement.
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

        change_value(entry=val_entry, function=function, value=value, change_to=change_to)

    get_var = tk.StringVar()

    # taken from https://stackoverflow.com/a/68128312/3212945

    state = 'readonly' if text.lower() not in ['eccentricity', 'geometric albedo',
                                               'apparent magnitude',
                                               'absolute magnitude'] else 'disabled'

    dropdown = ttk.Combobox(master=window, textvariable=get_var, values=options,
                            state=state)

    dropdown.bind('<<ComboboxSelected>>', value_set)
    dropdown.grid(row=int(row), column=int(column + 2), padx=10, sticky='news')

    state = 'disabled' if default is '' else 'normal'

    reset_button = tk.Button(master=window, text='Reset', state=state,
                             command=lambda: value_set(change_to=default, reset=True))
    reset_button.grid(row=int(row), column=int(column + 3), padx=10, sticky='news')


def label_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str, row: float,
                    column: float = 0, pad_y: Optional[int] = None, sticky: str = 'news',
                    columnspan: Optional[int] = None):
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
    sticky : str, optional
        Alignment of the text within the button. The default is 'news'.
    pad_y : Optional[int], optional
        Padding for the label in y direction. The default is None.
    columnspan : int, optional
        The number of columns to adjust the width of label.

    Returns
    -------
    None

    """
    label = tk.Label(master=window, text=text)
    label.grid(row=int(row), column=int(column), padx=10, pady=pad_y, sticky=sticky,
               columnspan=columnspan)


def entry_placement(window: Union[tk.Tk, tk.Toplevel, tk.Frame], value: str, row: float,
                    columns: float, width: Optional[int] = None) -> tk.Entry:
    """
    Places the `tk.Entry` widget in the tkinter window.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    value : str
        The value for given celestial object's property.
    row : float
        The row number to place the tk.Entry in a tkinter grid.
    columns : float
        The column number to place the tk.Entry in a tkinter grid.
    width : Optional[int], optional
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
                        column: float, equiv_type: str):
    """
    Put the equivalence values for selected celestial object in tkinter window.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    cel_object : Callable
        Celestial object class for which the equivalencies are to be found.
    column: float
        Where to place the equivalencies.
    equiv_type: str
        Whether the equivalencies to be placed are physical or orbital.

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

    equiv_radio_buttons(window=equiv_window, text='Sun', value='Sun', radio_val=get_val,
                        state=state,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Sun,
                                                          c_lbl='Sun',
                                                          c_type=equiv_type,
                                                          column=column), row=0, column=0)

    equiv_radio_buttons(window=equiv_window, text='Mercury', value='Mercury',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Mercury,
                                                          c_lbl='Mercury',
                                                          c_type=equiv_type,
                                                          column=column), row=0, column=1)

    equiv_radio_buttons(window=equiv_window, text='Venus', value='Venus',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Venus,
                                                          c_lbl='Venus',
                                                          c_type=equiv_type,
                                                          column=column), row=0, column=2)

    state = 'disabled' if equiv_type is 'observation' else 'active'

    equiv_radio_buttons(window=equiv_window, text='Earth', value='Earth',
                        radio_val=get_val, state=state,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Earth,
                                                          c_lbl='Earth',
                                                          c_type=equiv_type,
                                                          column=column), row=0, column=3)

    state = 'disabled' if equiv_type in ['orbital', 'observation'] else 'active'

    equiv_radio_buttons(window=equiv_window, text='Moon', value='Moon',
                        radio_val=get_val, state=state,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Moon,
                                                          c_lbl='Moon',
                                                          c_type=equiv_type,
                                                          column=column), row=1, column=0)

    equiv_radio_buttons(window=equiv_window, text='Mars', value='Mars', radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Mars,
                                                          c_lbl='Mars',
                                                          c_type=equiv_type,
                                                          column=column), row=1, column=1)

    equiv_radio_buttons(window=equiv_window, text='Jupiter', value='Jupiter',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Jupiter,
                                                          c_lbl='Jupiter',
                                                          c_type=equiv_type,
                                                          column=column), row=1, column=2)

    equiv_radio_buttons(window=equiv_window, text='Saturn', value='Saturn',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Saturn,
                                                          c_lbl='Saturn',
                                                          c_type=equiv_type,
                                                          column=column), row=1, column=3)

    equiv_radio_buttons(window=equiv_window, text='Uranus', value='Uranus',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Uranus,
                                                          c_lbl='Uranus',
                                                          c_type=equiv_type,
                                                          column=column), row=2, column=0)

    equiv_radio_buttons(window=equiv_window, text='Neptune', value='Neptune',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Neptune,
                                                          c_lbl='Neptune',
                                                          c_type=equiv_type,
                                                          column=column), row=2, column=1)

    equiv_radio_buttons(window=equiv_window, text='Pluto', value='Pluto',
                        radio_val=get_val,
                        function=lambda: utils.comparison(c_win=parent_window,
                                                          p_ojb=cel_object,
                                                          c_obj=Pluto,
                                                          c_lbl='Pluto',
                                                          c_type=equiv_type,
                                                          column=column), row=2, column=2)

    reset_button = tk.Button(master=equiv_window, text='Reset',
                             command=lambda: utils.comparison(c_win=parent_window,
                                                              p_ojb=cel_object,
                                                              c_obj=Pluto,
                                                              c_lbl='Reset',
                                                              c_type=equiv_type,
                                                              reset=True, column=column))
    reset_button.grid(row=3, column=0, columnspan=4, padx=10, sticky='news')

    # taken from https://stackoverflow.com/a/69416040/3212945
    for i in range(5):
        equiv_window.grid_columnconfigure(index=i, weight=1)
        equiv_window.grid_rowconfigure(index=i, weight=1)


def equiv_radio_buttons(window: Union[tk.Tk, tk.Toplevel, tk.Frame], text: str,
                        value: str, radio_val: tk.StringVar, function: Callable, row: int,
                        column: int, state='normal'):
    """
    Add radio buttons to select equivalent values against the selected celestial object.


    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
    text : str
        Text to display by the radiobutton.
    value : str
        Value of the radiobutton when selected.
    radio_val : tk.StringVar
        tk.StringVar to store the selected radiobutton value.
    function : Callable
        A function/method to apply on selection of the radiobutton.
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


def change_value(entry: tk.Entry, function: Callable, value: Union[Quantity, str],
                 change_to: str):
    """
    Change the value of tk.Entry widget.

    Parameters
    ----------
    entry : tk.Entry
        The tk.Entry widget in which the value needs to be changed.
    function : Callable
        A function/method to apply on the tk.Entry widgets.
    value : Union[Quantity, str]
        Unit (either string or astropy.units.quantity.Quantity) to change from.
    change_to : str
        The string representing the unit to which the value needs to be changed.

    Returns
    -------
    None.

    """
    entry.delete(first=0, last='end')
    entry.insert(index=0, string=function(parameter=value, change_to=change_to))
