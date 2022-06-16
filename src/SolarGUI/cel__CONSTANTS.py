"""
Created on Jun 12 12:13:02 2022
"""

try:
    from utilities import Q
except ImportError:
    from .utilities import Q

SOL_MASS = Q(1, 'M_sun').si
SOL_RADIUS = Q(1, 'R_sun').to('km')

EARTH_MASS = Q(1, 'M_earth').si
EARTH_RADIUS = Q(1, 'R_sun').to('km')

SOL_EARTH_PERIOD = Q(1, 'yr').to('day')
SOL_EARTH_DISTANCE = Q(1, 'AU').to('km')

JUPITER_MASS = Q(1, 'M_jupiter').si
JUPITER_RADIUS = Q(1, 'R_jupiter').to('km')
