"""
Created on May 22 00:40:38 2022
"""

import sys
import PySimpleGUI as sg

from . import moons, others, planets, stars
from . import show_celestial_object as sco


class Main:

    def __init__(self):
        # Define celestial objects data
        self.stars_data = [('Sun', stars.Sun)]
        
        self.planets_data = [
            ('Mercury', planets.Mercury), ('Venus', planets.Venus),
            ('Earth', planets.Earth), ('Mars', planets.Mars),
            ('Jupiter', planets.Jupiter), ('Saturn', planets.Saturn),
            ('Uranus', planets.Uranus), ('Neptune', planets.Neptune)
        ]
        
        self.moons_data = {
            'Earth': [('Moon', moons.Moon)],
            'Mars': [('Phobos', moons.Phobos), ('Deimos', moons.Deimos)],
            'Jupiter': [
                ('Io', moons.Io), ('Europa', moons.Europa),
                ('Ganymede', moons.Ganymede), ('Callisto', moons.Callisto),
                ('Metis', moons.Metis), ('Adrastea', moons.Adrastea),
                ('Amalthea', moons.Amalthea), ('Thebe', moons.Thebe)
            ],
            'Saturn': [
                ('Mimas', moons.Mimas), ('Enceladus', moons.Enceladus),
                ('Tethys', moons.Tethys), ('Dione', moons.Dione),
                ('Rhea', moons.Rhea), ('Titan', moons.Titan),
                ('Hyperion', moons.Hyperion), ('Iapetus', moons.Iapetus)
            ],
            'Uranus': [
                ('Miranda', moons.Miranda), ('Umbriel', moons.Umbriel),
                ('Ariel', moons.Ariel), ('Titania', moons.Titania),
                ('Oberon', moons.Oberon)
            ],
            'Neptune': [
                ('Naiad', moons.Naiad), ('Thalassa', moons.Thalassa),
                ('Despina', moons.Despina), ('Galatea', moons.Galatea),
                ('Larissa', moons.Larissa), ('Hippocamp', moons.Hippocamp),
                ('Proteus', moons.Proteus), ('Triton', moons.Triton)
            ],
            'Pluto': [('Charon', moons.Charon)]
        }
        
        self.others_data = [('Pluto', others.Pluto)]
        
        # Build the layout
        layout = self._build_layout()
        
        # Create the window
        self.window = sg.Window('SolarGUI', layout, size=(1024, 648), resizable=True, finalize=True)
        
        # Event loop
        self._run_event_loop()

    def _build_layout(self):
        """Build the main window layout."""
        # Stars section
        stars_buttons = [sg.Button(name, key=f'STAR_{name}') for name, _ in self.stars_data]
        
        # Planets section
        planets_buttons = [sg.Button(name, key=f'PLANET_{name}') for name, _ in self.planets_data]
        
        # Moons section - organized by parent planet
        moons_rows = []
        for planet, moon_list in self.moons_data.items():
            row = [sg.Text(f'{planet}:', size=(8, 1))]
            row.extend([sg.Button(name, key=f'MOON_{name}') for name, _ in moon_list])
            moons_rows.append(row)
        
        # Others section
        others_buttons = [sg.Button(name, key=f'OTHER_{name}') for name, _ in self.others_data]
        
        layout = [
            [sg.Text('Welcome to Solar Explorer. Please select a button.', justification='center', expand_x=True)],
            [sg.HorizontalSeparator()],
            [sg.Text('Stars', font=('Helvetica', 10, 'bold'))],
            stars_buttons,
            [sg.HorizontalSeparator()],
            [sg.Text('Planets', font=('Helvetica', 10, 'bold'))],
            planets_buttons,
            [sg.HorizontalSeparator()],
            [sg.Text('Moons', font=('Helvetica', 10, 'bold'))],
        ]
        
        # Add moon rows
        for row in moons_rows:
            layout.append(row)
        
        layout.extend([
            [sg.HorizontalSeparator()],
            [sg.Text('Others', font=('Helvetica', 10, 'bold'))],
            others_buttons
        ])
        
        return layout

    def _get_object_class(self, key):
        """Get the object class from a button key."""
        if key.startswith('STAR_'):
            name = key[5:]
            for obj_name, obj_class in self.stars_data:
                if obj_name == name:
                    return name, obj_class
        elif key.startswith('PLANET_'):
            name = key[7:]
            for obj_name, obj_class in self.planets_data:
                if obj_name == name:
                    return name, obj_class
        elif key.startswith('MOON_'):
            name = key[5:]
            for planet_moons in self.moons_data.values():
                for obj_name, obj_class in planet_moons:
                    if obj_name == name:
                        return name, obj_class
        elif key.startswith('OTHER_'):
            name = key[6:]
            for obj_name, obj_class in self.others_data:
                if obj_name == name:
                    return name, obj_class
        return None, None

    def _run_event_loop(self):
        """Run the main event loop."""
        while True:
            event, values = self.window.read()
            
            if event == sg.WIN_CLOSED:
                break
            
            # Handle celestial object button clicks
            if event and (event.startswith('STAR_') or event.startswith('PLANET_') or 
                         event.startswith('MOON_') or event.startswith('OTHER_')):
                obj_name, obj_class = self._get_object_class(event)
                if obj_class:
                    sco.show_parameter_selection(obj_name, obj_class)
        
        self.window.close()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/

if __name__ == '__main__':
    try:
        sys.exit(Main())
    except TypeError:
        pass
