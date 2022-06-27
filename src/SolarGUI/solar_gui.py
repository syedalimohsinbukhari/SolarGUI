"""
Created on May 22 00:40:38 2022
"""

import sys
import tkinter as tk

from tkinter import ttk

# added try/except because pip bundle and main file do not work with same imports
try:
    from . import show_celestial_object as sco
    from . import tk_functions as tk_f
    from . import cel__moons as moons_
    from . import cel__others as others_
    from . import cel__planets as planets_
    from . import cel__stars as stars_
except ImportError:
    import show_celestial_object as sco
    import tk_functions as tk_f
    import cel__moons as moons_
    import cel__others as others_
    import cel__planets as planets_
    import cel__stars as stars_


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
        self.height = 648
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

        tk_f.label_placement(window=self.star_frame, text='Stars', row=0, columnspan=10,
                             pad_y=10, sticky='news')
        tk_f.label_placement(window=self.planet_frame, text='Planets', row=0,
                             columnspan=10, pad_y=10, sticky='news')
        tk_f.label_placement(window=self.moons_frame, text='Moons', row=0, columnspan=10,
                             pad_y=10, sticky='news')
        tk_f.label_placement(window=self.others_frame, text='Others', row=0,
                             columnspan=10, pad_y=10, sticky='news')

        tk_f.object_button(window=self.star_frame, text='Sun',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Sun',
                                   object_class=stars_.Sun), row=1, column=0)

        tk_f.object_button(window=self.planet_frame, text='Mercury',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Mercury',
                                   object_class=planets_.Mercury), row=1, column=0)

        tk_f.object_button(window=self.planet_frame, text='Venus',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Venus',
                                   object_class=planets_.Venus), row=1, column=1)

        tk_f.object_button(window=self.planet_frame, text='Earth',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Earth',
                                   object_class=planets_.Earth), row=1, column=2)

        tk_f.object_button(window=self.planet_frame, text='Mars',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Mars',
                                   object_class=planets_.Mars), row=1, column=3)

        tk_f.object_button(window=self.planet_frame, text='Jupiter',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Jupiter',
                                   object_class=planets_.Jupiter), row=1, column=4)

        tk_f.object_button(window=self.planet_frame, text='Saturn',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Saturn',
                                   object_class=planets_.Saturn), row=1, column=5)

        tk_f.object_button(window=self.planet_frame, text='Uranus',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Uranus',
                                   object_class=planets_.Uranus), row=1, column=6)

        tk_f.object_button(window=self.planet_frame, text='Neptune',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Neptune',
                                   object_class=planets_.Neptune), row=1, column=7)

        tk.Label(master=self.moons_frame, text='Earth: ').grid(row=1,
                                                               column=0,
                                                               sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Moon',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Moon',
                                   object_class=moons_.Moon), row=1, column=1)

        tk.Label(master=self.moons_frame, text='Mars: ').grid(row=2,
                                                              column=0,
                                                              sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Phobos',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Phobos',
                                   object_class=moons_.Phobos), row=2, column=1)

        tk_f.object_button(window=self.moons_frame, text='Deimos',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Deimos',
                                   object_class=moons_.Deimos), row=2, column=2)

        tk.Label(master=self.moons_frame, text='Jupiter: ').grid(row=3,
                                                                 column=0,
                                                                 sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Io',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Io',
                                   object_class=moons_.Io), row=3, column=1)

        tk_f.object_button(window=self.moons_frame, text='Europa',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Europa',
                                   object_class=moons_.Europa), row=3, column=2)

        tk_f.object_button(window=self.moons_frame, text='Ganymede',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Ganymede',
                                   object_class=moons_.Ganymede), row=3, column=3)

        tk_f.object_button(window=self.moons_frame, text='Callisto',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Callisto',
                                   object_class=moons_.Callisto), row=3, column=4)

        tk_f.object_button(window=self.moons_frame, text='Metis',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Metis',
                                   object_class=moons_.Metis), row=3, column=5)

        tk_f.object_button(window=self.moons_frame, text='Adrastea',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Adrastea',
                                   object_class=moons_.Adrastea), row=3, column=6)

        tk_f.object_button(window=self.moons_frame, text='Amalthea',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Amalthea',
                                   object_class=moons_.Amalthea), row=3, column=7)

        tk_f.object_button(window=self.moons_frame, text='Thebe',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Thebe',
                                   object_class=moons_.Europa), row=3, column=8)

        tk.Label(master=self.moons_frame, text='Saturn: ').grid(row=4,
                                                                column=0,
                                                                sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Mimas',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Mimas',
                                   object_class=moons_.Mimas), row=4, column=1)

        tk_f.object_button(window=self.moons_frame, text='Enceladus',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Enceladus',
                                   object_class=moons_.Enceladus), row=4, column=2)

        tk_f.object_button(window=self.moons_frame, text='Tethys',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Tethys',
                                   object_class=moons_.Tethys), row=4, column=3)

        tk_f.object_button(window=self.moons_frame, text='Dione',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Dione',
                                   object_class=moons_.Dione), row=4, column=4)

        tk_f.object_button(window=self.moons_frame, text='Rhea',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Rhea',
                                   object_class=moons_.Rhea), row=4, column=5)

        tk_f.object_button(window=self.moons_frame, text='Titan',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Titan',
                                   object_class=moons_.Titan), row=4, column=6)

        tk_f.object_button(window=self.moons_frame, text='Hyperion',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Hyperion',
                                   object_class=moons_.Hyperion), row=4, column=7)

        tk_f.object_button(window=self.moons_frame, text='Iapetus',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Iapetus',
                                   object_class=moons_.Iapetus), row=4, column=8)

        tk.Label(master=self.moons_frame, text='Uranus: ').grid(row=5,
                                                                column=0,
                                                                sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Miranda',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Miranda',
                                   object_class=moons_.Miranda), row=5, column=1)

        tk_f.object_button(window=self.moons_frame, text='Umbriel',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Umbriel',
                                   object_class=moons_.Umbriel), row=5, column=2)

        tk_f.object_button(window=self.moons_frame, text='Ariel',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Ariel',
                                   object_class=moons_.Ariel), row=5, column=3)

        tk_f.object_button(window=self.moons_frame, text='Titania',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Titania',
                                   object_class=moons_.Titania), row=5, column=4)

        tk_f.object_button(window=self.moons_frame, text='Oberon',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Oberon',
                                   object_class=moons_.Oberon), row=5, column=5)

        tk.Label(master=self.moons_frame, text='Neptune: ').grid(row=6,
                                                                 column=0,
                                                                 sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Naiad',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Naiad',
                                   object_class=moons_.Naiad), row=6, column=1)

        tk_f.object_button(window=self.moons_frame, text='Thalassa',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Thalassa',
                                   object_class=moons_.Thalassa), row=6, column=2)

        tk_f.object_button(window=self.moons_frame, text='Despina',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Despina',
                                   object_class=moons_.Despina), row=6, column=3)

        tk_f.object_button(window=self.moons_frame, text='Galatea',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Galatea',
                                   object_class=moons_.Galatea), row=6, column=4)

        tk_f.object_button(window=self.moons_frame, text='Larissa',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Larissa',
                                   object_class=moons_.Larissa), row=6, column=5)

        tk_f.object_button(window=self.moons_frame, text='Hippocamp',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Hippocamp',
                                   object_class=moons_.Hippocamp), row=6, column=6)

        tk_f.object_button(window=self.moons_frame, text='Proteus',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Proteus',
                                   object_class=moons_.Proteus), row=6, column=7)

        tk_f.object_button(window=self.moons_frame, text='Triton',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Triton',
                                   object_class=moons_.Triton), row=6, column=8)

        tk.Label(master=self.moons_frame, text='Pluto: ').grid(row=7,
                                                               column=0,
                                                               sticky='news')

        tk_f.object_button(window=self.moons_frame, text='Charon',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Charon',
                                   object_class=moons_.Charon), row=7, column=1)

        tk_f.object_button(window=self.others_frame, text='Pluto',
                           function=lambda: sco.GetParameterSelection(
                                   window=self.root_window, object_name='Pluto',
                                   object_class=others_.Pluto), row=1, column=0)

        self.root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
