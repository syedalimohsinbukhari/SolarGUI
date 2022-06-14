"""
Created on Jun 12 12:13:02 2022
"""

from astropy.units import Quantity

SOL_MASS = Quantity(1, 'M_sun').si
SOL_RADIUS = Quantity(1, 'R_sun').to('km')

EARTH_MASS = Quantity(1, 'M_earth').si
EARTH_RADIUS = Quantity(1, 'R_sun').to('km')

SOL_EARTH_PERIOD = Quantity(1, 'yr').to('day')
SOL_EARTH_DISTANCE = Quantity(1, 'AU').to('km')

JUPITER_MASS = Quantity(1, 'M_jupiter').si
JUPITER_RADIUS = Quantity(1, 'R_jupiter').to('km')
