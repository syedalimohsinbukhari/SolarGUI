"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

# added try/except because pip bundle and main file do not work with same imports
try:
    from . import planets as planets
    from . import show_planet as sp
    from . import tk_functions as tk_f
except ImportError:
    import planets as planets
    import show_planet as sp
    import tk_functions as tk_f


# TODO: Get a good font
# TODO: adjust/create designs in tkinter windows
# TODO: make a planets vs Earth/Jupiter/Sun comparison dropdown menu as well


def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 700, 240
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('SolarGUI')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')
    # do not let it be resized smaller than it already is
    root_window.minsize(_w, _h)

    ##################################################################################
    # Working
    ##################################################################################

    welcome_label = tk.Label(master=root_window,
                             text='Welcome to Solar Explorer. Please select a button.')
    welcome_label.grid(row=0, column=0, columnspan=9, pady=10, ipady=10)

    # yes I know :D
    # planet_button(window=root_window, text='Sun', function=show_earth, column=0)

    tk_f.planet_button(window=root_window, text=' Sun  ',
                       function=lambda: sp.show_planet(window=root_window, text='Sun',
                                                       planet_class=planets.Sun()),
                       column=0)

    tk_f.planet_button(window=root_window, text='Mercury',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Mercury',
                                                       planet_class=planets.Mercury()),
                       column=1)

    tk_f.planet_button(window=root_window, text='Venus',
                       function=lambda: sp.show_planet(window=root_window, text='Venus',
                                                       planet_class=planets.Venus()),
                       column=2)

    tk_f.planet_button(window=root_window, text='Earth',
                       function=lambda: sp.show_planet(window=root_window, text='Earth',
                                                       planet_class=planets.Earth()),
                       column=3)

    tk_f.planet_button(window=root_window, text='Mars',
                       function=lambda: sp.show_planet(window=root_window, text='Mars',
                                                       planet_class=planets.Mars()),
                       column=4)

    tk_f.planet_button(window=root_window, text='Jupiter',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Jupiter',
                                                       planet_class=planets.Jupiter()),
                       column=5)

    tk_f.planet_button(window=root_window, text='Saturn',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Saturn',
                                                       planet_class=planets.Saturn()),
                       column=6)

    tk_f.planet_button(window=root_window, text='Uranus',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Uranus',
                                                       planet_class=planets.Uranus()),
                       column=7)

    tk_f.planet_button(window=root_window, text='Neptune',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Neptune',
                                                       planet_class=planets.Neptune()),
                       column=8)

    tk_f.planet_button(window=root_window, text='Moon',
                       function=lambda: sp.show_planet(window=root_window,
                                                       text='Moon',
                                                       planet_class=planets.Moon()),
                       column=0,
                       row=2)

    tk_f.planet_button(window=root_window, text='  Pluto  ',
                       function=lambda: sp.show_planet(window=root_window, text='Pluto',
                                                       planet_class=planets.Pluto()),
                       column=1,
                       row=2)

    ##################################################################################
    # Show it
    ##################################################################################
    root_window.mainloop()


# taken from
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and
# -scripts/
if __name__ == '__main__':
    try:
        sys.exit(main())
    except TypeError:
        pass
