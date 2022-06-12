"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

from tkinter import ttk

# added try/except because pip bundle and main file do not work with same imports
try:
    from . import show_planet as sp
    from . import tk_functions as tk_f
    from .cel__stars import Sun
    from .cel__planets import (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus,
                               Neptune)
    from .cel__moons import Moon
    from .cel__others import Pluto
except ImportError:
    import show_planet as sp
    import tk_functions as tk_f
    from cel__stars import Sun
    from cel__planets import Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune
    from cel__moons import Moon
    from cel__others import Pluto


# TODO: Get a good font
# TODO: adjust/create designs in tkinter windows
# TODO: Some interesting plots (optional).
# TODO: Random facts button.
# TODO: Add citations
# TODO: Add a section of papers that study different properties of the celestial objects.
# TODO: Add more celestial bodies
# TODO: See that no button opens more than one window


class Main:

    def __init__(self):
        self.width = 1024
        self.height = 448
        self.root_window = tk.Tk()

        self.root_window.geometry(f'{self.width}x{self.height}')
        self.root_window.minsize(self.width, self.height)

        self.root_window.title('SolarGUI')

        [self.root_window.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        # put main label inside the tkinter window
        self.label = tk.Label(master=self.root_window,
                              text='Welcome to Solar Explorer. Please select a button.')
        self.label.grid(row=0, column=0, columnspan=8, pady=10,
                        ipady=10)

        self.star_frame = tk.Frame(master=self.root_window)
        self.star_frame.grid(row=1, column=0, pady=5, columnspan=8)
        [self.star_frame.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        self.sep1 = ttk.Separator(master=self.root_window, orient='horizontal')
        self.sep1.grid(sticky='news', columnspan=10)

        self.planet_frame = tk.Frame(master=self.root_window)
        self.planet_frame.grid(row=2, column=0, pady=5, columnspan=8)
        [self.planet_frame.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        self.sep2 = ttk.Separator(master=self.root_window, orient='horizontal')
        self.sep2.grid(sticky='news', columnspan=10)

        self.moons_frame = tk.Frame(master=self.root_window)
        self.moons_frame.grid(row=3, column=0, pady=5, columnspan=8)
        [self.planet_frame.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        self.sep3 = ttk.Separator(master=self.root_window, orient='horizontal')
        self.sep3.grid(sticky='news', columnspan=10)

        self.others_frame = tk.Frame(master=self.root_window)
        self.others_frame.grid(row=4, column=0, pady=5, columnspan=8)
        [self.others_frame.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        tk_f.label_placement(window=self.star_frame, text='Stars', row=0, pad_y=10,
                             sticky='news', columnspan=10)
        tk_f.label_placement(window=self.planet_frame, text='Planets', row=0, pad_y=10,
                             sticky='news', columnspan=10)
        tk_f.label_placement(window=self.moons_frame, text='Moons', row=0, pad_y=10,
                             sticky='news', columnspan=10)
        tk_f.label_placement(window=self.others_frame, text='Others', row=0, pad_y=10,
                             sticky='news', columnspan=10)

        tk_f.object_button(window=self.star_frame, text='Sun',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Sun',
                                   object_class=Sun), column=0, row=1)

        tk_f.object_button(window=self.planet_frame, text='Mercury',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Mercury',
                                   object_class=Mercury),
                           column=0, row=1)

        tk_f.object_button(window=self.planet_frame, text='Venus',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Venus',
                                   object_class=Venus),
                           column=1, row=1)

        tk_f.object_button(window=self.planet_frame, text='Earth',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Earth',
                                   object_class=Earth),
                           column=2, row=1)

        tk_f.object_button(window=self.planet_frame, text='Mars',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Mars',
                                   object_class=Mars),
                           column=3, row=1)

        tk_f.object_button(window=self.planet_frame, text='Jupiter',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Jupiter',
                                   object_class=Jupiter),
                           column=4, row=1)

        tk_f.object_button(window=self.planet_frame, text='Saturn',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Saturn',
                                   object_class=Saturn),
                           column=5, row=1)

        tk_f.object_button(window=self.planet_frame, text='Uranus',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Uranus',
                                   object_class=Uranus),
                           column=6, row=1)

        tk_f.object_button(window=self.planet_frame, text='Neptune',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Neptune',
                                   object_class=Neptune),
                           column=7, row=1)

        tk_f.object_button(window=self.moons_frame, text='Moon',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Moon',
                                   object_class=Moon),
                           row=1, column=0)

        tk_f.object_button(window=self.others_frame, text='Pluto',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Pluto',
                                   object_class=Pluto),
                           row=1, column=0)

        self.root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
