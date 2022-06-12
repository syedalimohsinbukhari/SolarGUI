"""
Created on Jun 12 12:13:02 2022
"""

import astropy.units as u

SOL_MASS = (1 * u.M_sun).si
SOL_RADIUS = (1 * u.R_sun).to(u.km)

EARTH_MASS = (1 * u.M_earth).si
EARTH_RADIUS = (1 * u.R_earth).to(u.km)

SOL_EARTH_PERIOD = (1 * u.yr).to(u.day)
SOL_EARTH_DISTANCE = (1 * u.AU).to(u.km)

JUPITER_MASS = (1 * u.M_jupiter).si
JUPITER_RADIUS = (1 * u.R_jupiter).to(u.km)
