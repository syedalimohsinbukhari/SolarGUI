"""
Created on Jun 12 12:12:36 2022
"""

try:
    from .cel__CONSTANTS import SOL_EARTH_DISTANCE
    from .cel__object import c_, c_phy, c_orb, c_obs
    from .cel__planets import Jupiter, Mars, Saturn, Uranus, Neptune
    from .cel__others import Pluto
    from . import utilities as utils
except ImportError:
    from cel__CONSTANTS import SOL_EARTH_DISTANCE
    from cel__object import c_, c_phy, c_orb, c_obs
    from cel__planets import Jupiter, Mars, Saturn, Uranus, Neptune
    from cel__others import Pluto
    import utilities as utils

m_ = Mars().ObservationalParameters().distance_from_earth
j_ = Jupiter().ObservationalParameters().distance_from_earth
s_ = Saturn().ObservationalParameters().distance_from_earth
u_ = Uranus().ObservationalParameters().distance_from_earth
n_ = Neptune().ObservationalParameters().distance_from_earth
p_ = Pluto().ObservationalParameters().distance_from_earth


class Moon(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = utils.Q(4.53, 'Gyr')
            self.mass = utils.Q(7.342e22, 'kg')
            self.radius = utils.Q(1737.4, 'km')

            super(Moon().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(384399, 'km').to('AU')
            self.eccentricity = 0.0549

            super(
                    Moon().OrbitalParameters, self
                    ).__init__(a_0=self.semi_major_axis, ecc=self.eccentricity,
                               orbital_period=27.321661, av_orbital_speed=1.022,
                               mean_anom=135.27, inclination=5.145, long_asc=125.08,
                               arg_peri=318.15, axial_tilt=1.5427)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = utils.Q(29.3, 'arcmin'), utils.Q(34.1, 'arcmin')

            d_ = 0.00256955529 * SOL_EARTH_DISTANCE

            super(Moon().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                 ap_mag_min=-2.5,
                                                                 ap_mag_max=-12.9,
                                                                 geom_albedo=0.136,
                                                                 ang_min=ang_min,
                                                                 ang_max=ang_max)


class Phobos(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(1.0658e16, 'kg')
            self.radius = utils.Q(11.2667, 'km')

            super(Phobos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(9367, 'km').to('AU')
            self.eccentricity = 0.0151

            super(Phobos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=0.31891032,
                                                             av_orbital_speed=2.138,
                                                             inclination=1.093,
                                                             axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = utils.Q(0.14, 'deg'), utils.Q(0.20, 'deg')

            super(Phobos().ObservationalParameters, self).__init__(dist_from_earth=m_,
                                                                   apparent_mag=11.8,
                                                                   geom_albedo=0.071,
                                                                   ang_min=ang_min,
                                                                   ang_max=ang_max)


class Deimos(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(1.4762e15, 'kg')
            self.radius = utils.Q(6.2, 'km')

            super(Deimos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(23463.2, 'km').to('AU')
            self.eccentricity = 0.00033

            super(Deimos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=1.263,
                                                             av_orbital_speed=1.3513,
                                                             inclination=0.92)

    class ObservationalParameters(c_obs):

        def __init__(self):
            av_ = utils.Q(2.5, 'arcmin')

            super(Deimos().ObservationalParameters, self).__init__(dist_from_earth=m_,
                                                                   apparent_mag=12.89,
                                                                   geom_albedo=0.068,
                                                                   av_ang_size=av_)


class Io(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(8.931938, 'kg')
            self.radius = utils.Q(1821.6, 'km')

            super(Io.PhysicalParameters, self).__init__(mass=self.mass,
                                                        radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(421700, 'km').to('AU')
            self.eccentricity = 0.0041

            super(Io().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                         ecc=self.eccentricity,
                                                         orbital_period=1.769137786,
                                                         av_orbital_speed=17.334,
                                                         inclination=0.05)

    class ObservationalParameters(c_obs):

        def __init__(self):
            av_ = utils.Q(1.2, 'arcsec')

            super(Io().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                               apparent_mag=5.02,
                                                               geom_albedo=0.63,
                                                               av_ang_size=av_)


class Europa(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(4.799844e22, 'kg')
            self.radius = utils.Q(1560.8, 'km')

            super(Europa().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(670900, 'km')
            self.eccentricity = 0.009

            super(Europa().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=3.551181,
                                                             av_orbital_speed=13.74336,
                                                             inclination=0.470,
                                                             axial_tilt=0.1)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Europa().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                   apparent_mag=5.29,
                                                                   geom_albedo=0.67)


class Ganymede(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(1.4819e25, 'kg')
            self.radius = utils.Q(2634.1, 'km')

            super(Ganymede().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(1070400, 'km').to('AU')
            self.eccentricity = 0.0013

            super(Ganymede().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=7.15455296,
                                                               av_orbital_speed=10.880,
                                                               inclination=2.214,
                                                               axial_tilt=0.165)

    class ObservationalParameters(c_obs):

        def __init__(self):
            ang_min, ang_max = utils.Q(1.2, 'arcsec'), utils.Q(1.8, 'arcsec')

            super(Ganymede().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                     apparent_mag=4.61,
                                                                     geom_albedo=0.43,
                                                                     ang_min=ang_min,
                                                                     ang_max=ang_max)


class Callisto(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(1.075938e23, 'kg')
            self.radius = utils.Q(2410.3, 'km')

            super(Callisto().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(1882700, 'km')
            self.eccentricity = 0.0074

            super(Callisto().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=16.6890184,
                                                               av_orbital_speed=8.204,
                                                               inclination=2.017,
                                                               axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Callisto().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                     apparent_mag=5.65,
                                                                     geom_albedo=0.22)


class Metis(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(3.6e16, 'kg')
            self.radius = utils.Q(21.5, 'km')

            super(Metis().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(128000, 'km').to('AU')
            self.eccentricity = 0.0002

            super(Metis().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.294780,
                                                            av_orbital_speed=31.501,
                                                            inclination=0.06,
                                                            axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Metis().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                  geom_albedo=0.061)


class Adrastea(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(2e15, 'kg')
            self.radius = utils.Q(8.2, 'km')

            super(Adrastea().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(129000, 'km')
            self.eccentricity = 0.0015

            super(Adrastea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=0.29826,
                                                               av_orbital_speed=31.378,
                                                               inclination=0.03,
                                                               axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Adrastea().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                     geom_albedo=0.1)


class Amalthea(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(2.08e18, 'kg')
            self.radius = utils.Q(83.5, 'km')

            super(Amalthea().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(181365.84, 'km').to('AU')
            self.eccentricity = 0.00319

            super(Amalthea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=0.49817943,
                                                               av_orbital_speed=26.57,
                                                               inclination=0.374,
                                                               axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Amalthea().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                     apparent_mag=14.1,
                                                                     geom_albedo=0.09)


class Thebe(c_):

    class PhysicalParameters(c_phy):

        def __init__(self):
            self.age = None
            self.mass = utils.Q(4.3e17, 'kg')
            self.radius = utils.Q(49.3, 'km')

            super(Thebe().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(c_orb):

        def __init__(self):
            self.semi_major_axis = utils.Q(221889.0, 'km').to('AU')
            self.eccentricity = 0.0175

            super(Thebe().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.674536,
                                                            av_orbital_speed=23.92,
                                                            inclination=1.076,
                                                            axial_tilt=0)

    class ObservationalParameters(c_obs):

        def __init__(self):
            super(Thebe().ObservationalParameters, self).__init__(dist_from_earth=j_,
                                                                  geom_albedo=0.047)
