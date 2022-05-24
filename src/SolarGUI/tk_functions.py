"""
Created on May 24 22:08:46 2022
"""

import tkinter as tk
from tkinter import ttk
from typing import Callable


def planet_button(window, text, function, column, row=1):
    tk.Button(master=window, text=text,
              command=lambda: function()).grid(row=row, column=column, sticky='w',
                                               padx=10, pady=5)


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
