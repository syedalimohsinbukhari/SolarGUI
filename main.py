"""
Created on May 22 00:40:38 2022
"""
import sys
import tkinter as tk

from planets import mercury, venus, earth, mars, jupiter, saturn, uranus, neptune
from planets.others import pluto, moon, sun
from show_planet import show_planet
from tk_functions import planet_button


# TODO: make a planets vs Earth/Jupiter/Sun comparison dropdown menu as well


def main():

    ###################################################################################
    # Initialization
    ###################################################################################

    # set the width and height of the original window
    _w, _h = 800, 240
    # main is the master name in which all work is going to be done
    root_window = tk.Tk()
    # set the title of the GUI window
    root_window.title('[Enter appropriate name here]')
    # set the size of the GUI window
    root_window.geometry(f'{_w}x{_h}')
    # do not let it be resized smaller than it already is
    root_window.minsize(_w, _h)

    ##################################################################################
    # Working
    ##################################################################################

    welcome_label = tk.Label(master=root_window,
                             text='Welcome to Solar Explorer.\nPlease select a '
                                  'button.')
    welcome_label.grid(row=0, column=0, columnspan=9, pady=10, ipady=10)

    # yes I know :D
    # planet_button(window=root_window, text='Sun', function=show_earth, column=0)

    planet_button(window=root_window, text='Sun',
                  function=lambda: show_planet(window=root_window, text='Sun',
                                               planet_class=sun.Sun()), column=0)

    planet_button(window=root_window, text='Mercury',
                  function=lambda: show_planet(window=root_window, text='Mercury',
                                               planet_class=mercury.Mercury()), column=1)

    planet_button(window=root_window, text='Venus',
                  function=lambda: show_planet(window=root_window, text='Venus',
                                               planet_class=venus.Venus()), column=2)

    planet_button(window=root_window, text='Earth',
                  function=lambda: show_planet(window=root_window, text='Earth',
                                               planet_class=earth.Earth()), column=3)

    planet_button(window=root_window, text='Mars',
                  function=lambda: show_planet(window=root_window, text='Mars',
                                               planet_class=mars.Mars()), column=4)

    planet_button(window=root_window, text='Jupiter',
                  function=lambda: show_planet(window=root_window, text='Jupiter',
                                               planet_class=jupiter.Jupiter()), column=5)

    planet_button(window=root_window, text='Saturn',
                  function=lambda: show_planet(window=root_window, text='Saturn',
                                               planet_class=saturn.Saturn()), column=6)

    planet_button(window=root_window, text='Uranus',
                  function=lambda: show_planet(window=root_window, text='Uranus',
                                               planet_class=uranus.Uranus()), column=7)

    planet_button(window=root_window, text='Neptune',
                  function=lambda: show_planet(window=root_window, text='Neptune',
                                               planet_class=neptune.Neptune()), column=8)

    planet_button(window=root_window, text='Moon',
                  function=lambda: show_planet(window=root_window, text='Moon',
                                               planet_class=moon.Moon()), column=4, row=2)

    planet_button(window=root_window, text='Pluto  ',
                  function=lambda: show_planet(window=root_window, text='Pluto',
                                               planet_class=pluto.Pluto()), column=5,
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
