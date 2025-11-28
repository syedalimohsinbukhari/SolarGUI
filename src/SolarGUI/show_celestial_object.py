"""
Created on May 24 22:12:45 2022

Celestial object parameter display module for SolarGUI.

This module handles the display of physical, orbital, and observational
parameters for celestial objects in detailed parameter windows.
"""

import tkinter as tk
from typing import Any, Union

from . import tk_functions, utilities

# Modern color scheme (shared with other modules)
COLORS = {
    'bg_dark': '#1a1a2e',
    'bg_medium': '#16213e',
    'bg_light': '#0f3460',
    'accent': '#e94560',
    'text_light': '#eaeaea',
    'text_muted': '#a0a0a0',
    'button_bg': '#0f3460',
    'button_hover': '#e94560',
}

# Celestial object categorization
STAR_LIST = ['Sun']

PLANET_LIST = [
    'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'
]

MOON_LIST = [
    'Moon',
    'Phobos', 'Deimos',
    'Io', 'Europa', 'Ganymede', 'Callisto', 'Metis', 'Adrastea', 'Amalthea', 'Thebe',
    'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion', 'Iapetus',
    'Miranda', 'Umbrial', 'Ariel', 'Titania', 'Oberon',
    'Naiad', 'Thalassa', 'Despina', 'Galatea', 'Larissa', 'Hippocamp', 'Proteus', 'Triton',
    'Charon'
]

# Moon to parent planet mapping
PLANET_MOON = {
    'Moon': 'Earth',
    'Phobos': 'Mars', 'Deimos': 'Mars',
    'Io': 'Jupiter', 'Europa': 'Jupiter', 'Ganymede': 'Jupiter', 'Callisto': 'Jupiter',
    'Metis': 'Jupiter', 'Adrastea': 'Jupiter', 'Amalthea': 'Jupiter', 'Thebe': 'Jupiter',
    'Mimas': 'Saturn', 'Enceladus': 'Saturn', 'Tethys': 'Saturn', 'Dione': 'Saturn',
    'Rhea': 'Saturn', 'Titan': 'Saturn', 'Hyperion': 'Saturn', 'Iapetus': 'Saturn',
    'Miranda': 'Uranus', 'Umbrial': 'Uranus', 'Ariel': 'Uranus',
    'Titania': 'Uranus', 'Oberon': 'Uranus',
    'Naiad': 'Neptune', 'Thalassa': 'Neptune', 'Despina': 'Neptune', 'Galatea': 'Neptune',
    'Larissa': 'Neptune', 'Hippocamp': 'Neptune', 'Proteus': 'Neptune', 'Triton': 'Neptune',
    'Charon': 'Pluto'
}


class GetParameterSelection:
    """
    Parameter selection window for celestial objects.

    Displays buttons for Physical, Orbital, and Observational parameters
    of the selected celestial object.
    """

    def __init__(self, window, object_name, object_class):
        """
        Initialize the parameter selection window.

        Parameters
        ----------
        window : Union[tk.Tk, tk.Toplevel, tk.Frame]
            Parent window reference.
        object_name : str
            Display name of the celestial object.
        object_class : Any
            Class containing the celestial object's data.

        """
        self.par_window = tk.Toplevel(window)
        self.object_name = object_name
        self.object_class = object_class

        self._setup_window(window)
        self._create_frames()
        self._create_parameter_buttons()

    def _setup_window(self, parent_window):
        """Configure the parameter window appearance."""
        _w, _h = parent_window.winfo_width(), parent_window.winfo_height()

        self.par_window.geometry(newGeometry='{}x{}'.format(_w, _h))
        self.par_window.title(string=self.object_name)
        self.par_window.configure(bg=COLORS['bg_dark'])

    def _create_frames(self):
        """Create the button and parameter display frames."""
        self.button_frame = tk.Frame(
            master=self.par_window,
            padx=10,
            pady=10,
            bg=COLORS['bg_dark']
        )
        self.button_frame.pack(side=tk.TOP)

        self.parameter_frame = tk.Frame(
            master=self.par_window,
            padx=10,
            pady=10,
            bg=COLORS['bg_medium']
        )
        self.parameter_frame.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    def _create_parameter_buttons(self):
        """Create buttons for different parameter types."""
        button_config = {
            'font': ('Helvetica', 10),
            'bg': COLORS['button_bg'],
            'fg': COLORS['text_light'],
            'activebackground': COLORS['button_hover'],
            'activeforeground': COLORS['text_light'],
            'relief': tk.FLAT,
            'cursor': 'hand2',
            'width': 20
        }

        # Physical Parameters button (always shown)
        self.phy = tk.Button(
            master=self.button_frame,
            text='Physical Parameters',
            command=lambda: show_physical_parameters(
                window=self.parameter_frame,
                object_class=self.object_class
            ),
            **button_config
        )
        self.phy.grid(row=0, column=0, padx=5, pady=5, sticky='news')
        self._add_hover_effect(self.phy)

        # Orbital Parameters button (not shown for Sun)
        if self.object_name != 'Sun':
            self.orb = tk.Button(
                master=self.button_frame,
                text='Orbital Parameters',
                command=lambda: show_orbital_parameters(
                    window=self.parameter_frame,
                    object_name=self.object_name,
                    object_class=self.object_class
                ),
                **button_config
            )
            self.orb.grid(row=0, column=1, padx=5, pady=5, sticky='news')
            self._add_hover_effect(self.orb)

        # Observational Parameters button (not shown for Earth)
        if self.object_name != 'Earth':
            self.obs = tk.Button(
                master=self.button_frame,
                text='Observational Parameters',
                command=lambda: show_observational_parameters(
                    window=self.parameter_frame,
                    object_name=self.object_name,
                    object_class=self.object_class
                ),
                **button_config
            )
            self.obs.grid(row=0, column=2, padx=5, pady=5, sticky='news')
            self._add_hover_effect(self.obs)

    def _add_hover_effect(self, button):
        """Add hover effect to a button."""
        button.bind('<Enter>', lambda e: button.configure(bg=COLORS['button_hover']))
        button.bind('<Leave>', lambda e: button.configure(bg=COLORS['button_bg']))


# class _Images:
#     """
#     _Images class holds the code for displaying images of the celestial objects.
#     """
#
#     def __init__(self, window: Union[tk.Tk, tk.Toplevel, tk.Frame], object_name: str,
#                  object_class: Any):
#         """
#         Initialization function for _Images class.
#
#         Parameters
#         ----------
#         window : Union[tk.Tk, tk.Toplevel, tk.Frame]
#             tk.Tk, tk.Toplevel window or tk.Frame to build the object inside.
#         object_name : str
#             Name of the celestial object.
#         object_class : Any
#             The python class for the celestial object.
#
#         Returns
#         -------
#         None.
#
#         """
#
#         screen_w, screen_h = window.winfo_screenwidth(), window.winfo_screenheight()
#         self.w, self.h = int(screen_w * 0.8), int(screen_h * 0.8)
#         self.img_win = tk.Toplevel(master=window)
#         self.object_class = object_class
#         self.object_name = object_name
#         self.img_frame = None
#         self.img_win.resizable(False, False)
#
#     def adjustments(self):
#         """
#         Adjusts the image in the provided tkinter widget
#
#         Returns
#         -------
#         None.
#
#         """
#
#         self.img_win.geometry(newGeometry=f'{self.w}x{self.h}')
#         self.img_win.title(f'{self.object_name} images')
#
#         self.img_frame = tk.Frame(master=self.img_win)
#         self.img_frame.pack()
#
#         # iter and next_image() ideas taken from
#         # https://stackoverflow.com/a/49919635/3212945
#         path = f'{img_path}{self.object_name.lower()}/'
#         img_list = [f for f in os.listdir(path) if
#                     f.endswith('.png') or f.endswith('.jpg')]
#         img_ = itertools.cycle(img_list)
#
#         def next_image():
#             """
#             Iterator function to get the next image on button click
#
#             Returns
#             -------
#             None.
#
#             """
#
#             img = next(img_)
#             img_name = img.title()
#             img_title = img_name.split(' : ')[0]
#             img_descr = f"{img_name.split(' : ')[1].split(' ~ ')[0]}.".capitalize()
#             img_credits = f"{img_name.split(' ~ ')[1].split('.Jp')[0]}.".upper()
#
#             # thumbnail idea taken from https://stackoverflow.com/a/66506713
#             img = Image.open(f'{path}{img}')
#             img.thumbnail((self.w, self.h - 120))
#             img = ImageTk.PhotoImage(img)
#
#             self.img_frame.picture = img
#             self.img_frame.label = tk.Label(master=self.img_frame,
#                                             image=self.img_frame.picture)
#             self.img_frame.label.grid(row=0, column=0, sticky='news')
#
#             tk_functions.image_placement(window=self.img_frame, text=img_title, row=1)
#
#             tk_functions.label_placement(window=self.img_frame, text='', row=2)
#
#             tk_functions.image_placement(window=self.img_frame, text=img_descr, row=3)
#
#             tk_functions.label_placement(window=self.img_frame, text='', row=4)
#
#             tk_functions.image_placement(window=self.img_frame, text=img_credits, row=5)
#
#         next_image()
#
#         tk_functions.label_placement(window=self.img_frame, text='', row=4, column=0)
#
#         tk_functions.object_button(window=self.img_frame, function=lambda: next_image(),
#                                    text='Next Image', row=6, column=0, sticky='')


def _clear_window(window):
    """Clear all child widgets from a window."""
    for child in window.winfo_children():
        child.destroy()


def _setup_column_weights(window, num_columns=5):
    """Configure column weights for the window grid."""
    for i in range(num_columns):
        window.grid_columnconfigure(index=i, weight=1)


def _create_header_labels(window, parameter_type):
    """Create header labels for parameter display."""
    tk_functions.label_placement(
        window=window, text='{} parameters'.format(parameter_type),
        row=0, column=0, pad_y=5, sticky='e'
    )
    tk_functions.label_placement(window=window, text='Values', row=0, column=1, pad_y=5)
    tk_functions.label_placement(window=window, text='Unit space', row=0, column=2, pad_y=5)
    tk_functions.label_placement(window=window, text='Reset', row=0, column=3, pad_y=5)


def show_physical_parameters(window, object_class):
    """
    Display the physical parameters of a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for displaying parameters.
    object_class : Any
        Celestial object class containing the data.

    """
    _clear_window(window)
    object_class = object_class.PhysicalParameters()
    planet_window = window

    _setup_column_weights(planet_window)
    _create_header_labels(planet_window, 'Physical')

    # Equivalencies button
    tk_functions.object_button(
        window=planet_window,
        function=lambda: tk_functions.place_equivalencies(
            window=planet_window, cel_object=object_class,
            equiv_type='physical', column=4
        ),
        text='Equivalences', row=0, column=4, sticky='nsew', width=25
    )

    # Age options
    if object_class.age is None:
        age_opt, def_ = tuple(), ''
    else:
        age_opt, def_ = ('s', 'yr', 'Myr', 'Gyr'), 'Gyr'

    # Physical parameters
    parameters = [
        ('Age', object_class.age, 1, age_opt, def_),
        ('Mass', object_class.mass, 2, ('g', 'kg', 'M_earth', 'M_jupiter', 'M_sun'), 'kg'),
        ('Radius', object_class.radius, 3, ('cm', 'm', 'km', 'R_earth', 'R_jupiter', 'R_sun'), 'km'),
        ('Volume', object_class.volume, 4, ('cm^3', 'm^3', 'km^3'), 'km^3'),
        ('Density', object_class.density, 5, ('g/cm^3', 'kg/cm^3', 'kg/m^3'), 'g/cm^3'),
        ('Surface area', object_class.surface_area, 6, ('cm^2', 'm^2', 'km^2'), 'km^2'),
        ('Surface gravity', object_class.surface_gravity, 7, ('cm/s^2', 'm/s^2', 'km/s^2'), 'm/s^2'),
        ('Escape velocity', object_class.escape_velocity, 8, ('cm/s', 'm/s', 'km/s', 'km/h'), 'km/s'),
    ]

    for text, value, row, options, default in parameters:
        tk_functions.place_object_properties(
            window=planet_window, function=utilities.convert,
            text=text, value=value, row=row, column=0,
            options=options, default=default
        )


def show_orbital_parameters(window, object_name, object_class):
    """
    Display the orbital parameters of a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for displaying parameters.
    object_name : str
        Name of the celestial object.
    object_class : Any
        Celestial object class containing the data.

    """
    _clear_window(window)
    object_class = object_class.OrbitalParameters()
    planet_window = window

    _setup_column_weights(planet_window)
    _create_header_labels(planet_window, 'Orbital')

    # Info label for moons
    if object_name in PLANET_MOON.keys():
        tk_functions.label_placement(
            window=planet_window,
            text='The orbital parameters are given with respect to the planet {}.'.format(
                PLANET_MOON[object_name]
            ),
            row=20, column=0, columnspan=10, pad_y=10, sticky='news'
        )

    # Equivalencies button
    tk_functions.object_button(
        window=planet_window,
        function=lambda: tk_functions.place_equivalencies(
            window=planet_window, cel_object=object_class,
            equiv_type='orbital', column=4
        ),
        text='Equivalences', row=0, column=4, sticky='nsew', width=25
    )

    # Distance options
    dist_opts = ('cm', 'm', 'km', 'Gm', 'AU', 'lyr', 'pc')

    # Get dynamic options for various parameters
    t_orb_ = utilities.get_options(object_class.orbital_period, 't_orb')
    v_orb_ = utilities.get_options(object_class.av_orbital_speed, 'v_orb')
    anom_ = utilities.get_options(object_class.mean_anomaly, 'm_anom')
    incl_ = utilities.get_options(object_class.inclination, 'incl')
    long_ = utilities.get_options(object_class.longitude_of_ascending_node, 'long')
    peri_ = utilities.get_options(object_class.argument_of_perihelion, 'arg')
    tilt_ = utilities.get_options(object_class.axial_tilt, 'tilt')

    # Orbital parameters
    parameters = [
        ('Semi Major Axis', object_class.semi_major_axis, 1, dist_opts, 'AU'),
        ('Eccentricity', object_class.eccentricity, 2, tuple(), ''),
        ('Closest approach', object_class.apo, 3, dist_opts, 'AU'),
        ('Farthest approach', object_class.peri, 4, dist_opts, 'AU'),
        ('Orbital Period', object_class.orbital_period, 5, t_orb_[0], t_orb_[1]),
        ('Av. Orbital Speed', object_class.av_orbital_speed, 6, v_orb_[0], v_orb_[1]),
        ('Mean anomaly', object_class.mean_anomaly, 7, anom_[0], anom_[1]),
        ('Inclination', object_class.inclination, 8, incl_[0], incl_[1]),
        ('Longitude of Asc. node', object_class.longitude_of_ascending_node, 9, long_[0], long_[1]),
        ('Argument of peri.', object_class.argument_of_perihelion, 10, peri_[0], peri_[1]),
        ('Axial Tilt', object_class.axial_tilt, 11, tilt_[0], tilt_[1]),
    ]

    for text, value, row, options, default in parameters:
        tk_functions.place_object_properties(
            window=planet_window, function=utilities.convert,
            text=text, value=value, row=row, column=0,
            options=options, default=default
        )


def show_observational_parameters(window, object_name, object_class):
    """
    Display the observational parameters of a celestial object.

    Parameters
    ----------
    window : Union[tk.Tk, tk.Toplevel, tk.Frame]
        Parent widget for displaying parameters.
    object_name : str
        Name of the celestial object.
    object_class : Any
        Celestial object class containing the data.

    """
    _clear_window(window)
    object_class = object_class.ObservationalParameters()
    planet_window = window

    _setup_column_weights(planet_window)
    _create_header_labels(planet_window, 'Observational')

    # Equivalencies button
    tk_functions.object_button(
        window=planet_window,
        function=lambda: tk_functions.place_equivalencies(
            window=planet_window, cel_object=object_class,
            equiv_type='observation', column=4
        ),
        text='Equivalences', row=0, column=4, sticky='nsew', width=25
    )

    # Get dynamic options
    dist_ = utilities.get_options(object_class.distance_from_earth, 'dist')
    size_ = utilities.get_options(object_class.average_angular_size, 'size')

    # Observational parameters
    parameters = [
        ('Mean Apparent Magnitude', object_class.apparent_magnitude, 1, tuple(), ''),
        ('Geometric Albedo', object_class.geom_albedo, 2, tuple(), ''),
        ('Distance from Earth', object_class.distance_from_earth, 3, dist_[0], dist_[1]),
        ('Absolute Magnitude', object_class.absolute_magnitude, 4, tuple(), ''),
        ('Mean angular size', object_class.average_angular_size, 5, size_[0], size_[1]),
    ]

    for text, value, row, options, default in parameters:
        tk_functions.place_object_properties(
            window=planet_window, function=utilities.convert,
            text=text, value=value, row=row, column=0,
            options=options, default=default
        )

    # Information label
    if object_name not in STAR_LIST:
        if object_name in PLANET_LIST:
            info_text = "Distance from Earth for the planet is calculated as the planets' distance from Sun in AU - 1 AU."
        elif object_name in MOON_LIST and object_name != 'Moon':
            info_text = 'Distance from Earth to {} is taken as the distance from Earth to the parent planet, e.g, {}.'.format(
                object_name, PLANET_MOON.get(object_name, 'Unknown')
            )
        else:
            info_text = ''

        if info_text:
            tk_functions.label_placement(
                window=planet_window, text=info_text,
                row=20, columnspan=10, pad_y=10, sticky='news'
            )
