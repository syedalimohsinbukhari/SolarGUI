"""
Created on May 22 00:40:38 2022
"""

import sys
import tkinter as tk
from tkinter import ttk

from . import (moons, others, planets, show_celestial_object as sco, stars, tk_functions as tk_f)


# TODO: Get a good font
# TODO: adjust/create designs in tkinter windows
# TODO: Some interesting plots (optional).
# TODO: Random facts button.
# TODO: Add citations
# TODO: Add a section of papers that study different properties of the celestial objects.
# TODO: See that no button opens more than one window


class Main:

    def __init__(self):
        self.width = 1024
        self.height = 648
        self.root_window = tk.Tk()

        self.root_window.geometry(f'{self.width}x{self.height}')
        self.root_window.minsize(self.width, self.height)

        self.root_window.title('SolarGUI')

        [self.root_window.grid_columnconfigure(index=i, weight=1) for i in range(8)]

        # put main label inside the tkinter window
        self.label = tk.Label(master=self.root_window, text='Welcome to Solar Explorer. Please select a button.')
        self.label.grid(row=0, column=0, columnspan=8, pady=10, ipady=10)

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

        tk_f.label_placement(window=self.star_frame, text='Stars', row=0, columnspan=10, pad_y=10, sticky='news')
        tk_f.label_placement(window=self.planet_frame, text='Planets', row=0, columnspan=10, pad_y=10, sticky='news')
        tk_f.label_placement(window=self.moons_frame, text='Moons', row=0, columnspan=10, pad_y=10, sticky='news')
        tk_f.label_placement(window=self.others_frame, text='Others', row=0, columnspan=10, pad_y=10, sticky='news')

        tk_f.object_button(window=self.star_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Sun',
                                                                      object_class=stars.Sun),
                           text='Sun', row=1, column=0)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Mercury',
                                                                      object_class=planets.Mercury),
                           text='Mercury', row=1, column=0)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Venus',
                                                                      object_class=planets.Venus),
                           text='Venus', row=1, column=1)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Earth',
                                                                      object_class=planets.Earth),
                           text='Earth', row=1, column=2)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Mars',
                                                                      object_class=planets.Mars),
                           text='Mars', row=1, column=3)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Jupiter',
                                                                      object_class=planets.Jupiter),
                           text='Jupiter', row=1, column=4)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Saturn',
                                                                      object_class=planets.Saturn),
                           text='Saturn', row=1, column=5)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Uranus',
                                                                      object_class=planets.Uranus),
                           text='Uranus', row=1, column=6)

        tk_f.object_button(window=self.planet_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Neptune',
                                                                      object_class=planets.Neptune),
                           text='Neptune', row=1, column=7)

        tk.Label(master=self.moons_frame, text='Earth: ').grid(row=1, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Moon',
                                                                      object_class=moons.Moon),
                           text='Moon', row=1, column=1)

        tk.Label(master=self.moons_frame, text='Mars: ').grid(row=2, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Phobos',
                                                                      object_class=moons.Phobos),
                           text='Phobos', row=2, column=1)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Deimos',
                                                                      object_class=moons.Deimos),
                           text='Deimos', row=2, column=2)

        tk.Label(master=self.moons_frame, text='Jupiter: ').grid(row=3, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Io',
                                                                      object_class=moons.Io),
                           text='Io', row=3, column=1)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Europa',
                                                                      object_class=moons.Europa),
                           text='Europa', row=3, column=2)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Ganymede',
                                                                      object_class=moons.Ganymede),
                           text='Ganymede', row=3, column=3)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Callisto',
                                                                      object_class=moons.Callisto),
                           text='Callisto', row=3, column=4)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Metis',
                                                                      object_class=moons.Metis),
                           text='Metis', row=3, column=5)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Adrastea',
                                                                      object_class=moons.Adrastea),
                           text='Adrastea', row=3, column=6)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Amalthea',
                                                                      object_class=moons.Amalthea),
                           text='Amalthea', row=3, column=7)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Thebe',
                                                                      object_class=moons.Europa),
                           text='Thebe', row=3, column=8)

        tk.Label(master=self.moons_frame, text='Saturn: ').grid(row=4, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Mimas',
                                                                      object_class=moons.Mimas),
                           text='Mimas', row=4, column=1)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Enceladus',
                                                                      object_class=moons.Enceladus),
                           text='Enceladus', row=4, column=2)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Tethys',
                                                                      object_class=moons.Tethys),
                           text='Tethys', row=4, column=3)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Dione',
                                                                      object_class=moons.Dione),
                           text='Dione', row=4, column=4)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Rhea',
                                                                      object_class=moons.Rhea),
                           text='Rhea', row=4, column=5)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Titan', object_class=moons.Titan),
                           text='Titan', row=4, column=6)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Hyperion',
                                                                      object_class=moons.Hyperion),
                           text='Hyperion', row=4, column=7)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Iapetus',
                                                                      object_class=moons.Iapetus),
                           text='Iapetus', row=4, column=8)

        tk.Label(master=self.moons_frame, text='Uranus: ').grid(row=5, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Miranda',
                                                                      object_class=moons.Miranda),
                           text='Miranda', row=5, column=1)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Umbriel',
                                                                      object_class=moons.Umbriel),
                           text='Umbriel', row=5, column=2)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Ariel',
                                                                      object_class=moons.Ariel),
                           text='Ariel', row=5, column=3)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Titania',
                                                                      object_class=moons.Titania),
                           text='Titania', row=5, column=4)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Oberon',
                                                                      object_class=moons.Oberon),
                           text='Oberon', row=5, column=5)

        tk.Label(master=self.moons_frame, text='Neptune: ').grid(row=6, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Naiad',
                                                                      object_class=moons.Naiad),
                           text='Naiad', row=6, column=1)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Thalassa',
                                                                      object_class=moons.Thalassa),
                           text='Thalassa', row=6, column=2)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Despina',
                                                                      object_class=moons.Despina),
                           text='Despina', row=6, column=3)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Galatea',
                                                                      object_class=moons.Galatea),
                           text='Galatea', row=6, column=4)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Larissa',
                                                                      object_class=moons.Larissa),
                           text='Larissa', row=6, column=5)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Hippocamp',
                                                                      object_class=moons.Hippocamp),
                           text='Hippocamp', row=6, column=6)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Proteus',
                                                                      object_class=moons.Proteus),
                           text='Proteus', row=6, column=7)

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Triton',
                                                                      object_class=moons.Triton),
                           text='Triton', row=6, column=8)

        tk.Label(master=self.moons_frame, text='Pluto: ').grid(row=7, column=0, sticky='news')

        tk_f.object_button(window=self.moons_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Charon',
                                                                      object_class=moons.Charon),
                           text='Charon', row=7, column=1)

        tk_f.object_button(window=self.others_frame,
                           function=lambda: sco.GetParameterSelection(window=self.root_window,
                                                                      object_name='Pluto',
                                                                      object_class=others.Pluto),
                           text='Pluto', row=1, column=0)

        self.root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
