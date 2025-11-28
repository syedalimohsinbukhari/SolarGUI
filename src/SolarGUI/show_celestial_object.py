"""
Created on May 24 22:12:45 2022
"""

import PySimpleGUI as sg
import numpy as np
from typing import Any

from . import utilities

star_list = ['Sun']

planet_list = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune',
               'Pluto']

moon_list = ['Moon',
             'Phobos', 'Deimos',
             'Io', 'Europa', 'Ganymede', 'Callisto', 'Metis', 'Adrastea', 'Amalthea',
             'Thebe',
             'Mimas', 'Enceladus', 'Tethys', 'Dione', 'Rhea', 'Titan', 'Hyperion',
             'Iapetus',
             'Miranda', 'Umbrial', 'Ariel', 'Titania', 'Oberon',
             'Naiad', 'Thalassa', 'Despina', 'Galatea', 'Larissa', 'Hippocamp', 'Proteus',
             'Triton',
             'Charon']

planet_moon = {'Moon': 'Earth',
               'Phobos': 'Mars',
               'Deimos': 'Mars',
               'Io': 'Jupiter',
               'Europa': 'Jupiter',
               'Ganymede': 'Jupiter',
               'Callisto': 'Jupiter',
               'Metis': 'Jupiter',
               'Adrastea': 'Jupiter',
               'Amalthea': 'Jupiter',
               'Thebe': 'Jupiter',
               'Mimas': 'Saturn',
               'Enceladus': 'Saturn',
               'Tethys': 'Saturn',
               'Dione': 'Saturn',
               'Rhea': 'Saturn',
               'Titan': 'Saturn',
               'Hyperion': 'Saturn',
               'Iapetus': 'Saturn',
               'Miranda': 'Uranus',
               'Umbrial': 'Uranus',
               'Ariel': 'Uranus',
               'Titania': 'Uranus',
               'Oberon': 'Uranus',
               'Naiad': 'Neptune',
               'Thalassa': 'Neptune',
               'Despina': 'Neptune',
               'Galatea': 'Neptune',
               'Larissa': 'Neptune',
               'Hippocamp': 'Neptune',
               'Proteus': 'Neptune',
               'Triton': 'Neptune',
               'Charon': 'Pluto'}


def show_parameter_selection(object_name: str, object_class: Any):
    """
    Show parameter selection window for a celestial object.
    
    Parameters
    ----------
    object_name : str
        Name of the celestial object.
    object_class : Any
        The python class for the celestial object.
    """
    # Build buttons based on object type
    buttons = [sg.Button('Physical Parameters', key='PHYSICAL')]
    
    if object_name != 'Sun':
        buttons.append(sg.Button('Orbital Parameters', key='ORBITAL'))
    
    if object_name != 'Earth':
        buttons.append(sg.Button('Observational Parameters', key='OBSERVATIONAL'))
    
    layout = [
        buttons,
        [sg.HorizontalSeparator()],
        [sg.Column([], key='PARAMS_COLUMN', expand_x=True, expand_y=True, scrollable=True, vertical_scroll_only=True)]
    ]
    
    window = sg.Window(object_name, layout, size=(1024, 648), resizable=True, finalize=True)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            break
        elif event == 'PHYSICAL':
            _update_physical_params(window, object_class)
        elif event == 'ORBITAL':
            _update_orbital_params(window, object_name, object_class)
        elif event == 'OBSERVATIONAL':
            _update_observational_params(window, object_name, object_class)
        elif event and event.startswith('UNIT_'):
            _handle_unit_change(window, event, values, object_class)
        elif event and event.startswith('RESET_'):
            _handle_reset(window, event, object_class)
    
    window.close()


def _update_physical_params(window, object_class):
    """Update the window with physical parameters."""
    obj = object_class.PhysicalParameters()
    
    # Age options
    if obj.age is None:
        age_opt = []
        age_def = ''
    else:
        age_opt = ['s', 'yr', 'Myr', 'Gyr']
        age_def = 'Gyr'
    
    params = [
        ('Age', obj.age, age_opt, age_def),
        ('Mass', obj.mass, ['g', 'kg', 'M_earth', 'M_jupiter', 'M_sun'], 'kg'),
        ('Radius', obj.radius, ['cm', 'm', 'km', 'R_earth', 'R_jupiter', 'R_sun'], 'km'),
        ('Volume', obj.volume, ['cm^3', 'm^3', 'km^3'], 'km^3'),
        ('Density', obj.density, ['g/cm^3', 'kg/cm^3', 'kg/m^3'], 'g/cm^3'),
        ('Surface area', obj.surface_area, ['cm^2', 'm^2', 'km^2'], 'km^2'),
        ('Surface gravity', obj.surface_gravity, ['cm/s^2', 'm/s^2', 'km/s^2'], 'm/s^2'),
        ('Escape velocity', obj.escape_velocity, ['cm/s', 'm/s', 'km/s', 'km/h'], 'km/s'),
    ]
    
    _create_params_layout(window, params, 'Physical Parameters')


def _update_orbital_params(window, object_name, object_class):
    """Update the window with orbital parameters."""
    obj = object_class.OrbitalParameters()
    
    t_orb_ = utilities.get_options(obj.orbital_period, 't_orb')
    v_orb_ = utilities.get_options(obj.av_orbital_speed, 'v_orb')
    anom_ = utilities.get_options(obj.mean_anomaly, 'm_anom')
    incl_ = utilities.get_options(obj.inclination, 'incl')
    long_ = utilities.get_options(obj.longitude_of_ascending_node, 'long')
    peri_ = utilities.get_options(obj.argument_of_perihelion, 'arg')
    tilt_ = utilities.get_options(obj.axial_tilt, 'tilt')
    
    dist_opts = ['cm', 'm', 'km', 'Gm', 'AU', 'lyr', 'pc']
    
    params = [
        ('Semi Major Axis', obj.semi_major_axis, dist_opts, 'AU'),
        ('Eccentricity', obj.eccentricity, [], ''),
        ('Closest approach', obj.apo, dist_opts, 'AU'),
        ('Farthest approach', obj.peri, dist_opts, 'AU'),
        ('Orbital Period', obj.orbital_period, list(t_orb_[0]), t_orb_[1]),
        ('Av. Orbital Speed', obj.av_orbital_speed, list(v_orb_[0]), v_orb_[1]),
        ('Mean anomaly', obj.mean_anomaly, list(anom_[0]), anom_[1]),
        ('Inclination', obj.inclination, list(incl_[0]), incl_[1]),
        ('Longitude of Asc. node', obj.longitude_of_ascending_node, list(long_[0]), long_[1]),
        ('Argument of peri.', obj.argument_of_perihelion, list(peri_[0]), peri_[1]),
        ('Axial Tilt', obj.axial_tilt, list(tilt_[0]), tilt_[1]),
    ]
    
    note = ''
    if object_name in planet_moon.keys():
        note = 'The orbital parameters are given with respect to the planet {}.'.format(planet_moon[object_name])
    
    _create_params_layout(window, params, 'Orbital Parameters', note)


def _update_observational_params(window, object_name, object_class):
    """Update the window with observational parameters."""
    obj = object_class.ObservationalParameters()
    
    dist_ = utilities.get_options(obj.distance_from_earth, 'dist')
    size_ = utilities.get_options(obj.average_angular_size, 'size')
    
    params = [
        ('Mean Apparent Magnitude', obj.apparent_magnitude, [], ''),
        ('Geometric Albedo', obj.geom_albedo, [], ''),
        ('Distance from Earth', obj.distance_from_earth, list(dist_[0]), dist_[1]),
        ('Absolute Magnitude', obj.absolute_magnitude, [], ''),
        ('Mean angular size', obj.average_angular_size, list(size_[0]), size_[1]),
    ]
    
    # Add note based on object type
    note = ''
    if object_name not in star_list:
        if object_name in planet_list:
            note = "Distance from Earth for the planet is calculated as the planets' distance from Sun in AU - 1 AU."
        elif object_name in moon_list and object_name != 'Moon':
            note = 'Distance from Earth to {} is taken as the distance from Earth to the parent planet, e.g, {}.'.format(object_name, planet_moon[object_name])
    
    _create_params_layout(window, params, 'Observational Parameters', note)


def _create_params_layout(window, params, title, note=''):
    """Create parameter display layout."""
    layout = [
        [sg.Text(title, font=('Helvetica', 12, 'bold'))],
        [sg.Text('Parameter', size=(20, 1)), sg.Text('Value', size=(30, 1)), 
         sg.Text('Unit', size=(15, 1)), sg.Text('', size=(8, 1))],
        [sg.HorizontalSeparator()]
    ]
    
    for i, (name, value, options, default) in enumerate(params):
        val_str = str(value) if value is not None else 'N/A'
        disabled = len(options) == 0
        
        row = [
            sg.Text(name, size=(20, 1)),
            sg.Input(val_str, key='VAL_{}'.format(i), size=(30, 1), disabled=True),
            sg.Combo(options, key='UNIT_{}'.format(i), size=(12, 1), enable_events=True, disabled=disabled),
            sg.Button('Reset', key='RESET_{}'.format(i), disabled=disabled)
        ]
        layout.append(row)
    
    if note:
        layout.append([sg.HorizontalSeparator()])
        layout.append([sg.Text(note, size=(80, 2))])
    
    # Update the column in the window
    window['PARAMS_COLUMN'].update(visible=False)
    window.extend_layout(window['PARAMS_COLUMN'], layout)
    window['PARAMS_COLUMN'].update(visible=True)


def _handle_unit_change(window, event, values, object_class):
    """Handle unit conversion when dropdown changes."""
    # Note: Unit conversion is complex as it requires tracking original values.
    # For this simple PySimpleGUI port, unit changes just update the dropdown.
    # Full unit conversion functionality would require storing original Quantity objects.
    pass


def _handle_reset(window, event, object_class):
    """Handle reset button click."""
    # For now, just clear the unit dropdown
    idx = int(event.split('_')[1])
    unit_key = 'UNIT_{}'.format(idx)
    window[unit_key].update('')


# Keep old class for backwards compatibility (deprecated)
class GetParameterSelection:
    """
    Deprecated: Use show_parameter_selection() function instead.
    """
    def __init__(self, window, object_name: str, object_class: Any):
        show_parameter_selection(object_name, object_class)
