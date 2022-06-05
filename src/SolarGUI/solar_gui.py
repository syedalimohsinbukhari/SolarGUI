"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

# added try/except because pip bundle and main file do not work with same imports

try:
    from . import show_planet as sp
    from . import tk_functions as tk_f
    from .celestial_objects import (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter,
                                    Saturn, Uranus, Neptune, Pluto)
except ImportError:
    import show_planet as sp
    import tk_functions as tk_f
    from celestial_objects import (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter,
                                   Saturn, Uranus, Neptune, Pluto)


# TODO: Get a good font
# TODO: adjust/create designs in tkinter windows
# TODO: Segregate moons, dwarf planets, planets and other type of celestial objects.
# TODO: Design adjustments of the GUI
# TODO: Some interesting plots (optional).
# TODO: Random facts button.
# TODO: Add citations
# TODO: Add a section of papers that study different properties of the celestial objects.
# TODO: Better GUI layouts, with some fancy stuff
# TODO: Add more parameters
# TODO: Add more celestial bodies
# TODO: See that no button opens more than one window


class Main:

    def __init__(self):
        self.width = 1024
        self.height = 512
        self.root_window = tk.Tk()

        self.root_window.geometry(f'{self.width}x{self.height}')
        self.root_window.minsize(self.width, self.height)

        [self.root_window.grid_columnconfigure(index=i, weight=1) for i in range(9)]

        # put main label inside the tkinter window
        self.label = tk.Label(master=self.root_window,
                              text='Welcome to Solar Explorer. Please select a button.')
        self.label.grid(row=0, column=0, columnspan=9, pady=10,
                        ipady=10)

        tk_f.object_button(window=self.root_window, text='Sun',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Sun',
                                   object_class=Sun()), column=0)

        tk_f.object_button(window=self.root_window, text='Mercury',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Mercury',
                                   object_class=Mercury),
                           column=1)

        tk_f.object_button(window=self.root_window, text='Venus',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Venus',
                                   object_class=Venus),
                           column=2)

        tk_f.object_button(window=self.root_window, text='Earth',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Earth',
                                   object_class=Earth),
                           column=3)

        tk_f.object_button(window=self.root_window, text='Mars',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Mars',
                                   object_class=Mars),
                           column=4)

        tk_f.object_button(window=self.root_window, text='Jupiter',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Jupiter',
                                   object_class=Jupiter),
                           column=5)

        tk_f.object_button(window=self.root_window, text='Saturn',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Saturn',
                                   object_class=Saturn),
                           column=6)

        tk_f.object_button(window=self.root_window, text='Uranus',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Uranus',
                                   object_class=Uranus),
                           column=7)

        tk_f.object_button(window=self.root_window, text='Neptune',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Neptune',
                                   object_class=Neptune),
                           column=8)

        tk_f.object_button(window=self.root_window, text='Moon',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Moon',
                                   object_class=Moon),
                           row=2, column=0)

        tk_f.object_button(window=self.root_window, text='Pluto',
                           function=lambda: sp.GetParameterSelection(
                                   window=self.root_window,
                                   title='Pluto',
                                   object_class=Pluto),
                           row=2, column=1)

        self.root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
