"""
Created on May 22 00:40:38 2022

SolarGUI - A Solar System Explorer Application

This module provides the main GUI interface for exploring celestial objects
in our solar system including stars, planets, moons, and dwarf planets.
"""

import sys
import tkinter as tk
from tkinter import ttk

from . import moons, others, planets, stars
from . import show_celestial_object as sco
from . import tk_functions as tk_f


# Modern color scheme
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

# Celestial object definitions for cleaner data management
STARS = [
    ('Sun', stars.Sun),
]

PLANETS = [
    ('Mercury', planets.Mercury),
    ('Venus', planets.Venus),
    ('Earth', planets.Earth),
    ('Mars', planets.Mars),
    ('Jupiter', planets.Jupiter),
    ('Saturn', planets.Saturn),
    ('Uranus', planets.Uranus),
    ('Neptune', planets.Neptune),
]

MOONS_BY_PLANET = {
    'Earth': [('Moon', moons.Moon)],
    'Mars': [('Phobos', moons.Phobos), ('Deimos', moons.Deimos)],
    'Jupiter': [
        ('Io', moons.Io), ('Europa', moons.Europa), ('Ganymede', moons.Ganymede),
        ('Callisto', moons.Callisto), ('Metis', moons.Metis), ('Adrastea', moons.Adrastea),
        ('Amalthea', moons.Amalthea), ('Thebe', moons.Thebe),
    ],
    'Saturn': [
        ('Mimas', moons.Mimas), ('Enceladus', moons.Enceladus), ('Tethys', moons.Tethys),
        ('Dione', moons.Dione), ('Rhea', moons.Rhea), ('Titan', moons.Titan),
        ('Hyperion', moons.Hyperion), ('Iapetus', moons.Iapetus),
    ],
    'Uranus': [
        ('Miranda', moons.Miranda), ('Umbriel', moons.Umbriel), ('Ariel', moons.Ariel),
        ('Titania', moons.Titania), ('Oberon', moons.Oberon),
    ],
    'Neptune': [
        ('Naiad', moons.Naiad), ('Thalassa', moons.Thalassa), ('Despina', moons.Despina),
        ('Galatea', moons.Galatea), ('Larissa', moons.Larissa), ('Hippocamp', moons.Hippocamp),
        ('Proteus', moons.Proteus), ('Triton', moons.Triton),
    ],
    'Pluto': [('Charon', moons.Charon)],
}

OTHERS = [
    ('Pluto', others.Pluto),
]


class Main:
    """Main application class for the Solar System Explorer GUI."""

    def __init__(self):
        """Initialize the main application window and UI components."""
        self.width = 1024
        self.height = 700
        self.root_window = tk.Tk()

        self._setup_window()
        self._setup_styles()
        self._create_main_container()
        self._create_header()
        self._create_content_sections()

        self.root_window.mainloop()

    def _setup_window(self):
        """Configure the main application window."""
        self.root_window.geometry('{w}x{h}'.format(w=self.width, h=self.height))
        self.root_window.minsize(self.width, self.height)
        self.root_window.title('SolarGUI - Solar System Explorer')
        self.root_window.configure(bg=COLORS['bg_dark'])

    def _setup_styles(self):
        """Configure ttk styles for a modern appearance."""
        style = ttk.Style()

        # Try to use a modern theme if available
        available_themes = style.theme_names()
        if 'clam' in available_themes:
            style.theme_use('clam')

        # Configure custom styles
        style.configure('Title.TLabel',
                        font=('Helvetica', 24, 'bold'),
                        background=COLORS['bg_dark'],
                        foreground=COLORS['text_light'])

        style.configure('Section.TLabel',
                        font=('Helvetica', 14, 'bold'),
                        background=COLORS['bg_medium'],
                        foreground=COLORS['accent'])

        style.configure('Planet.TLabel',
                        font=('Helvetica', 10),
                        background=COLORS['bg_medium'],
                        foreground=COLORS['text_muted'])

        style.configure('Custom.TFrame',
                        background=COLORS['bg_dark'])

        style.configure('Section.TFrame',
                        background=COLORS['bg_medium'])

        style.configure('Horizontal.TSeparator',
                        background=COLORS['accent'])

    def _create_main_container(self):
        """Create the main scrollable container."""
        # Main container frame
        self.main_container = ttk.Frame(self.root_window, style='Custom.TFrame')
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def _create_header(self):
        """Create the application header with title."""
        header_frame = ttk.Frame(self.main_container, style='Custom.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))

        title_label = ttk.Label(
            header_frame,
            text='\u2600 Solar System Explorer',
            style='Title.TLabel'
        )
        title_label.pack(pady=10)

        subtitle_label = tk.Label(
            header_frame,
            text='Explore the celestial objects in our solar system',
            font=('Helvetica', 11),
            bg=COLORS['bg_dark'],
            fg=COLORS['text_muted']
        )
        subtitle_label.pack()

    def _create_content_sections(self):
        """Create all content sections for celestial objects."""
        self._create_section('Stars', STARS, self._create_object_buttons)
        self._create_section('Planets', PLANETS, self._create_object_buttons)
        self._create_section('Moons', MOONS_BY_PLANET, self._create_moon_buttons)
        self._create_section('Dwarf Planets & Others', OTHERS, self._create_object_buttons)

    def _create_section(self, title, data, button_creator):
        """Create a section with a title and content.

        Parameters
        ----------
        title : str
            Section title
        data : list or dict
            Data for creating buttons
        button_creator : callable
            Function to create buttons for this section

        """
        # Section frame
        section_frame = ttk.Frame(self.main_container, style='Section.TFrame')
        section_frame.pack(fill=tk.X, pady=5)

        # Section header
        header = ttk.Label(section_frame, text=title, style='Section.TLabel')
        header.pack(anchor=tk.W, padx=15, pady=(10, 5))

        # Content frame for buttons
        content_frame = tk.Frame(section_frame, bg=COLORS['bg_medium'])
        content_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

        # Create buttons
        button_creator(content_frame, data)

        # Separator
        sep = ttk.Separator(self.main_container, orient='horizontal')
        sep.pack(fill=tk.X, pady=5)

    def _create_object_buttons(self, parent, objects):
        """Create buttons for a list of celestial objects.

        Parameters
        ----------
        parent : tk.Frame
            Parent frame for the buttons
        objects : list
            List of tuples (name, class) for celestial objects

        """
        for i in range(10):
            parent.grid_columnconfigure(i, weight=1)

        for col, (name, obj_class) in enumerate(objects):
            self._create_styled_button(parent, name, obj_class, row=0, column=col)

    def _create_moon_buttons(self, parent, moons_dict):
        """Create buttons for moons organized by parent planet.

        Parameters
        ----------
        parent : tk.Frame
            Parent frame for the buttons
        moons_dict : dict
            Dictionary mapping planet names to lists of moon tuples

        """
        for i in range(10):
            parent.grid_columnconfigure(i, weight=1)

        row = 0
        for planet_name, moon_list in moons_dict.items():
            # Planet label
            planet_label = tk.Label(
                parent,
                text='{planet}:'.format(planet=planet_name),
                font=('Helvetica', 9, 'bold'),
                bg=COLORS['bg_medium'],
                fg=COLORS['text_muted'],
                width=8,
                anchor='e'
            )
            planet_label.grid(row=row, column=0, sticky='e', padx=(0, 5), pady=3)

            # Moon buttons
            for col, (moon_name, moon_class) in enumerate(moon_list, start=1):
                self._create_styled_button(parent, moon_name, moon_class, row=row, column=col)

            row += 1

    def _create_styled_button(self, parent, name, obj_class, row, column):
        """Create a styled button for a celestial object.

        Parameters
        ----------
        parent : tk.Frame
            Parent frame for the button
        name : str
            Display name for the button
        obj_class : class
            Celestial object class to open on click
        row : int
            Grid row position
        column : int
            Grid column position

        """
        btn = tk.Button(
            parent,
            text=name,
            font=('Helvetica', 9),
            bg=COLORS['button_bg'],
            fg=COLORS['text_light'],
            activebackground=COLORS['button_hover'],
            activeforeground=COLORS['text_light'],
            relief=tk.FLAT,
            cursor='hand2',
            width=10,
            command=lambda n=name, c=obj_class: sco.GetParameterSelection(
                window=self.root_window,
                object_name=n,
                object_class=c
            )
        )
        btn.grid(row=row, column=column, padx=3, pady=3, sticky='ew')

        # Hover effects
        btn.bind('<Enter>', lambda e, b=btn: b.configure(bg=COLORS['button_hover']))
        btn.bind('<Leave>', lambda e, b=btn: b.configure(bg=COLORS['button_bg']))


# Entry point for the application
# Reference: https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
