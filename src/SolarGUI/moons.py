"""
Created on Jun 12 12:12:36 2022
"""

from . import CONSTANTS, _CelestialObject, others, planets, utilities

m_ = planets.Mars().ObservationalParameters().distance_from_earth
j_ = planets.Jupiter().ObservationalParameters().distance_from_earth
s_ = planets.Saturn().ObservationalParameters().distance_from_earth
u_ = planets.Uranus().ObservationalParameters().distance_from_earth
n_ = planets.Neptune().ObservationalParameters().distance_from_earth
p_ = others.Pluto().ObservationalParameters().distance_from_earth


class Moon(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = utilities.Q(4.53, 'Gyr')
            self.mass = utilities.Q(7.342e22, 'kg')
            self.radius = utilities.Q(1737.4, 'km')

            super(Moon().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(384399, 'km').to('AU')
            self.eccentricity = 0.0549

            super(Moon().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                           ecc=self.eccentricity,
                                                           orbital_period=27.321661,
                                                           av_orbital_speed=1.022,
                                                           mean_anom=135.27,
                                                           inclination=5.145,
                                                           long_asc=125.08,
                                                           arg_peri=318.15,
                                                           axial_tilt=1.5427)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            ang_min, ang_max = utilities.Q(29.3, 'arcmin'), utilities.Q(34.1, 'arcmin')

            d_ = 0.00256955529 * CONSTANTS.SOL_EARTH_DISTANCE

            super(Moon().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                 ap_mag_min=-2.5,
                                                                 ap_mag_max=-12.9,
                                                                 geom_albedo=0.136,
                                                                 ang_min=ang_min,
                                                                 ang_max=ang_max)


class Phobos(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.0658e16, 'kg')
            self.radius = utilities.Q(11.2667, 'km')

            super(Phobos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(9367, 'km').to('AU')
            self.eccentricity = 0.0151

            super(Phobos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=0.31891032,
                                                             av_orbital_speed=2.138,
                                                             inclination=1.093,
                                                             axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            ang_min, ang_max = utilities.Q(0.14, 'deg'), utilities.Q(0.20, 'deg')

            d_ = m_ - Phobos().OrbitalParameters().semi_major_axis

            super(Phobos().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=11.8,
                                                                   geom_albedo=0.071,
                                                                   ang_min=ang_min,
                                                                   ang_max=ang_max)


class Deimos(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.4762e15, 'kg')
            self.radius = utilities.Q(6.2, 'km')

            super(Deimos().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(23463.2, 'km').to('AU')
            self.eccentricity = 0.00033

            super(Deimos().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=1.263,
                                                             av_orbital_speed=1.3513,
                                                             inclination=0.92)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            av_ = utilities.Q(2.5, 'arcmin').to('arcsec')

            d_ = m_ - Deimos().OrbitalParameters().semi_major_axis

            super(Deimos().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=12.89,
                                                                   geom_albedo=0.068,
                                                                   av_ang_size=av_)


class Io(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(8.931938, 'kg')
            self.radius = utilities.Q(1821.6, 'km')

            super(Io.PhysicalParameters, self).__init__(mass=self.mass,
                                                        radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(421700, 'km').to('AU')
            self.eccentricity = 0.0041

            super(Io().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                         ecc=self.eccentricity,
                                                         orbital_period=1.769137786,
                                                         av_orbital_speed=17.334,
                                                         inclination=0.05)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            av_ = utilities.Q(1.2, 'arcsec')

            d_ = j_ - Io().OrbitalParameters().semi_major_axis

            super(Io().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                               apparent_mag=5.02,
                                                               geom_albedo=0.63,
                                                               av_ang_size=av_)


class Europa(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(4.799844e22, 'kg')
            self.radius = utilities.Q(1560.8, 'km')

            super(Europa().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(670900, 'km').to('AU')
            self.eccentricity = 0.009

            super(Europa().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=3.551181,
                                                             av_orbital_speed=13.74336,
                                                             inclination=0.470,
                                                             axial_tilt=0.1)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Europa().OrbitalParameters().semi_major_axis

            super(Europa().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=5.29,
                                                                   geom_albedo=0.67)


class Ganymede(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.4819e25, 'kg')
            self.radius = utilities.Q(2634.1, 'km')

            super(Ganymede().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(1070400, 'km').to('AU')
            self.eccentricity = 0.0013

            super(Ganymede().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=7.15455296,
                                                               av_orbital_speed=10.880,
                                                               inclination=2.214,
                                                               axial_tilt=0.165)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            ang_min, ang_max = utilities.Q(1.2, 'arcsec'), utilities.Q(1.8, 'arcsec')

            d_ = j_ - Ganymede().OrbitalParameters().semi_major_axis

            super(Ganymede().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     apparent_mag=4.61,
                                                                     geom_albedo=0.43,
                                                                     ang_min=ang_min,
                                                                     ang_max=ang_max)


class Callisto(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.075938e23, 'kg')
            self.radius = utilities.Q(2410.3, 'km')

            super(Callisto().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(1882700, 'km').to('AU')
            self.eccentricity = 0.0074

            super(Callisto().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=16.6890184,
                                                               av_orbital_speed=8.204,
                                                               inclination=2.017,
                                                               axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Callisto().OrbitalParameters().semi_major_axis

            super(Callisto().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     apparent_mag=5.65,
                                                                     geom_albedo=0.22)


class Metis(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(3.6e16, 'kg')
            self.radius = utilities.Q(21.5, 'km')

            super(Metis().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(128000, 'km').to('AU')
            self.eccentricity = 0.0002

            super(Metis().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.294780,
                                                            av_orbital_speed=31.501,
                                                            inclination=0.06,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Metis().OrbitalParameters().semi_major_axis

            super(Metis().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  geom_albedo=0.061)


class Adrastea(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2e15, 'kg')
            self.radius = utilities.Q(8.2, 'km')

            super(Adrastea().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(129000, 'km').to('AU')
            self.eccentricity = 0.0015

            super(Adrastea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=0.29826,
                                                               av_orbital_speed=31.378,
                                                               inclination=0.03,
                                                               axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Adrastea().OrbitalParameters().semi_major_axis

            super(Adrastea().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     geom_albedo=0.1)


class Amalthea(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2.08e18, 'kg')
            self.radius = utilities.Q(83.5, 'km')

            super(Amalthea().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(181365.84, 'km').to('AU')
            self.eccentricity = 0.00319

            super(Amalthea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=0.49817943,
                                                               av_orbital_speed=26.57,
                                                               inclination=0.374,
                                                               axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Amalthea().OrbitalParameters().semi_major_axis

            super(Amalthea().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     apparent_mag=14.1,
                                                                     geom_albedo=0.09)


class Thebe(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(4.3e17, 'kg')
            self.radius = utilities.Q(49.3, 'km')

            super(Thebe().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(221889.0, 'km').to('AU')
            self.eccentricity = 0.0175

            super(Thebe().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.674536,
                                                            av_orbital_speed=23.92,
                                                            inclination=1.076,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = j_ - Thebe().OrbitalParameters().semi_major_axis

            super(Thebe().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  geom_albedo=0.047)


class Mimas(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(3.7493e19, 'kg')
            self.radius = utilities.Q(198.2, 'km')

            super(Mimas().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(185539, 'km').to('AU')
            self.eccentricity = 0.0196

            super(Mimas().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.942421959,
                                                            av_orbital_speed=14.28,
                                                            inclination=1.574,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Mimas().OrbitalParameters().semi_major_axis

            super(Mimas().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  apparent_mag=12.9,
                                                                  geom_albedo=0.962)


class Enceladus(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.08022e20, 'kg')
            self.radius = utilities.Q(252.1, 'km')

            super(Enceladus().PhysicalParameters, self).__init__(mass=self.mass,
                                                                 radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(237948, 'km').to('AU')
            self.eccentricity = 0.0047

            super(Enceladus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                                ecc=self.eccentricity,
                                                                orbital_period=1.370218,
                                                                inclination=0.009,
                                                                axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Enceladus().OrbitalParameters().semi_major_axis

            super(Enceladus().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                      apparent_mag=11.7,
                                                                      geom_albedo=1.375)


class Tethys(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(6.17449e20, 'kg')
            self.radius = utilities.Q(531.1, 'km')

            super(Tethys().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(294619, 'km').to('AU')
            self.eccentricity = 0.0001

            super(Tethys().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=1.887802,
                                                             av_orbital_speed=11.35,
                                                             inclination=1.12,
                                                             axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Tethys().OrbitalParameters().semi_major_axis

            super(Tethys().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=10.2,
                                                                   geom_albedo=1.229)


class Dione(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.095452e20, 'kg')
            self.radius = utilities.Q(561.4, 'km')

            super(Dione().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(377396, 'km').to('AU')
            self.eccentricity = 0.0022

            super(Dione().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=2.736915,
                                                            inclination=0.019,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Dione().OrbitalParameters().semi_major_axis

            super(Dione().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  apparent_mag=10.4,
                                                                  geom_albedo=0.998)


class Rhea(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2.306518e21, 'kg')
            self.radius = utilities.Q(763.8, 'km')

            super(Rhea().PhysicalParameters, self).__init__(mass=self.mass,
                                                            radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(527108, 'km').to('AU')
            self.eccentricity = 0.0012583

            super(Rhea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                           ecc=self.eccentricity,
                                                           orbital_period=4.518212,
                                                           av_orbital_speed=8.48,
                                                           inclination=0.345,
                                                           axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Rhea().OrbitalParameters().semi_major_axis

            super(Rhea().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                 apparent_mag=10,
                                                                 geom_albedo=0.949)


class Titan(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.3452e23, 'kg')
            self.radius = utilities.Q(2574.73, 'km')

            super(Titan().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(1221870, 'km').to('AU')
            self.eccentricity = 0.0288

            super(Titan().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=15.945,
                                                            av_orbital_speed=5.57,
                                                            inclination=0.34854,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Titan().OrbitalParameters().semi_major_axis

            super(Titan().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  ap_mag_min=9,
                                                                  ap_mag_max=8.2,
                                                                  geom_albedo=0.949)


class Hyperion(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(5.6199e18, 'kg')
            self.radius = utilities.Q(270, 'km')

            super(Hyperion().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(1481009, 'km').to('AU')
            self.eccentricity = 0.1230061

            super(Hyperion().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=21.276,
                                                               inclination=0.43)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Hyperion().OrbitalParameters().semi_major_axis

            super(Hyperion().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     apparent_mag=14.1,
                                                                     geom_albedo=0.949)


class Iapetus(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.805635e21, 'kg')
            self.radius = utilities.Q(1469.0, 'km')

            super(Iapetus().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(3560820, 'km').to('AU')
            self.eccentricity = 0.0276812

            super(Iapetus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=21.276,
                                                              av_orbital_speed=3.26,
                                                              inclination=15.47,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = s_ - Iapetus().OrbitalParameters().semi_major_axis

            super(Iapetus().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    ap_mag_min=11.9,
                                                                    ap_mag_max=10.2,
                                                                    geom_albedo=0.949)


class Miranda(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(6.4e19, 'kg')
            self.radius = utilities.Q(235.8, 'km')

            super(Miranda().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(129390, 'km').to('AU')
            self.eccentricity = 0.0013

            super(Miranda().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=1.413479,
                                                              av_orbital_speed=6.66,
                                                              inclination=4.232,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = u_ - Miranda().OrbitalParameters().semi_major_axis

            super(Miranda().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=15.8,
                                                                    geom_albedo=0.32)


class Umbriel(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.275e21, 'kg')
            self.radius = utilities.Q(584.7, 'km')

            super(Umbriel().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(266000, 'km').to('AU')
            self.eccentricity = 0.0039

            super(Umbriel().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=4.144,
                                                              av_orbital_speed=4.67,
                                                              inclination=0.128,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = u_ - Umbriel().OrbitalParameters().semi_major_axis

            super(Umbriel().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=14.5,
                                                                    geom_albedo=0.26)


class Ariel(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.251e21, 'kg')
            self.radius = utilities.Q(578.9, 'km')

            super(Ariel().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(191020, 'km').to('AU')
            self.eccentricity = 0.0012

            super(Ariel().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=2.520,
                                                            av_orbital_speed=5.51,
                                                            inclination=0.260)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = u_ - Ariel().OrbitalParameters().semi_major_axis

            super(Ariel().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  apparent_mag=14.4,
                                                                  geom_albedo=0.53)


class Titania(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(3.400e21, 'kg')
            self.radius = utilities.Q(788.4, 'km')

            super(Titania().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(435910, 'km').to('AU')
            self.eccentricity = 0.0011

            super(Titania().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=8.706234,
                                                              av_orbital_speed=3.64,
                                                              inclination=0.340)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = u_ - Titania().OrbitalParameters().semi_major_axis

            super(Titania().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=13.9,
                                                                    geom_albedo=0.35)


class Oberon(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(3.076e21, 'kg')
            self.radius = utilities.Q(761.4, 'km')

            super(Oberon().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(583520, 'km').to('AU')
            self.eccentricity = 0.0014

            super(Oberon().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=13.463234,
                                                             av_orbital_speed=3.15,
                                                             inclination=0.058)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = u_ - Oberon().OrbitalParameters().semi_major_axis

            super(Oberon().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=14.1,
                                                                   geom_albedo=0.31)


class Naiad(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(9.2e16, 'kg')
            self.radius = utilities.Q(30.2, 'km')

            super(Naiad().PhysicalParameters, self).__init__(mass=self.mass,
                                                             radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(48224.41, 'km').to('AU')
            self.eccentricity = 0.0047

            super(Naiad().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                            ecc=self.eccentricity,
                                                            orbital_period=0.2943958,
                                                            inclination=4.75,
                                                            axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Naiad().OrbitalParameters().semi_major_axis

            super(Naiad().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                  apparent_mag=23.91,
                                                                  geom_albedo=0.072)


class Thalassa(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(3.5e17, 'kg')
            self.radius = utilities.Q(40.7, 'km')

            super(Thalassa().PhysicalParameters, self).__init__(mass=self.mass,
                                                                radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(50074.44, 'km').to('AU')
            self.eccentricity = 0.00176

            super(Thalassa().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                               ecc=self.eccentricity,
                                                               orbital_period=0.31148444,
                                                               inclination=0.21,
                                                               axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Thalassa().OrbitalParameters().semi_major_axis

            super(Thalassa().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                     apparent_mag=23.32,
                                                                     geom_albedo=0.091)


class Despina(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2.2e18, 'kg')
            self.radius = utilities.Q(78, 'km')

            super(Despina().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(52525.95, 'km').to('AU')
            self.eccentricity = 0.00038

            super(Despina().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=0.33465551,
                                                              inclination=0.216,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Despina().OrbitalParameters().semi_major_axis

            super(Despina().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=22.0,
                                                                    geom_albedo=0.09)


class Galatea(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2.12e18, 'kg')
            self.radius = utilities.Q(87.4, 'km')

            super(Galatea().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(61952.57, 'km').to('AU')
            self.eccentricity = 0.00022

            super(Galatea().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=0.42874431,
                                                              inclination=0.052,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Galatea().OrbitalParameters().semi_major_axis

            super(Galatea().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=21.9,
                                                                    geom_albedo=0.08)


class Larissa(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(4.2e18, 'kg')
            self.radius = utilities.Q(97, 'km')

            super(Larissa().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(73548.26, 'km').to('AU')
            self.eccentricity = 0.001393

            super(Larissa().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=0.55465332,
                                                              inclination=0.251,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Larissa().OrbitalParameters().semi_major_axis

            super(Larissa().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=21.5,
                                                                    geom_albedo=0.09)


class Hippocamp(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(15.9495e15, 'kg')
            self.radius = utilities.Q(17.4, 'km')

            super(Hippocamp().PhysicalParameters, self).__init__(mass=self.mass,
                                                                 radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(105283, 'km').to('AU')
            self.eccentricity = 0.00084

            super(Hippocamp().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                                ecc=self.eccentricity,
                                                                orbital_period=0.95,
                                                                mean_anom=329.901,
                                                                inclination=0.0641,
                                                                long_asc=110.467,
                                                                arg_peri=305.446)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Hippocamp().OrbitalParameters().semi_major_axis

            super(Hippocamp().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                      apparent_mag=26.5,
                                                                      geom_albedo=0.09)


class Proteus(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(4.4e19, 'kg')
            self.radius = utilities.Q(210, 'km')

            super(Proteus().PhysicalParameters, self).__init__(mass=self.mass,
                                                               radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(117647, 'km').to('AU')
            self.eccentricity = 0.00053

            super(Proteus().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                              ecc=self.eccentricity,
                                                              orbital_period=1.12231477,
                                                              av_orbital_speed=7.623,
                                                              inclination=0.524,
                                                              axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Proteus().OrbitalParameters().semi_major_axis

            super(Proteus().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                    apparent_mag=19.7,
                                                                    geom_albedo=0.096)


class Triton(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(2.139e22, 'kg')
            self.radius = utilities.Q(1353.4, 'km')

            super(Triton().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(354759, 'km').to('AU')
            self.eccentricity = 0.000016

            super(Triton().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=5.876854,
                                                             av_orbital_speed=4.39,
                                                             inclination=156.885,
                                                             axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            d_ = n_ - Triton().OrbitalParameters().semi_major_axis

            super(Triton().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   apparent_mag=13.47,
                                                                   # absolute_mag=-1.2,
                                                                   geom_albedo=0.76, )


class Charon(_CelestialObject.c_):

    class PhysicalParameters(_CelestialObject.c_phy):

        def __init__(self):
            self.age = None
            self.mass = utilities.Q(1.586e21, 'kg')
            self.radius = utilities.Q(606, 'km')

            super(Charon().PhysicalParameters, self).__init__(mass=self.mass,
                                                              radius=self.radius)

    class OrbitalParameters(_CelestialObject.c_orb):

        def __init__(self):
            self.semi_major_axis = utilities.Q(19591.4, 'km').to('AU')
            self.eccentricity = 0.0002

            super(Charon().OrbitalParameters, self).__init__(a_0=self.semi_major_axis,
                                                             ecc=self.eccentricity,
                                                             orbital_period=6.3872304,
                                                             av_orbital_speed=0.21,
                                                             inclination=0.080,
                                                             long_asc=223.046,
                                                             axial_tilt=0)

    class ObservationalParameters(_CelestialObject.c_obs):

        def __init__(self):
            av_ = utilities.Q(0.055, 'arcsec')

            d_ = p_ - Charon().OrbitalParameters().semi_major_axis

            super(Charon().ObservationalParameters, self).__init__(dist_from_earth=d_,
                                                                   av_ang_size=av_,
                                                                   apparent_mag=16.8,
                                                                   # absolute_mag=1,
                                                                   geom_albedo=0.35)
