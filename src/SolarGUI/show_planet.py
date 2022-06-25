"""
Created on May 24 22:12:45 2022
"""

import itertools
import os
import tkinter as tk
from typing import Any, Callable, Union

from PIL import Image, ImageTk

# add path to images
img_path = f'{os.getcwd()}/src/SolarGUI/images/'

# added try/except because pip bundle and main file do not work with same imports
try:
    from . import tk_functions as tk_f
    from .utilities import convert
except ImportError:
    import tk_functions as tk_f
    from utilities import convert

star_list = ['Sun']
planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
               'Pluto']
moon_list = ['Moon', 'Phobos', 'Deimos']

planet_moon = {'Moon': 'Earth',
               'Phobos': 'Mars',
               'Deimos': 'Mars'}


class GetParameterSelection:
    """
    The GetParameterSelection class holds the button for Physical, Orbital,
    Observational parameter and images and more?
    """

    def __init__(self, window: Union[tk.Tk, tk.Toplevel, tk.Frame], object_name: str,
                 object_class: Callable):
        """
        Initialization function for GetParameterSelection class

        Parameters
        ----------
        window : Union[tk.Tk, tk.Toplevel, tk.Frame]
            tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
        object_name : str
            Name of the celestial object.
        object_class : Callable
            The python class for the celestial object.

        Returns
        -------
        None.

        """
        self.par_window = tk.Toplevel(window)

        _w, _h = window.winfo_width(), window.winfo_height()

        self.par_window.geometry(newGeometry=f'{_w}x{_h}')
        self.par_window.title(string=object_name)

        self.button_frame = tk.Frame(master=self.par_window, padx=10, pady=10)
        self.button_frame.pack(side=tk.TOP)

        self.parameter_frame = tk.Frame(master=self.par_window, padx=10, pady=10)
        self.parameter_frame.pack(side=tk.BOTTOM, expand=True)

        # Physical parameter button
        self.phy = tk.Button(master=self.button_frame, text='Physical Parameters',
                             command=lambda: show_physical_parameters(
                                     window=self.parameter_frame,
                                     object_class=object_class))
        self.phy.grid(row=0, column=0, sticky='news')

        # Orbital parameter button
        if object_name != 'Sun':
            self.orb = tk.Button(master=self.button_frame, text='Orbital Parameters',
                                 command=lambda: show_orbital_parameters(
                                         window=self.parameter_frame,
                                         object_name=object_name,
                                         object_class=object_class))
            self.orb.grid(row=0, column=1, sticky='news')

        # Observational parameter button
        if object_name != 'Earth':
            self.obs = tk.Button(master=self.button_frame,
                                 text='Observational Parameters',
                                 command=lambda: show_observational_parameters(
                                         window=self.parameter_frame,
                                         object_name=object_name,
                                         object_class=object_class))
            self.obs.grid(row=0, column=2, sticky='news')

        # Image button
        img = tk.Button(master=self.button_frame, text='Images',
                        command=lambda: Images_(window=window, object_name=object_name,
                                                object_class=object_class).adjustments())
        img.grid(row=0, column=3, sticky='news')


class Images_:
    """
    Images_ class holds the code for displaying images of the celestial objects.
    """

    def __init__(self, window: Union[tk.Tk, tk.Toplevel, tk.Frame], object_name: str,
                 object_class: Callable):
        """
        Initialization function for Images_ class.

        Parameters
        ----------
        window : Union[tk.Tk, tk.Toplevel, tk.Frame]
            tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
        object_name : str
            Name of the celestial object.
        object_class : Callable
            The python class for the celestial object.

        Returns
        -------
        None.

        """

        screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
        self.w, self.h = int(screen_w * 0.8), int(screen_h * 0.8)
        self.img_win = tk.Toplevel(master=window)
        self.object_class = object_class
        self.object_name = object_name
        self.img_frame = None
        self.img_win.resizable(False, False)

    def adjustments(self):
        """
        Adjusts the image in the provided tkinter widget

        Returns
        -------
        None.

        """

        self.img_win.geometry(newGeometry=f'{self.w}x{self.h}')
        self.img_win.title(f'{self.object_name} images')

        self.img_frame = tk.Frame(master=self.img_win)
        self.img_frame.pack()

        # iter and next_image() ideas taken from
        # https://stackoverflow.com/a/49919635/3212945
        path = f'{img_path}{self.object_name.lower()}/'
        img_list = [f for f in os.listdir(path) if
                    f.endswith('.png') or f.endswith('.jpg')]
        img_ = itertools.cycle(img_list)

        def next_image():
            """
            Iterator function to get the next image on button click

            Returns
            -------
            None.

            """

            img = next(img_)
            img_name = img.title()
            img_title = img_name.split(' : ')[0]
            img_descr = f"{img_name.split(' : ')[1].split(' ~ ')[0]}.".capitalize()
            img_credits = f"{img_name.split(' ~ ')[1].split('.Jp')[0]}.".upper()

            # thumbnail idea taken from https://stackoverflow.com/a/66506713
            img = Image.open(f'{path}{img}')
            img.thumbnail((self.w, self.h - 120))
            img = ImageTk.PhotoImage(img)

            self.img_frame.picture = img
            self.img_frame.label = tk.Label(master=self.img_frame,
                                            image=self.img_frame.picture)
            self.img_frame.label.grid(row=0, column=0, sticky='news')

            tk_f.image_placement(window=self.img_frame, text=img_title, row=1)

            tk_f.label_placement(window=self.img_frame, text='', row=2)

            tk_f.image_placement(window=self.img_frame, text=img_descr, row=3)

            tk_f.label_placement(window=self.img_frame, text='', row=4)

            tk_f.image_placement(window=self.img_frame, text=img_credits, row=5)

        next_image()

        tk_f.label_placement(window=self.img_frame, text='', row=4, column=0)

        tk_f.object_button(window=self.img_frame, text='Next Image',
                           function=lambda: next_image(), row=6, column=0, sticky='')


def show_physical_parameters(window: Union[tk.Tk, tk.Toplevel, tk.Frame],
                             object_class: Any):
    """
    Display the physical parameters of the celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk or tk.Toplevel window or a tk.Frame to build the object inside.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    _children = window.winfo_children()

    for child in _children:
        child.destroy()

    object_class = object_class.PhysicalParameters()

    planet_window = window

    # adjust the columns in window's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(5)]

    # heading labels
    tk_f.label_placement(window=planet_window, text='Physical parameters', row=0,
                         column=0, pad_y=5, sticky='e')
    tk_f.label_placement(window=planet_window, text='Values', row=0, column=1, pad_y=5)
    tk_f.label_placement(window=planet_window, text='Unit space', row=0, column=2,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text='Reset', row=0, column=3, pad_y=5)

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text='Equivalences',
                       function=lambda: tk_f.place_equivalencies(window=planet_window,
                                                                 cel_object=object_class,
                                                                 equiv_type='physical',
                                                                 column=4),
                       row=0, column=4, sticky='nsew', width=25)

    # placing the details of celestial objects one by one
    tk_f.place_object_properties(window=planet_window, text='Age', value=object_class.age,
                                 function=convert, row=1, column=0,
                                 options=('s', 'yr', 'Myr', 'Gyr'), default='Gyr')

    tk_f.place_object_properties(window=planet_window, text='Mass',
                                 value=object_class.mass, function=convert, row=2,
                                 column=0, options=('g', 'kg', 'M_earth', 'M_jupiter',
                                                    'M_sun'), default='kg')

    tk_f.place_object_properties(window=planet_window, text='Radius',
                                 value=object_class.radius, function=convert, row=3,
                                 column=0, options=('cm', 'm', 'km', 'R_earth',
                                                    'R_jupiter', 'R_sun'), default='km')

    tk_f.place_object_properties(window=planet_window, text='Volume',
                                 value=object_class.volume, function=convert, row=4,
                                 column=0, options=('cm^3', 'm^3', 'km^3'),
                                 default='km^3')

    tk_f.place_object_properties(window=planet_window, text='Density',
                                 value=object_class.density, function=convert, row=5,
                                 column=0, options=('g/cm^3', 'kg/cm^3', 'kg/m^3'),
                                 default='g/cm^3')

    tk_f.place_object_properties(window=planet_window, text='Surface area',
                                 value=object_class.surface_area, function=convert, row=6,
                                 column=0, options=('cm^2', 'm^2', 'km^2'),
                                 default='km^2')

    tk_f.place_object_properties(window=planet_window, text='Surface gravity',
                                 value=object_class.surface_gravity, function=convert,
                                 row=7, column=0, options=('cm/s^2', 'm/s^2', 'km/s^2'),
                                 default='m/s^2')

    tk_f.place_object_properties(window=planet_window, text='Escape velocity',
                                 value=object_class.escape_velocity, function=convert,
                                 row=8, column=0, options=('cm/s', 'm/s', 'km/s', 'km/h'),
                                 default='km/s')


def show_orbital_parameters(window: Union[tk.Tk, tk.Toplevel, tk.Frame], object_name: str,
                            object_class: Any):
    """
    Display the orbital parameters of the celestial object.
    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk or tk.Toplevel window or a tk.Frame to build the object inside.
    object_name: str
        The name of the object in consideration.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    # destroy the previous contents of the frame
    _children = window.winfo_children()

    for child in _children:
        child.destroy()

    # initialize the new data
    object_class = object_class.OrbitalParameters()

    # assign the frame to a new variable
    planet_window = window

    # adjust the columns in frame's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(5)]

    # heading labels
    tk_f.label_placement(window=planet_window, text='Orbital parameters', row=0, column=0,
                         pad_y=5, sticky='e')

    if object_name in planet_moon.keys():
        tk_f.label_placement(window=planet_window,
                             text='The orbital parameters are given with respect to '
                                  f'the planet {planet_moon[object_name]}.', row=20,
                             column=0, columnspan=10, pad_y=10, sticky='news')

    tk_f.label_placement(window=planet_window, text='Values', row=0, column=1, pad_y=5)
    tk_f.label_placement(window=planet_window, text='Unit space', row=0, column=2,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text='Reset', row=0, column=3, pad_y=5)

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text='Equivalences',
                       function=lambda: tk_f.place_equivalencies(window=planet_window,
                                                                 cel_object=object_class,
                                                                 equiv_type='orbital',
                                                                 column=4),
                       row=0, column=4, sticky='nsew', width=25)

    # placing the details of celestial objects one by one
    tk_f.place_object_properties(window=planet_window, text='Semi Major Axis',
                                 value=object_class.semi_major_axis, function=convert,
                                 row=1, column=0, options=('cm', 'm', 'km', 'Gm', 'AU',
                                                           'lyr', 'pc'), default='AU')

    tk_f.place_object_properties(window=planet_window, text='Eccentricity',
                                 value=object_class.eccentricity, function=convert, row=2,
                                 column=0, options=tuple(), default='')

    tk_f.place_object_properties(window=planet_window, text='Closest approach',
                                 value=object_class.apo, function=convert, row=3,
                                 column=0, options=('cm', 'm', 'km', 'Gm', 'AU',
                                                    'lyr', 'pc'), default='AU')

    tk_f.place_object_properties(window=planet_window, text='Farthest approach',
                                 value=object_class.peri, function=convert, row=4,
                                 column=0, options=('cm', 'm', 'km', 'Gm', 'AU', 'lyr',
                                                    'pc'), default='AU')

    tk_f.place_object_properties(window=planet_window, text='Orbital Period',
                                 value=object_class.orbital_period, function=convert,
                                 row=5, column=0, options=('s', 'hr', 'day', 'yr', 'Myr'),
                                 default='day')

    tk_f.place_object_properties(window=planet_window, text='Av. Orbital Speed',
                                 value=object_class.av_orbital_speed, function=convert,
                                 row=6, column=0, options=('cm/s', 'm/s', 'km/s', 'km/h'),
                                 default='km/s')

    tk_f.place_object_properties(window=planet_window, text='Mean anomaly',
                                 value=object_class.mean_anomaly, function=convert, row=7,
                                 column=0, options=('deg', 'rad'), default='deg')

    tk_f.place_object_properties(window=planet_window, text='Inclination',
                                 value=object_class.inclination, function=convert, row=8,
                                 column=0, options=('deg', 'rad'), default='deg')

    tk_f.place_object_properties(window=planet_window, text='Longitude of Asc. node',
                                 value=object_class.longitude_of_ascending_node,
                                 function=convert, row=9, column=0,
                                 options=('deg', 'rad'), default='deg')

    tk_f.place_object_properties(window=planet_window, text='Argument of peri.',
                                 value=object_class.argument_of_perihelion,
                                 function=convert, row=10, column=0,
                                 options=('deg', 'rad'), default='deg')

    tk_f.place_object_properties(window=planet_window, text='Axial Tilt',
                                 value=object_class.axial_tilt, function=convert, row=11,
                                 column=0, options=('deg', 'rad'), default='deg')


def show_observational_parameters(window: Union[tk.Tk, tk.Toplevel, tk.Frame],
                                  object_name: str, object_class: Any):
    """
    Display the orbital parameters of the celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        tk.Tk or tk.Toplevel window or a tk.Frame to build the object inside.
    object_name: str
        Name of the celestial object.
    object_class : Any
        The object clas from which the attributes are to be read.

    Returns
    -------
    None.

    """

    # destroy the previous contents of the frame
    _children = window.winfo_children()

    for child in _children:
        child.destroy()

    # initialize the new data
    object_class = object_class.ObservationalParameters()

    # assign the frame to a new variable
    planet_window = window

    # adjust the columns in frame's width
    [planet_window.grid_columnconfigure(index=i, weight=1) for i in range(5)]

    # heading labels
    tk_f.label_placement(window=planet_window, text='Observational parameters', row=0,
                         column=0, pad_y=5, sticky='e')

    tk_f.label_placement(window=planet_window, text='Values', row=0, column=1, pad_y=5)
    tk_f.label_placement(window=planet_window, text='Unit space', row=0, column=2,
                         pad_y=5)
    tk_f.label_placement(window=planet_window, text='Reset', row=0, column=3, pad_y=5)

    # placing the equivalency button
    tk_f.object_button(window=planet_window, text='Equivalences',
                       function=lambda: tk_f.place_equivalencies(window=planet_window,
                                                                 cel_object=object_class,
                                                                 equiv_type='observation',
                                                                 column=4), row=0,
                       column=4, sticky='nsew', width=25)

    tk_f.place_object_properties(window=planet_window, text='Mean Apparent Magnitude',
                                 value=object_class.apparent_magnitude, function=convert,
                                 row=1, column=0, options=tuple(), default='')

    tk_f.place_object_properties(window=planet_window, text='Geometric Albedo',
                                 value=object_class.geom_albedo, function=convert, row=2,
                                 column=0, options=tuple(), default='')

    tk_f.place_object_properties(window=planet_window, text='Distance from Earth',
                                 value=object_class.distance_from_earth, function=convert,
                                 row=3, column=0, options=('cm', 'm', 'km', 'Gm', 'AU',
                                                           'lyr', 'pc'), default='km')

    tk_f.place_object_properties(window=planet_window, text='Absolute Magnitude',
                                 value=object_class.absolute_magnitude, function=convert,
                                 row=4, column=0, options=tuple(), default='')

    tk_f.place_object_properties(window=planet_window, text='Mean angular size',
                                 value=object_class.average_angular_size,
                                 function=convert, row=5, column=0,
                                 options=('arcsec', 'arcmin', 'deg', 'rad'),
                                 default='arcsec')

    if object_name not in star_list:
        if object_name in planet_list:
            text = 'Distance from Earth for the planet is calculated as the planets\' ' \
                   'distance from Sun in AU - 1 AU.'
        elif object_name in moon_list and object_name != 'Moon':
            _pl_name = [moon for moon, planet in planet_moon.items() if
                        moon == object_name][0]
            text = f'Distance from Earth to {_pl_name} is taken as the distance from ' \
                   f'Earth to the parent planet, e.g, {planet_moon[object_name]}.'
        else:
            text = ''

        tk_f.label_placement(window=planet_window, text=text, row=20, columnspan=10,
                             pad_y=10, sticky='news')
