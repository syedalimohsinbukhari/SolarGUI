"""
Created on Jun 12 12:13:02 2022
"""

from . import utilities as utils

SOL_MASS = utils.Q(1, 'M_sun').si
SOL_RADIUS = utils.Q(1, 'R_sun').to('km')

EARTH_MASS = utils.Q(1, 'M_earth').si
EARTH_RADIUS = utils.Q(1, 'R_sun').to('km')

SOL_EARTH_PERIOD = utils.Q(1, 'yr').to('day')
SOL_EARTH_DISTANCE = utils.Q(1, 'AU').to('km')

JUPITER_MASS = utils.Q(1, 'M_jupiter').si
JUPITER_RADIUS = utils.Q(1, 'R_jupiter').to('km')
